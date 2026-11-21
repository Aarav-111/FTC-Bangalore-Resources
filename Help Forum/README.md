# Help Forum

This is the help page for [FTC India Resources](https://github.com/Aarav-111/FTC-India-Resources). We wrote it for Indian FTC teams who are using this repository, the V3 shooter kit, the intake upgrade, the camera plan, or the mecanum presentation.

We use simple English, and we only state facts we can stand behind. If something is a guess, a CAD number, or not yet tested on a robot, we say so. Approximate values are marked with "about" or "approximate".

If your question is not answered here, see [Ask a question](#ask-a-question) at the bottom of this page.

## Contents

1. [Frequently asked questions](#frequently-asked-questions)
   - [General FTC](#general-ftc)
   - [BIOBUZZ season basics](#biobuzz-season-basics)
   - [This repository](#this-repository)
2. [The basics](#the-basics)
   - [How to use the guides](#how-to-use-the-guides)
   - [Printing](#printing)
   - [Wiring](#wiring)
   - [The SDK](#the-sdk)
   - [The Driver Hub](#the-driver-hub)
3. [Common mistakes](#common-mistakes)
4. [Troubleshooting](#troubleshooting)
5. [Ask a question](#ask-a-question)
6. [Links to files in this repository](#links-to-files-in-this-repository)

---

## Frequently asked questions

### General FTC

**What is FTC?**

FTC is FIRST Tech Challenge, a student robotics competition. This repository is for the **FTC 2027 Challenge**, which was released in 2026. We started the collection in Bangalore, but it is for every FTC team in India.

**What is the Control Hub, and what is the Driver Hub?**

The REV Control Hub is the computer on the robot. It runs your OpModes and talks to motors, servos and sensors. The REV Driver Hub is the driver station you hold. You use it to pick an OpMode, press INIT and START, watch telemetry, and (during INIT) open the camera preview.

**What do INIT and START mean?**

INIT is the period after you press INIT and before you press START. The robot can power up hardware, open the webcam, and show telemetry, but the match has not started. START runs the OpMode for real. This matters for the camera: the Driver Hub Camera Stream is meant to be used during INIT. See [The Driver Hub](#the-driver-hub).

**Which SDK should we use?**

Our Java camera plan and [`CameraAimTeleOp.java`](../FTC%20Camera/CameraAimTeleOp.java) were written for **FTC SDK v12.0**, the official 2026-27 release. Older AprilTag code that reads `detection.id` on every detection will not compile on SDK v12.0, because detections are now two types. Please see the [Camera Integration Plan](../FTC%20Camera/Camera%20Integration%20Plan.md).

**Where do the official rules come from?**

This repository is a set of team resources. It is not the rule book. For game rules, tag print files, and field setup, use the official [FTC Competition Manual and game resources](https://ftc-resources.firstinspires.org/ftc/game/manual). For software and hardware setup, use [FTC Docs](https://ftc-docs.firstinspires.org/).

### BIOBUZZ season basics

**What game is this season?**

The 2026-27 season game is **BIOBUZZ**. Our V3 shooter kit and camera plan are written for the [goBILDA FTC StarterBot 2026-27](https://www.gobilda.com/ftc-starter-bot-resource-guide-2026-2027-season/) with our upgrades. We have not copied the full game rules into this repository, so please read the official manual for scoring, timing, and what is legal.

**What are POLLEN and NECTAR?**

These are game elements from BIOBUZZ, as used in our shooter fit checks:

| Element | Size we used | How it fits our V3 shooter channel |
|---|---|---|
| POLLEN | 71 mm | Fits. CAD shows about 8.5 mm of room per side |
| NECTAR | 91 mm | About 3 mm too wide. The channel is borderline, so we treat it as **POLLEN only** until we test on a robot |

Those fit numbers are from CAD. The kit has been built on a robot, but **shooting has not been tested yet**. Please check the fit by hand before competition use. Details are in the [BOM and 3D printing Guide](../FTC%20Kits/Shooter%20Upgrade%20Kit/BOM%20%26%203D%20printing%20Guide.md).

**What is a HIVE CELL, and how do AprilTags work this season?**

Each HIVE CELL has a **4-tag AprilTag cluster** on its underside. The tags are family **tag36h11**. According to the official FTC docs and SDK v12.0 (as summarised in our [Camera Integration Plan](../FTC%20Camera/Camera%20Integration%20Plan.md)):

- BIOBUZZ has **4 clusters and no single tags**.
- The four cluster names in SDK v12.0 are `RED SCORING`, `RED AUDIENCE`, `BLUE AUDIENCE` and `BLUE SCORING`.
- The cluster pose points to roughly the centre of the CELL opening, which is useful for aiming.
- CELLs tip during the match, so we should aim with the relative pose (`range` and `bearing`) and not trust field position (`robotPose`) from these tags.

Print practice tags at real size from the official game resources. Tag IDs should be checked against the Competition Manual before you print.

**Has the V3 shooter been shooting tested?**

No. It has been built on a robot. We have [photos and a short walkaround video](../FTC%20precise%20shooting%20mechanism/V3%20Shooter%203D%20files/Testing%20videos%20and%20photos) of the finished build. Shooting test videos are not online yet. Fit numbers in the guides are from CAD.

**Has the camera Java code been tested on a robot?**

No. We wrote the [Camera Integration Plan](../FTC%20Camera/Camera%20Integration%20Plan.md) and [`CameraAimTeleOp.java`](../FTC%20Camera/CameraAimTeleOp.java) from official FTC docs and samples, and we compiled the Java against SDK v12.0. We have not run it on a robot or a BIOBUZZ field yet. Numbers marked TUNE in the code are starting guesses.

### This repository

**Who made this repository?**

It was created by Aarav Jaisingh (Aarav J.), in collaboration with Team R- Factor (FRC), led by Nilesh Shah, and supported by Prolabs Robotics. The project is under the MIT License.

**What is in this repository?**

| Folder or file | What it is |
|---|---|
| [FTC Kits](../FTC%20Kits) | Everything for each upgrade kit: the [Shooter Upgrade Kit](../FTC%20Kits/Shooter%20Upgrade%20Kit) (V3 guide, BOM) and the [Intake Upgrade Kit](../FTC%20Kits/Intake%20Upgrade%20Kit) (intake guide, STL) |
| [FTC precise shooting mechanism](../FTC%20precise%20shooting%20mechanism) | V3 shooter print files, theory PDF, photos |
| [FTC Intake mechanism Upgrade](../FTC%20Intake%20mechanism%20Upgrade) | v1 intake roller STL, the FTC Intake Attachment STL, printing guide, and calculations |
| [FTC Camera](../FTC%20Camera) | Laptop Python app, buying guide, Java integration plan, and starter OpMode |
| [FTC Chassis options](../FTC%20Chassis%20options) | Mecanum wheels presentation (PDF, PowerPoint, and Google Slides) |
| [FTC Docs by Aarav Jaisingh](../FTC%20Docs%20by%20Aarav%20Jaisingh) | Shooting and intake strategy guide, plus a copy of the mecanum presentation |
| [Help Forum](./README.md) | This page |

There is also a 1-byte placeholder file at the repo root named `FTC chassis options`. The real chassis materials are in the folder [`FTC Chassis options`](../FTC%20Chassis%20options) (capital C).

**What is in each kit, and where are the kit files?**

All kit files are in [FTC Kits](../FTC%20Kits):

- [Shooter Upgrade Kit](../FTC%20Kits/Shooter%20Upgrade%20Kit): 1 V3 shooter, 2 Plate 368 (1 spare), 2 OP2 sheets (one on each side, flared out), electrical tape, zip ties, and a small bottle of super glue. Guide: [V3 Shooting Assembly Guide](../FTC%20Kits/Shooter%20Upgrade%20Kit/V3%20Shooting%20Assembly%20Guide.pdf).
- [Intake Upgrade Kit](../FTC%20Kits/Intake%20Upgrade%20Kit): 1 FTC intake attachment, foam, and zip ties. Guide: [Intake Assembly Guide](../FTC%20Kits/Intake%20Upgrade%20Kit/Intake%20Assembly%20Guide.pdf) (13 pages, 7 steps).

**How much foam goes on the intake attachment?**

Wrap the foam layer by layer until it reaches the POLLEN: it should just touch the POLLEN and give it a light squeeze, about 2 to 3 mm. About 50 mm across is a good place to start testing, but the POLLEN fit check (step 5 in the [Intake Assembly Guide](../FTC%20Kits/Intake%20Upgrade%20Kit/Intake%20Assembly%20Guide.pdf)) decides the real size. This has not been tested on a robot yet.

**Do we have to copy the designs exactly?**

No. Please treat these designs as a strong starting point. Every team has different parts, budgets, and tools. Change sizes, motors, and materials to match what your team has, and check the fit on your own robot.

**Where should a new team start?**

1. Read this Help Forum, then the main [README](../README.md).
2. For a chassis and for mecanum driving, open [FTC Chassis options](../FTC%20Chassis%20options).
3. For the shooter, read the [BOM and 3D printing Guide](../FTC%20Kits/Shooter%20Upgrade%20Kit/BOM%20%26%203D%20printing%20Guide.md), then follow the [V3 Shooting Assembly Guide](../FTC%20Kits/Shooter%20Upgrade%20Kit/V3%20Shooting%20Assembly%20Guide.pdf) (27 pages, 15 steps).
4. For intake and scoring ideas, read the guide in [FTC Docs by Aarav Jaisingh](../FTC%20Docs%20by%20Aarav%20Jaisingh). The v1 intake roller files are in [FTC Intake mechanism Upgrade](../FTC%20Intake%20mechanism%20Upgrade). To build the intake kit, follow the [Intake Assembly Guide](../FTC%20Kits/Intake%20Upgrade%20Kit/Intake%20Assembly%20Guide.pdf).
5. For vision, pick a webcam with the [Camera buying Guide](../FTC%20Camera/Camera%20buying%20Guide.md), then follow the [Camera Integration Plan](../FTC%20Camera/Camera%20Integration%20Plan.md). The Python file is a laptop practice tool, not robot code.

**Is `FTC-camera(v1).py` the code we put on the robot?**

No. [`FTC-camera(v1).py`](../FTC%20Camera/FTC-camera(v1).py) runs on a laptop (it uses OpenCV, `pupil_apriltags`, Tkinter, and on a Mac it can use voice prompts). None of that runs on the Control Hub. On the robot we use Java (or Blocks) on the FTC SDK. The starter OpMode is [`CameraAimTeleOp.java`](../FTC%20Camera/CameraAimTeleOp.java).

**Where is the mecanum presentation?**

In [`FTC Chassis options`](../FTC%20Chassis%20options), by Aarav J.:

- [PDF](../FTC%20Chassis%20options/Mecanum%20Wheels%20Presentation.pdf)
- [PowerPoint](../FTC%20Chassis%20options/Mecanum%20Wheels%20Presentation.pptx)
- [Google Slides](https://docs.google.com/presentation/d/10t6m5lrtCYghSzNBLcLgv_6zWi-kxssT0vhTHXqJd7Y/edit)

The deck covers how mecanum wheels move, simple trigonometry for driving at any angle, driving on curves, normalising wheel powers, step-by-step calculations, Java for robot-centric and field-centric drive, and testing. The main README describes the current deck as 18 slides, including a "What are mecanum wheels?" slide.

**How do we get a copy of the files?**

You can browse on GitHub, or:

```bash
git clone https://github.com/Aarav-111/FTC-India-Resources.git
cd FTC-India-Resources
```

If you do not use Git, click the green **Code** button on GitHub and choose **Download ZIP**.

---

## The basics

### How to use the guides

- Read the guide for a part **before** you print or cut anything. Most build mistakes happen when a team starts building before it understands the full design.
- For the V3 shooter, the **main** assembly guide is the [V3 Shooting Assembly Guide PDF](../FTC%20Kits/Shooter%20Upgrade%20Kit/V3%20Shooting%20Assembly%20Guide.pdf). The BOM page also has a short list of steps, but the PDF is the full, updated version (27 pages, 15 steps, 3D pictures, and 5 real photos). There is also an [interactive 3D simulator](https://ftc-shooter-interactive-guide.netlify.app/) that compares V3 with the older V2.
- The shooter kit is **V3 only**. The older V2 rail guard is in [Older versions](../FTC%20precise%20shooting%20mechanism/V3%20Shooter%203D%20files/Older%20versions). It is not in the kit. Do not print V2 unless you want that older part on purpose.
- For the intake roller, start with [v1 by Aarav Jaisingh](../FTC%20Intake%20mechanism%20Upgrade/v1%20by%20Aarav%20Jaisingh.md), then the [Printing Guide](../FTC%20Intake%20mechanism%20Upgrade/Printing%20Guide.md). How the roller is mounted on the robot is still to confirm. Some foam notes are in [Intake Calculations](../FTC%20Intake%20mechanism%20Upgrade/Intake%20Calculations.md), and those readings also still need a check.
- For the camera, read the plan first, then put [`CameraAimTeleOp.java`](../FTC%20Camera/CameraAimTeleOp.java) in `TeamCode/src/main/java/org/firstinspires/ftc/teamcode/`. Hardware names in that file match goBILDA's StarterBot example: `left_drive`, `right_drive`, `intake`, `launcher`, `windmill`, `left_intake_servo`, `right_intake_servo`. The webcam must be named exactly `Webcam 1`.
- CAD suggestions (for example the intake plate tilt) should be checked on your own robot. Do not treat example launcher speeds in the Java file as real match values.

### Printing

Our standing rule for these kit parts is **100% infill** (fully solid).

**V3 shooter** (from the [BOM and 3D printing Guide](../FTC%20Kits/Shooter%20Upgrade%20Kit/BOM%20%26%203D%20printing%20Guide.md)):

| Setting | V3 rail guard | OP2 sheet (print 2) | Plate 368 |
|---|---|---|---|
| File | `FTC Shooter V3 Rail Guard.stl` | `prolabs_plain_sheet_0p2.stl` | `plate_368_cut_5x5.stl` |
| Size | about 217 x 88 x 116 mm | 88 x 104 x 0.2 mm | 40 x 40 x 1.5 mm |
| Material | PETG or PLA+ | PETG | PETG or PLA+ |
| Infill | 100% | 100% | 100% |
| Orientation | **Sideways** | Flat on the bed | Flat on the bed |
| Supports | None | None | None |
| Other | 5 mm brim | One 0.2 mm layer, level bed, slow first layer | 0.2 mm layers |

Print the rail guard sideways so the main shooter curve stays smooth. A rough curve can cause shooting problems. Do not print it vertically. Do not use supports on any of these three parts.

**Intake Upgrade v1** (from the [Printing Guide](../FTC%20Intake%20mechanism%20Upgrade/Printing%20Guide.md)):

| Setting | Our recommendation |
|---|---|
| File | `Intake Upgrade v1.stl` |
| Shape | 180 mm long roller, about 30 mm diameter, 7.00 mm hex hole across flats, through the full length |
| Orientation | Standing on one flat end, so the part is 180 mm tall |
| Infill | 100% (the original 3MF still had 15%, please change this) |
| Walls | 3 or 4 |
| Supports | None |
| Brim | 5 to 8 mm |
| Layer height | 0.2 mm |
| Material | PETG or PLA (please confirm which one you will use) |

A tall, thin part can wobble. Print one roller at a time, slow the outer walls, and use a brim so the base holds. The printer needs at least 180 mm of Z height. A Bambu Lab A1 mini is exactly 180 mm tall, so this part is right at the limit. Check the height in the slicer, including the brim.

After printing, let the part cool, peel the brim carefully, and check length, diameter, and the hex hole at both ends. The hex hole is about 0.06 mm off the centre line. That is very small, but we should still check the fit on the shaft. If the hole is tight, lightly sand the flats. Do not open it out so much that the shaft spins. The exact hex shaft size is still to confirm.

### Wiring

We do not have a full robot wiring diagram in this repository yet. These points come from our camera plan and from normal FTC practice:

- Plug the webcam into the Control Hub **USB 3.0 port** (the blue one). Official FTC docs warn that ESD on the USB 2.0 port can cause Wi-Fi disconnects. See [Configuring an External Webcam](https://ftc-docs.firstinspires.org/en/latest/hardware_and_software_configuration/configuring/configuring_external_webcam/configuring-external-webcam.html).
- Zip tie the camera cable to the frame every 10 to 15 cm, with a small loop of slack at the camera and at the hub, so a hit does not pull the plug.
- Keep the cable away from the launcher wheel and the intake.
- If you add a second camera, use a USB hub on the USB 3.0 port. A Logitech C920 may need a powered hub.
- On the Driver Hub, use **Configure Robot, Scan**. Give each motor, servo and webcam a clear name, and keep those names exactly the same in code.
- Do not force connectors. Check that the battery is locked in and that power cables cannot rub on wheels or belts.
- In hot and humid conditions, check batteries and wiring often. Heat can affect performance.

### The SDK

- Install **FTC SDK v12.0** (Android Studio) or use OnBot Java, then update the Control Hub and the Driver Hub.
- A good first check is the official sample `ConceptAprilTag`. Remove `@Disabled` so it shows in the OpMode list, then confirm it builds and appears on the Driver Hub.
- In SDK v12.0, `getDetections()` can return `AprilTagSingleDetection` or `AprilTagClusterDetection`. Check the type before you read fields. Old code that always reads `detection.id` will not compile.
- Our starter OpMode uses `VisionPortal` and `AprilTagProcessor`, at 640 x 480, with MJPEG, and with the official BIOBUZZ tag library. 640 x 480 has a built-in SDK calibration for the Logitech C920 and C270.
- Tune one number at a time, and write down what happened. Test on blocks with the wheels off the ground first.

### The Driver Hub

- Pick the configuration you saved, then pick the OpMode.
- Press **INIT** first, not START, when you want to look at the camera.
- Open the **3-dot menu**, choose **Camera Stream**, and tap the picture to refresh it. The Driver Hub camera preview is meant to be used **during INIT**. After START, many teams turn the preview off so the robot stays responsive. Our camera plan also says to turn off the preview during matches, because a live preview adds load.
- Wait until telemetry or the preview shows that the camera is actually running (for official samples, you should see a clear, steady image). If the camera never reaches a streaming state, the Driver Hub has nothing useful to show.
- Telemetry is the text on the Driver Hub. Our starter OpMode prints target name, range, bearing, aim state and launcher speed. Read it before you blame the hardware.
- If an OpMode does not appear in the list, check that the file is in TeamCode, that it has `@TeleOp` or `@Autonomous`, and that it is not `@Disabled`. Then rebuild and restart the Robot Controller.

---

## Common mistakes

### Using the FTC guides

- Starting to cut, print or assemble before reading the full guide.
- Following an old V2 step after the kit became V3 only (18 to 19 Nov 2026). There are no rubber bands, no zip-tie links, and both OP2 sheets are used.
- Treating the short BOM step list as the full assembly guide. Use the [27-page PDF](../FTC%20Kits/Shooter%20Upgrade%20Kit/V3%20Shooting%20Assembly%20Guide.pdf).
- Opening the 1-byte `FTC chassis options` file at the repo root, instead of the folder [`FTC Chassis options`](../FTC%20Chassis%20options).
- Putting [`FTC-camera(v1).py`](../FTC%20Camera/FTC-camera(v1).py) on the Control Hub. That file is a laptop tool.
- Treating CAD fit numbers, example launcher speeds, or untested tilt values as proven match settings.
- Copying a design without checking it on your own robot, parts, and field.

### Building the shooter

These points come from the [BOM and 3D printing Guide](../FTC%20Kits/Shooter%20Upgrade%20Kit/BOM%20%26%203D%20printing%20Guide.md) and the V3 assembly guide.

- Printing the older V2 rail guard by mistake. The kit uses [`FTC Shooter V3 Rail Guard.stl`](../FTC%20precise%20shooting%20mechanism/V3%20Shooter%203D%20files/FTC%20Shooter%20V3%20Rail%20Guard.stl).
- Printing the rail guard vertically, or with supports. Print it sideways, with no supports, at 100% infill.
- Leaving U-channels **316** and **317** at the wrong spacing. Set the gap to **exactly 88 mm**, measured at the bottom, middle and top. Loosen, slide, tighten, and measure again.
- Skipping the Plate 368 fix. The kit plate's right end reaches about 30 mm into the ball path. Print [`plate_368_cut_5x5.stl`](../FTC%20precise%20shooting%20mechanism/V3%20Shooter%203D%20files/plate_368_cut_5x5.stl), or cut 56 mm (7 hole rows) off the channel end of the kit plate. Keep the left edge against plate 367. After the fix, CAD shows 4 mm of clearance for POLLEN.
- Fitting only one OP2 sheet, or leaving both sheets straight. Fit **both** sheets, one on each side. The inner corner of each sheet slides about 40 mm into the V3 slot. The rest turns out **about 15 degrees**, like a funnel, onto the intake plate. A V-shaped gap stays open in the middle. Check the angle on the robot.
- Using rubber bands, or the old zip-tie links. Use **16 zip ties**, 2.5 mm wide (8 to the U-channels at holes 16 to 19, and 4 per sheet at V3 holes 1 to 4). Only 2.5 mm ties pass through the 4 mm holes. Pull every tie tight. The shooter must not move at all.
- Taping straight onto the V3 rail guard. Tape goes only over the zip ties, and also along the front edge of each sheet on the intake plate after gluing.
- Putting super glue in the wrong place. Use a few small drops (the guide suggests 4 drops per sheet, about 2 mm each, about 20 mm apart) on the front edge of each sheet where it meets the intake plate (floor plate 375). Do not glue the bent part, the slot, the zip ties, or the shooter. Hold 30 to 60 seconds, wait 10 minutes before taping, and allow about 24 hours for full strength.
- Tilting the intake plate without checking clearance. The CAD suggestion is to raise the back edge (shooter end) about 4 to 5 mm, about 3 degrees more slope, and to keep at least 5 mm under the shooter. Check this on your robot. Use washers under the back screws if the holes do not allow the tilt.
- Expecting NECTAR (91 mm) to feed through the channel. CAD says it is about 3 mm too wide. Plan for POLLEN unless your own tests say otherwise.
- Assuming the shooter is competition ready because it is bolted on. It has been built, but not shooting tested.

### Building the intake

These points come from the [intake printing guide](../FTC%20Intake%20mechanism%20Upgrade/Printing%20Guide.md) and [Intake Calculations](../FTC%20Intake%20mechanism%20Upgrade/Intake%20Calculations.md). Some intake details are still to confirm, and we mark those below.

- Printing the roller on its side. Print it **standing on one flat end**, 180 mm tall, so each layer is a circle and the hex hole is a clean vertical hole.
- Leaving the slicer at the 3MF default of 15% infill and 2 walls. Use **100% infill** and 3 or 4 walls.
- Printing without a brim, or printing two tall rollers at once, so the part tips or gets knocked over.
- Starting a print on a machine with less than 180 mm of Z height, or not checking the brim and lid clearance on an A1 mini.
- Pulling the part off the bed while it is still hot, which can bend or snap it.
- Forcing a hex shaft through a tight hole, or sanding the hex so wide that the shaft spins.
- Treating foam sizes as final. The handwritten paper adds the 30 mm roller and 20 mm of foam to get a 50 mm total. That would mean about 10 mm of foam thickness all the way around. We still need to confirm that reading, and **how the foam is fitted**, with Aarav. If your kit includes foam, check the finished outer size against POLLEN on the robot before you glue anything.
- Assuming the mounting is already documented. How the roller is mounted on the robot is still to confirm.

### Mecanum drive and code

These points are based on the [Mecanum Wheels Presentation](../FTC%20Chassis%20options/Mecanum%20Wheels%20Presentation.pdf) and on common FTC mecanum setup problems.

- Mounting the wheels so the rollers do not form an **X** when you look from above. Wrong orientation makes the robot veer or refuse to strafe. Check the presentation and your wheel markings before you tighten the hex hubs.
- Forgetting to **normalise wheel powers**. If any wheel command goes above 1, the motion direction changes. The presentation covers this.
- Mixing up **robot-centric** and **field-centric** drive. Robot-centric moves left relative to the robot. Field-centric moves left relative to the field, and it needs a working heading sensor (usually a IMU). Test both the way the presentation describes.
- Changing several code values at once, then not knowing which change helped or hurt. The presentation includes testing. Change one thing at a time.
- Expecting a mecanum robot to push as hard as a tank drive, or assuming strafe speed equals forward speed. Mecanum is strong for alignment and strafing. Tank drive is often simpler and better at pushing. Pick the chassis that matches your team, using the comparison in the main [README](../README.md).

### Camera

These points come from the [Camera Integration Plan](../FTC%20Camera/Camera%20Integration%20Plan.md), [`CameraAimTeleOp.java`](../FTC%20Camera/CameraAimTeleOp.java), and the [Camera buying Guide](../FTC%20Camera/Camera%20buying%20Guide.md).

- Looking for the Driver Hub camera feed after pressing START. The **Camera Stream is meant to be used during INIT**. Press INIT, wait for the camera, open the 3-dot menu, then Camera Stream, and tap the picture to refresh it.
- Asking the webcam for **1920 x 1080**, often with MJPEG. Many FTC webcams cannot open that stream. The camera light may still come on, but the Driver Hub has nothing to show. **Use 640 x 480.** That is what our starter OpMode uses, and it has a built-in SDK calibration for the Logitech C920 and C270.
- Using a webcam name in code that does not match the robot configuration. Our starter OpMode expects exactly `Webcam 1`. If you named the camera something else (for example a custom name), either rename it in Configure Robot or change `WEBCAM_NAME` in the code so both sides match, including spaces and capital letters.
- Plugging the webcam into the USB 2.0 port. Use the USB 3.0 (blue) port.
- Using a Logitech Brio 100 or a BigPassport Pro-Live N3 for range measurements without calibration. Those cameras are not on the SDK built-in calibration list, so distance can be wrong until you calibrate and set lens intrinsics. The C920 (best pick in our plan) and the C270 have built-in calibration at 640 x 480.
- Leaving `ALLOW_SINGLE_TAGS_FOR_BENCH_TEST` set to `true` in a match. Set it to `false` for matches.
- Leaving `RED_ALLIANCE` wrong, so the robot aims at the other alliance's CELL.
- Trusting `robotPose` from HIVE CELL tags for field position. The official docs, and our plan, say to use `range` and `bearing` instead, because CELLs tip.
- Using old SDK AprilTag code that reads `.id` on every detection. On SDK v12.0 you must check whether you have a single detection or a cluster detection.
- Mounting the camera flat, or not facing the same way the V3 shooter fires. The tags are on the underside of the CELL. Our plan suggests tilting up, starting around 20 to 30 degrees, and then checking on the robot. Height and tilt are still guesses until we test.
- Leaving the live preview on during matches, which can lag the robot. Use 640 x 480, MJPEG, and turn the preview off for matches.
- Using the example distance table in the Java file as a real shooting table. Those launcher speeds are examples only. Fill them in from real test shots.

### Printing

- Using low infill on kit parts. Use 100% for the V3 shooter parts and for the intake roller.
- Printing the shooter curve in a way that makes it rough (wrong orientation, or supports left on the curve).
- Printing the 0.2 mm OP2 sheet with a normal multi-layer profile, or with a bed that is not level, so the sheet fails or warps.
- Ignoring first-layer adhesion on the tall intake roller (no brim, dirty bed, or a fast first layer).
- Scaling the STL in the slicer. These files are already in millimetres. If you "scale to fit," the 88 mm shooter width and the 7 mm hex hole will be wrong.
- Using the V2 STL from [Older versions](../FTC%20precise%20shooting%20mechanism/V3%20Shooter%203D%20files/Older%20versions) when you meant to print V3.

### General team mistakes

- Ordering key parts late. Shipping to many places in India takes time. Keep spares of motors, servos and a battery.
- Skipping the engineering notebook. Judges value clear records from day one.
- Building more than you drive. Driver practice wins close matches.
- Testing only on the bench, never with real game elements or under match conditions.
- Changing the robot the night before a competition without time to test.
- Not labelling wires, or not bringing a toolkit, zip ties, tape and a charged battery to the venue.
- Keeping useful notes inside one team only. If something in these guides is wrong, please tell us so we can fix it.

---

## Troubleshooting

### Shooter and mechanical fit

| Symptom | Likely cause | Fix |
|---|---|---|
| V3 rail guard will not sit between the pillars, or it sits loose | U-channels 316 and 317 are not 88 mm apart at all heights | Measure at the bottom, middle and top. Loosen, slide to exactly 88 mm, tighten, and measure again |
| POLLEN hits something before the shooter | Kit plate 368 still sticks into the ball path (about 30 mm in CAD) | Print or cut the 5x5 plate 368, keep the left edge against plate 367, and check for about 4 mm of clearance |
| Balls fall off the sides of the intake, or miss the slot | One or both OP2 sheets are missing, straight, or not in the slot far enough | Fit both sheets, about 15 degrees out, inner corners about 40 mm into the slot, then zip-tie holes 1 to 4 and glue the front edges |
| Shooter shifts when you push it | Zip ties are loose, the wrong width, or too few | Use 16 ties, 2.5 mm wide, 4 per side into the U-channels at holes 16 to 19. Pull them tight. Do not use rubber bands |
| Sheet will not accept a zip tie | Ties wider than 2.5 mm, or a sheet hole not under a V3 hole | Use 2.5 mm ties. The sheet is on an 8 mm grid and turned, so move the sheet a little or use the nearest hole |
| Glue failed, or the sheet is stuck in the slot | Glue on the bent part, the slot, or the shooter | Glue only the front edge on the intake plate. Wait 10 minutes before taping, and about 24 hours for full strength |
| Intake plate rubs the shooter | Tilt too large, or not checked on the robot | The CAD suggestion is about 3 degrees (back edge up about 4 to 5 mm) and at least 5 mm of gap. Recheck on your robot |
| NECTAR will not go through | Channel is sized around the 71 mm POLLEN | CAD shows NECTAR about 3 mm too wide. Use POLLEN, or test carefully and do not force it |
| Shots look inconsistent (when you begin testing) | Rough printed curve, loose shooter, or untested tilt and power | Reprint the rail guard sideways at 100% infill, recheck the 88 mm gap and ties, then test with a charged battery. We do not have shooting test results yet |

### Intake roller

| Symptom | Likely cause | Fix |
|---|---|---|
| Roller tips during the print | No brim, dirty bed, two rollers at once, or high speed up the part | 5 to 8 mm brim, clean bed, one roller at a time, slower outer walls in the upper half |
| Print will not start, or hits the lid | Printer Z height is under 180 mm, or the brim was not included in the height check | Check Z height in the slicer. An A1 mini is exactly 180 mm, so this is tight |
| Roller feels weak or the hex rounds out | Infill left at 15%, or only 2 walls | Reprint at 100% infill with 3 or 4 walls |
| Hex shaft will not go through | Hole is tight, or there is debris | Check about 7.00 mm across flats at both ends. Lightly sand. Do not force it |
| Shaft spins in the roller | Hole sanded too large | Reprint the roller. Do not open the hex out past a firm fit |
| Foam diameter looks wrong | 20 mm foam figure not yet confirmed | Read [Intake Calculations](../FTC%20Intake%20mechanism%20Upgrade/Intake%20Calculations.md). Confirm the finished size on the robot against POLLEN before gluing |

### Camera, SDK and Driver Hub

| Symptom | Likely cause | Fix |
|---|---|---|
| Camera light is on, but there is no feed on the Driver Hub | Preview opened after START, or the stream never started | Press INIT (not START). Wait, then use the 3-dot menu, Camera Stream, and tap to refresh |
| Camera light is on, but the stream never starts | Resolution too high (for example 1920 x 1080 MJPEG) | Set the webcam to **640 x 480**. That is what [`CameraAimTeleOp.java`](../FTC%20Camera/CameraAimTeleOp.java) uses |
| OpMode crashes at INIT: webcam not found | Name or configuration does not match | In Configure Robot, Scan, name the camera exactly `Webcam 1` (or change `WEBCAM_NAME` to your exact name), and activate the config |
| Old AprilTag code does not compile | SDK v12.0 split detections into two types | Check `instanceof AprilTagSingleDetection` or `AprilTagClusterDetection` before reading `.id` or `.metadata`. See the [Camera Integration Plan](../FTC%20Camera/Camera%20Integration%20Plan.md) |
| Tags seen, but range is wrong | No calibration for this camera or resolution | Use a C920 or C270 at 640 x 480, or calibrate and call `setLensIntrinsics` |
| Tags lost while turning | Motion blur | Lower exposure, raise gain, or turn slower (`MAX_AUTO_TURN`). Official sample starting values in our code are 6 ms exposure and gain 250 (tune these) |
| Tags only found close up | Decimation too high, or camera tilted wrong | Try decimation 2 or 1. Tilt the camera up more, then check on the robot |
| Low frame rate, laggy robot | Too much resolution or preview load | 640 x 480, MJPEG, and turn off the preview during matches |
| Wi-Fi drops during matches | Camera on the USB 2.0 port, ESD | Move the webcam to the USB 3.0 port, and follow official FTC ESD advice |
| Robot shakes left and right when aiming | `TURN_GAIN` too high | Lower it, or widen `AIM_TOLERANCE_DEG` a little. Our starting values are guesses |
| Robot turns away from the target | Sign or motor direction flipped | Flip the sign of `rotate` in auto-aim, or check motor directions |
| Aims at the wrong CELL | Wrong alliance setting | Set `RED_ALLIANCE` before the match |
| C920 readings jump | Autofocus hunting | Lock focus with the SDK `FocusControl` |
| Python camera app will not run on the robot | It is laptop software | Use the Java plan and `CameraAimTeleOp.java` on the Control Hub. Keep the Python app for laptop practice |

### Mecanum drive

| Symptom | Likely cause | Fix |
|---|---|---|
| Robot will not strafe, or it curves when it should go sideways | Wheel rollers are not in an X, or one motor direction is reversed | Check wheel orientation against the [presentation](../FTC%20Chassis%20options/Mecanum%20Wheels%20Presentation.pdf), then check motor directions in code |
| Direction feels wrong at full stick, but better at half stick | Wheel powers not normalised | Normalise so the largest wheel power is 1, as the presentation shows |
| Field-centric drive drifts or goes the wrong way | IMU heading not initialised, or inverted | Recalibrate the IMU, set heading at the start of the match, and test as the presentation describes |
| Robot is hard to line up in front of the shooter | Using only tank turns to shift sideways | That is a reason teams use mecanum: you can strafe a little left or right without turning in a circle. See the presentation for the drive methods |

### Printing and first-layer problems

| Symptom | Likely cause | Fix |
|---|---|---|
| Shooter curve is rough or ridged | Printed upright, or supports marked the curve | Reprint sideways, 100% infill, no supports |
| 0.2 mm sheet fails or is the wrong thickness | Wrong layer height, or unlevel bed | One 0.2 mm layer, PETG, slow first layer, level bed |
| Tall intake roller comes off the bed | Weak first layer or no brim | 5 to 8 mm brim, clean bed or glue stick, slow first layer |
| Printed part is the wrong size | Slicer scaled the STL | Reset scale to 100%. Files are already in mm. Check 88 mm width on V3, 180 mm length and 7 mm hex on the roller |

---

## Ask a question

If this page and the guides do not answer your question, please ask us. We will add a form here when it is ready.

**Question form: (link coming soon)**

Until the form is up, you can:

- Open a [GitHub Issue](https://github.com/Aarav-111/FTC-India-Resources/issues) on this repository
- Email [prolabsrobotics@gmail.com](mailto:prolabsrobotics@gmail.com)

When you ask, please include:

- What you are trying to build
- What you have tried so far
- Photos or code snippets if possible
- Your SDK version, webcam name (as it appears in Configure Robot), and whether the problem happens during INIT or after START

Clear questions get faster and better answers.

---

## Links to files in this repository

| File or folder | Link |
|---|---|
| Main README | [README.md](../README.md) |
| FTC Kits (all kit files) | [FTC Kits](../FTC%20Kits) |
| Intake Assembly Guide (PDF) | [Intake Assembly Guide.pdf](../FTC%20Kits/Intake%20Upgrade%20Kit/Intake%20Assembly%20Guide.pdf) |
| Intake kit part (STL) | [FTC Intake Attachment.stl](../FTC%20Kits/Intake%20Upgrade%20Kit/FTC%20Intake%20Attachment.stl) |
| V3 Shooting Assembly Guide (PDF) | [V3 Shooting Assembly Guide.pdf](../FTC%20Kits/Shooter%20Upgrade%20Kit/V3%20Shooting%20Assembly%20Guide.pdf) |
| V3 BOM and 3D printing Guide | [BOM & 3D printing Guide.md](../FTC%20Kits/Shooter%20Upgrade%20Kit/BOM%20%26%203D%20printing%20Guide.md) |
| V3 print files | [V3 Shooter 3D files](../FTC%20precise%20shooting%20mechanism/V3%20Shooter%203D%20files) |
| Testing photos and walkaround video | [Testing videos and photos](../FTC%20precise%20shooting%20mechanism/V3%20Shooter%203D%20files/Testing%20videos%20and%20photos) |
| Shooter and intake theory PDF | [FTC Shooting and Intake Mechanism Theory.pdf](../FTC%20precise%20shooting%20mechanism/FTC%20Shooting%20and%20Intake%20Mechanism%20Theory.pdf) |
| Interactive shooter simulator | [ftc-shooter-interactive-guide.netlify.app](https://ftc-shooter-interactive-guide.netlify.app/) |
| Intake upgrade (start here) | [v1 by Aarav Jaisingh.md](../FTC%20Intake%20mechanism%20Upgrade/v1%20by%20Aarav%20Jaisingh.md) |
| Intake printing guide | [Printing Guide.md](../FTC%20Intake%20mechanism%20Upgrade/Printing%20Guide.md) |
| Intake calculations | [Intake Calculations.md](../FTC%20Intake%20mechanism%20Upgrade/Intake%20Calculations.md) |
| Camera buying guide | [Camera buying Guide.md](../FTC%20Camera/Camera%20buying%20Guide.md) |
| Camera integration plan (Java) | [Camera Integration Plan.md](../FTC%20Camera/Camera%20Integration%20Plan.md) |
| Starter OpMode | [CameraAimTeleOp.java](../FTC%20Camera/CameraAimTeleOp.java) |
| Laptop AprilTag app | [FTC-camera(v1).py](../FTC%20Camera/FTC-camera(v1).py) |
| Mecanum presentation (PDF) | [Mecanum Wheels Presentation.pdf](../FTC%20Chassis%20options/Mecanum%20Wheels%20Presentation.pdf) |
| Mecanum presentation (PowerPoint) | [Mecanum Wheels Presentation.pptx](../FTC%20Chassis%20options/Mecanum%20Wheels%20Presentation.pptx) |
| Mecanum presentation (Google Slides) | [Google Slides](https://docs.google.com/presentation/d/10t6m5lrtCYghSzNBLcLgv_6zWi-kxssT0vhTHXqJd7Y/edit) |
| FTC Docs by Aarav Jaisingh | [FTC Docs by Aarav Jaisingh](../FTC%20Docs%20by%20Aarav%20Jaisingh) |

Official docs we relied on for the camera sections are listed in the [Camera Integration Plan, section 12](../FTC%20Camera/Camera%20Integration%20Plan.md).
