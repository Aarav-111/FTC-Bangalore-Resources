# Mecanum Chassis Guide

A simple, goBILDA style FTC chassis with 4 mecanum wheels, by Aarav J. (Prolabs Robotics), with R-Factor FRC.

- **[Mecanum Chassis Guide.pdf](./Mecanum%20Chassis%20Guide.pdf)**: the full guide, 15 pages, A4, black and white, print friendly
- [Mecanum Chassis Guide.html](./Mecanum%20Chassis%20Guide.html): editable source of the guide
- [Chassis guide source](./Chassis%20guide%20source): the Python scripts we used to make the pictures and the PDF

For how mecanum wheels move, with the maths, see the [Mecanum Wheels Presentation](./Mecanum%20Wheels%20Presentation.pdf) in this folder ([PowerPoint](./Mecanum%20Wheels%20Presentation.pptx), [Google Slides](https://docs.google.com/presentation/d/10t6m5lrtCYghSzNBLcLgv_6zWi-kxssT0vhTHXqJd7Y/edit)). For shooting from the chassis, see our [Shooter Trajectory Calculations](../FTC%20Docs%20by%20Aarav%20Jaisingh/Shooter%20Trajectory%20Calculations.md).

> We have not built and tested this exact chassis yet. The build is one good way to do it, based on goBILDA parts and gm0. Costs are approximate.

## The build

- **Frame:** 2 x goBILDA 1120 Series U-Channel, 384 mm (side rails) and 2 x 288 mm (cross channels). About 384 x 384 mm. Check it is square: both diagonals the same length.
- **Motors:** 4 x goBILDA 5203 Series Yellow Jacket, 19.2:1, 312 RPM, 8 mm REX shaft, direct drive, one per corner.
- **Wheels:** 1 x goBILDA GripForce Mecanum Wheel Set, 104 mm (4 wheels: 2 left, 2 right).
- **Bearings and spacers:** each wheel sits between the side rail and an outer plate. Spacers hold the plate, and a bearing in the plate supports the end of the shaft.
- **Balance:** Control Hub and battery low and near the centre.
- **3D printed parts:** none needed. Print any extras at 100% infill.

Theoretical top speed: pi x 104 mm x 312 RPM / 60 = about 1.70 m/s (about 5.57 ft/s, the same figure goBILDA lists for its Strafer kit).

## X pattern, not O

Look straight down on the robot. The top rollers of all four wheels must point towards the centre, making an **X**. Front left and back right are one kind of wheel, front right and back left are the other. If you see an **O**, two wheels are swapped: the robot still drives forward and turns, but it cannot strafe properly.

## Parts list (approximate costs)

| Part | Qty | goBILDA SKU | Approx. cost (USD) |
|---|---|---|---|
| U-Channel, 15 hole, 384 mm | 2 | 1120-0015-0384 | about 38 (18.99 each) |
| U-Channel, 11 hole, 288 mm | 2 | 1120-0011-0288 | about 30 (14.99 each) |
| Yellow Jacket motor, 312 RPM | 4 | 5203-2402-0019 | about 220 (54.99 each) |
| GripForce Mecanum Wheel Set, 104 mm | 1 set of 4 | 3625-0202-0104 | about 190 (189.99) |
| Motor mounts, hubs, bearings, spacers, plates, screws | as needed | various | about 60 to 100 (our estimate) |
| **Total** | | | **about 540 to 580** |
| Alternative: Strafer Chassis Kit, 104 mm GripForce | 1 | 3209-0001-0007 | about 700 (699.99) |

goBILDA list prices in US dollars, read in November 2026. **All costs are approximate.** Prices in India are usually higher (shipping, import duty, GST). Control Hub, battery and cables are not included.

## Wiring and configuration

| Motor | Control Hub motor port | Encoder port | Configuration name |
|---|---|---|---|
| Front left | 0 | 0 | `frontLeftMotor` |
| Back left | 1 | 1 | `backLeftMotor` |
| Front right | 2 | 2 | `frontRightMotor` |
| Back right | 3 | 3 | `backRightMotor` |
| Built-in IMU | inside the hub | | `imu` |

On the Driver Hub: 3 dots menu, Configure Robot, New, Control Hub Portal, Control Hub, Motors. Pick the motor type **goBILDA 5202/3/4 series** and type the names exactly (they are case sensitive). Save and activate.

## Motor directions

Most FTC motors spin counterclockwise (seen from the shaft end) with positive power, so one side must be reversed. Like the gm0 sample, we start by reversing the right side. If the robot drives backward, reverse the left side instead. Test each wheel on its own with the robot on a box before driving.

## Drive code

The guide has the full Java OpModes, adapted from gm0:

- **Robot-centric:** `y = -left_stick_y`, `x = left_stick_x * 1.1`, `rx = right_stick_x`. Front left = y + x + rx, back left = y - x + rx, front right = y - x - rx, back right = y + x - rx.
- **1.1 strafe factor:** counteracts the slower strafing of mecanum wheels. Try 1.0 to 1.2.
- **Normalising:** divide all four powers by `max(|y| + |x| + |rx|, 1)` so the ratio is kept when a power goes over 1.
- **Field-centric:** rotate (x, y) by minus the IMU heading before the same maths. OPTIONS resets the heading.

## First drive test

Each wheel forward on its own, X pattern checked, then forward, back, strafe left and right, diagonals, turn both ways, a full speed straight run, and a screw check after 5 minutes. The full checklist is on page 13 of the PDF.

## Troubleshooting

| Problem | What to check |
|---|---|
| Drifts or turns when strafing | X pattern, motor directions, weight balance, all 4 wheels touching the mat, strafe factor |
| A wheel spins the wrong way | Reverse that motor in code, or check its port and name |
| Wobble at speed | Loose hub or set screw, bent shaft, damaged roller, outer bearing missing or out of line |
| Weight balance | Move the battery and hub to the centre, low down |
| Code crashes on INIT | Names in code and configuration do not match |

## Sources

- gm0, Mecanum TeleOp: https://gm0.org/en/latest/docs/software/tutorials/mecanum-drive.html
- gm0, Holonomic drivetrains: https://gm0.org/en/latest/docs/robot-design/drivetrains/holonomic.html
- FTC Docs, Creating a Configuration: https://ftc-docs.firstinspires.org/en/latest/hardware_and_software_configuration/configuring/getting_started/getting-started.html
- FTC Docs, IMU interface: https://ftc-docs.firstinspires.org/en/latest/programming_resources/imu/imu.html
- goBILDA GripForce Mecanum Wheel Set, 104 mm: https://www.gobilda.com/gripforce-mecanum-wheel-set-o104mm-40a-durometer-rollers/
- goBILDA Yellow Jacket, 312 RPM: https://www.gobilda.com/5203-series-yellow-jacket-planetary-gear-motor-19-2-1-ratio-24mm-length-8mm-rex-shaft-312-rpm-3-3-5v-encoder/
- goBILDA U-Channel, 384 mm: https://www.gobilda.com/1120-series-u-channel-15-hole-384mm-length/
- goBILDA U-Channel, 288 mm: https://www.gobilda.com/1120-series-u-channel-11-hole-288mm-length/
- goBILDA Strafer Chassis Kit: https://www.gobilda.com/strafer-chassis-kit-104mm-gripforce-mecanum-wheels/
- goBILDA bearings, hubs, spacers, motor mounts: https://www.gobilda.com/bearings/ , https://www.gobilda.com/hubs/ , https://www.gobilda.com/spacers/ , https://www.gobilda.com/motor-mounts/
- REV Control Hub getting started: https://docs.revrobotics.com/duo-control/control-hub-gs
