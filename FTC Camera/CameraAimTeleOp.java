/*
 * CameraAimTeleOp.java
 * Prolabs Robotics, FTC Bangalore Resources (Aarav J. and collaborators)
 *
 * Starter TeleOp for the goBILDA FTC StarterBot 2026-27 (BIOBUZZ) with the V3 shooter
 * and one USB webcam named "Webcam 1".
 *
 * What it does:
 *   1. Finds our alliance HIVE CELL AprilTag cluster with the FTC SDK VisionPortal
 *      and AprilTagProcessor (tag36h11, SDK 12.0 or newer).
 *   2. Hold LEFT BUMPER: the robot turns by itself to face the cell opening (auto-aim assist).
 *      The driver still controls forward and back with the left stick.
 *   3. Hold RIGHT BUMPER: the launcher spins up. Its speed comes from a distance table,
 *      using the range the camera measured. The feeder only runs when the launcher is at
 *      speed (and, while aiming, only when the robot is lined up).
 *
 * Built from the official FTC SDK samples ConceptAprilTag, ConceptAprilTagOptimizeExposure
 * and RobotAutoDriveToAprilTagTank, and from goBILDA's BioBuzzStarterBotTeleop example.
 * Hardware names match goBILDA's example code.
 *
 * IMPORTANT: NOT ROBOT TESTED YET. Every number marked TUNE is a starting guess.
 * Test on blocks with the wheels off the ground first.
 *
 * Put this file in TeamCode/src/main/java/org/firstinspires/ftc/teamcode/
 */
package org.firstinspires.ftc.teamcode;

import android.util.Size;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.CRServo;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorEx;
import com.qualcomm.robotcore.hardware.DcMotorSimple;
import com.qualcomm.robotcore.hardware.PIDFCoefficients;
import com.qualcomm.robotcore.util.ElapsedTime;
import com.qualcomm.robotcore.util.Range;

import org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName;
import org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl;
import org.firstinspires.ftc.robotcore.external.hardware.camera.controls.GainControl;
import org.firstinspires.ftc.robotcore.external.navigation.AngleUnit;
import org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit;
import org.firstinspires.ftc.vision.VisionPortal;
import org.firstinspires.ftc.vision.apriltag.AprilTagClusterDetection;
import org.firstinspires.ftc.vision.apriltag.AprilTagDetection;
import org.firstinspires.ftc.vision.apriltag.AprilTagGameDatabase;
import org.firstinspires.ftc.vision.apriltag.AprilTagProcessor;
import org.firstinspires.ftc.vision.apriltag.AprilTagSingleDetection;

import java.util.List;
import java.util.concurrent.TimeUnit;

@TeleOp(name = "Camera Aim TeleOp (V3 shooter)", group = "Prolabs")
public class CameraAimTeleOp extends LinearOpMode {

    // ---------------- Match settings ----------------
    /** Set before each match. true = RED alliance, false = BLUE alliance. */
    static final boolean RED_ALLIANCE = true;

    /**
     * Bench test mode. true = also accept single tags that are in the SDK library
     * (for example the sample tags 583 to 586) so we can test at a desk without a HIVE.
     * Set to false for matches.
     */
    static final boolean ALLOW_SINGLE_TAGS_FOR_BENCH_TEST = true;

    // ---------------- Camera settings ----------------
    static final String WEBCAM_NAME = "Webcam 1";        // must match the robot configuration
    static final int CAMERA_WIDTH = 640;                 // 640x480 has a built-in SDK calibration
    static final int CAMERA_HEIGHT = 480;                //   for the Logitech C920 and C270
    static final float DECIMATION = 2;                   // TUNE: 1 = longer range, 3 = faster
    static final boolean USE_MANUAL_EXPOSURE = true;     // short exposure = less motion blur
    static final int EXPOSURE_MS = 6;                    // TUNE: value from the official sample
    static final int GAIN = 250;                         // TUNE: raise if the image is too dark

    // ---------------- Aim settings (Python v1 ideas, in Java) ----------------
    static final double TURN_GAIN = 0.01;                // TUNE: turn power per degree of error
    static final double MAX_AUTO_TURN = 0.30;            // TUNE: cap on auto turn power
    static final double AIM_TOLERANCE_DEG = 2.0;         // TUNE: "aligned" if error is inside this
    static final double BEARING_OFFSET_DEG = 0.0;        // TUNE: if the camera is not on the shot line
    static final int FRAMES_TO_CONFIRM = 3;              // v1 debounce: need 3 fresh frames in a row
    static final double TARGET_TIMEOUT_S = 0.30;         // v1 GUIDE_MAX_AGE idea: forget old targets

    // ---------------- Launcher settings ----------------
    static final double LAUNCHER_DEFAULT_VELOCITY = 1250; // goBILDA example value (ticks per second)
    static final double LAUNCHER_TOLERANCE = 50;          // TUNE: "at speed" window (ticks per second)

    /**
     * Distance table: camera range (inches) to launcher velocity (ticks per second).
     * EXAMPLE NUMBERS ONLY. Fill these in from real test shots (see the plan, Phase 6).
     * Keep the ranges in increasing order.
     */
    static final double[] TABLE_RANGE_IN  = {  24,   36,   48,   60,   72 };
    static final double[] TABLE_VELOCITY  = { 1150, 1200, 1250, 1320, 1400 };

    // ---------------- Hardware ----------------
    private DcMotor leftDrive, rightDrive, intake;
    private DcMotorEx launcher;
    private CRServo windmillServo, leftIntakeServo, rightIntakeServo;

    // ---------------- Vision ----------------
    private VisionPortal visionPortal;
    private AprilTagProcessor aprilTag;

    // ---------------- Target state ----------------
    private boolean targetLocked = false;     // true after FRAMES_TO_CONFIRM fresh frames in a row
    private int framesSeen = 0;
    private String targetName = "none";
    private double targetRange = 0;           // inches, camera to target
    private double targetBearing = 0;         // degrees, + means target is to the LEFT
    private double targetRoll = 0;            // degrees, used to skip upside down cells
    private int targetPercentFound = 0;
    private final ElapsedTime sinceLastSeen = new ElapsedTime();

    @Override
    public void runOpMode() {
        initHardware();
        initAprilTag();
        if (USE_MANUAL_EXPOSURE) {
            setManualExposure(EXPOSURE_MS, GAIN);
        }

        telemetry.addData("Alliance", RED_ALLIANCE ? "RED" : "BLUE");
        telemetry.addData("Camera preview", "3 dots menu, Camera Stream");
        telemetry.addData(">", "Touch START");
        telemetry.update();
        waitForStart();

        while (opModeIsActive()) {
            updateTarget();

            // ----- Drive (same arcade style as goBILDA's TeleOp) -----
            double forward = -gamepad1.left_stick_y;
            double rotate = gamepad1.right_stick_x;            // + turns right (clockwise)
            boolean aiming = gamepad1.left_bumper;
            double aimError = targetBearing - BEARING_OFFSET_DEG;
            boolean aligned = targetLocked && Math.abs(aimError) < AIM_TOLERANCE_DEG;

            if (aiming && targetLocked) {
                // bearing + means target is LEFT, so we turn left (negative rotate).
                rotate = Range.clip(-aimError * TURN_GAIN, -MAX_AUTO_TURN, MAX_AUTO_TURN);
                if (aligned) {
                    rotate = 0;                                // v1 "STOP / Aligned"
                }
            }
            arcadeDrive(forward, rotate);

            // ----- Intake -----
            double intakePower = gamepad1.right_trigger - gamepad1.left_trigger;

            // ----- Launcher -----
            double targetVelocity = targetLocked ? velocityForRange(targetRange)
                                                 : LAUNCHER_DEFAULT_VELOCITY;
            boolean atSpeed = false;
            if (gamepad1.right_bumper) {
                launcher.setVelocity(targetVelocity);
                atSpeed = Math.abs(launcher.getVelocity() - targetVelocity) < LAUNCHER_TOLERANCE;
            } else {
                launcher.setVelocity(0);
            }

            boolean okToFeed = gamepad1.right_bumper && atSpeed && (!aiming || aligned);
            if (okToFeed) {
                windmillServo.setPower(1);
                intakePower += 0.5;                            // same push as goBILDA's code
            } else {
                windmillServo.setPower(0);
            }
            intakePower = Range.clip(intakePower, -1, 1);
            intake.setPower(intakePower);
            leftIntakeServo.setPower(intakePower);
            rightIntakeServo.setPower(intakePower);

            // ----- Telemetry -----
            telemetry.addData("Target", targetLocked ? targetName : "none (drive to find one)");
            if (targetLocked) {
                telemetry.addData("Range", "%5.1f in", targetRange);
                telemetry.addData("Bearing", "%5.1f deg (error %5.1f)", targetBearing, aimError);
                telemetry.addData("Roll", "%5.1f deg", targetRoll);
                telemetry.addData("Tags seen", "%d %%", targetPercentFound);
            }
            telemetry.addData("Aim", aiming ? (aligned ? "ALIGNED" : "turning") : "manual (hold LB)");
            telemetry.addData("Launcher", "%4.0f / %4.0f %s", launcher.getVelocity(), targetVelocity,
                    atSpeed ? "AT SPEED" : "");
            telemetry.update();

            sleep(10);
        }

        visionPortal.close();
    }

    /** Reads new detections, picks the best target, and keeps a short memory of it. */
    private void updateTarget() {
        // getFreshDetections() returns null if no new frame was processed since the last call.
        // This keeps our "3 frames in a row" count honest.
        List<AprilTagDetection> fresh = aprilTag.getFreshDetections();
        if (fresh != null) {
            AprilTagDetection best = null;
            int bestPercent = -1;
            String bestName = "none";

            for (AprilTagDetection detection : fresh) {
                if (detection.ftcPose == null) {
                    continue;                                  // no pose, cannot aim at it
                }
                if (detection instanceof AprilTagClusterDetection) {
                    AprilTagClusterDetection cluster = (AprilTagClusterDetection) detection;
                    String name = cluster.metadata.name;       // "RED SCORING", "BLUE AUDIENCE", ...
                    boolean ourAlliance = RED_ALLIANCE ? name.startsWith("R") : name.startsWith("B");
                    boolean rightSideUp = Math.abs(detection.ftcPose.roll) < 90; // scorable cell
                    if (!ourAlliance || !rightSideUp) {
                        continue;
                    }
                    // Prefer the cluster with more tags visible, then the closer one.
                    if (cluster.percentClusterFound > bestPercent
                            || (cluster.percentClusterFound == bestPercent && best != null
                                && detection.ftcPose.range < best.ftcPose.range)) {
                        best = detection;
                        bestPercent = cluster.percentClusterFound;
                        bestName = name;
                    }
                } else if (ALLOW_SINGLE_TAGS_FOR_BENCH_TEST
                        && detection instanceof AprilTagSingleDetection) {
                    AprilTagSingleDetection single = (AprilTagSingleDetection) detection;
                    if (single.metadata != null && best == null) {
                        best = detection;
                        bestPercent = 0;
                        bestName = "bench tag " + single.id;
                    }
                }
            }

            if (best != null) {
                framesSeen++;
                targetName = bestName;
                targetRange = best.ftcPose.range;
                targetBearing = best.ftcPose.bearing;
                targetRoll = best.ftcPose.roll;
                targetPercentFound = bestPercent;
                sinceLastSeen.reset();
                if (framesSeen >= FRAMES_TO_CONFIRM) {
                    targetLocked = true;
                }
            } else {
                framesSeen = 0;
            }
        }

        // Forget the target if we have not seen it for a short time.
        if (sinceLastSeen.seconds() > TARGET_TIMEOUT_S) {
            targetLocked = false;
            framesSeen = 0;
            targetName = "none";
        }
    }

    /** Straight-line interpolation in the distance table, clamped at both ends. */
    private double velocityForRange(double rangeIn) {
        int last = TABLE_RANGE_IN.length - 1;
        if (rangeIn <= TABLE_RANGE_IN[0]) return TABLE_VELOCITY[0];
        if (rangeIn >= TABLE_RANGE_IN[last]) return TABLE_VELOCITY[last];
        for (int i = 0; i < last; i++) {
            double r0 = TABLE_RANGE_IN[i], r1 = TABLE_RANGE_IN[i + 1];
            if (rangeIn <= r1) {
                double t = (rangeIn - r0) / (r1 - r0);
                return TABLE_VELOCITY[i] + t * (TABLE_VELOCITY[i + 1] - TABLE_VELOCITY[i]);
            }
        }
        return LAUNCHER_DEFAULT_VELOCITY;
    }

    private void arcadeDrive(double forward, double rotate) {
        double left = forward + rotate;
        double right = forward - rotate;
        double max = Math.max(1.0, Math.max(Math.abs(left), Math.abs(right)));
        leftDrive.setPower(left / max);
        rightDrive.setPower(right / max);
    }

    private void initHardware() {
        // Names match goBILDA's BIOBUZZ StarterBot example code and robot configuration.
        leftDrive = hardwareMap.get(DcMotor.class, "left_drive");
        rightDrive = hardwareMap.get(DcMotor.class, "right_drive");
        intake = hardwareMap.get(DcMotor.class, "intake");
        launcher = hardwareMap.get(DcMotorEx.class, "launcher");
        windmillServo = hardwareMap.get(CRServo.class, "windmill");
        leftIntakeServo = hardwareMap.get(CRServo.class, "left_intake_servo");
        rightIntakeServo = hardwareMap.get(CRServo.class, "right_intake_servo");

        leftDrive.setDirection(DcMotor.Direction.FORWARD);
        rightDrive.setDirection(DcMotor.Direction.REVERSE);
        leftDrive.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);
        rightDrive.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);

        launcher.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);
        launcher.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
        launcher.setPIDFCoefficients(DcMotor.RunMode.RUN_USING_ENCODER,
                new PIDFCoefficients(40, 0, 0, 12.5));          // goBILDA example values

        rightIntakeServo.setDirection(DcMotorSimple.Direction.REVERSE);
        windmillServo.setDirection(DcMotorSimple.Direction.REVERSE);
    }

    private void initAprilTag() {
        aprilTag = new AprilTagProcessor.Builder()
                .setTagFamily(AprilTagProcessor.TagFamily.TAG_36h11)
                .setTagLibrary(AprilTagGameDatabase.getCurrentGameTagLibrary())
                .setOutputUnits(DistanceUnit.INCH, AngleUnit.DEGREES)
                .setDrawTagOutline(true)
                // Only needed if our camera or resolution is NOT in the SDK's built-in list.
                // Values are fx, fy, cx, cy from our own calibration:
                // .setLensIntrinsics(578.272, 578.272, 402.145, 221.506)
                .build();
        aprilTag.setDecimation(DECIMATION);

        visionPortal = new VisionPortal.Builder()
                .setCamera(hardwareMap.get(WebcamName.class, WEBCAM_NAME))
                .setCameraResolution(new Size(CAMERA_WIDTH, CAMERA_HEIGHT))
                .setStreamFormat(VisionPortal.StreamFormat.MJPEG)   // less USB bandwidth
                .addProcessor(aprilTag)
                .build();
    }

    /** Short exposure and higher gain to cut motion blur. Same steps as the official sample. */
    private void setManualExposure(int exposureMS, int gain) {
        if (visionPortal == null) return;

        while (!isStopRequested()
                && visionPortal.getCameraState() != VisionPortal.CameraState.STREAMING) {
            telemetry.addData("Camera", "Waiting for stream");
            telemetry.update();
            sleep(20);
        }
        if (isStopRequested()) return;

        ExposureControl exposureControl = visionPortal.getCameraControl(ExposureControl.class);
        if (exposureControl.getMode() != ExposureControl.Mode.Manual) {
            exposureControl.setMode(ExposureControl.Mode.Manual);
            sleep(50);
        }
        exposureControl.setExposure((long) exposureMS, TimeUnit.MILLISECONDS);
        sleep(20);
        GainControl gainControl = visionPortal.getCameraControl(GainControl.class);
        gainControl.setGain(gain);
        sleep(20);
        telemetry.addData("Camera", "Ready");
        telemetry.update();
    }
}
