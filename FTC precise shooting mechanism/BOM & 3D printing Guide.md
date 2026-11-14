# Shooter: BOM and 3D Printing Guide

**V2 Rail Guard + Prolabs Flex Sheet**, by Aarav Jaisingh, Prolabs Robotics. For the goBILDA FTC StarterBot 2026-27 (BIOBUZZ).

> **NOT ROBOT TESTED.** Everything here is checked in CAD only. Updated 13 Nov 2026: plate 368 fix, V2 mounting, corrected V2 hole positions, fit check.

## Bill of Materials

| # | Part | Qty | File / notes |
|---|------|-----|------|
| a | 3D printed shooter rail guard (V2) by Aarav Jaisingh, Prolabs Robotics (100% infill) | 1 | `FTC Shooter V2 Rail Guard.stl` |
| b | 3D printed Prolabs Flex Sheet: 88 x 104 x 0.2mm, 143 holes (11 x 13, Ø4mm, 8mm grid) | 1 | `prolabs_plain_sheet_0p2.stl` |
| c | **Plate 368 replacement**: 40 x 40 x 1.5mm, 25 holes (5 x 5, Ø4mm, 8mm grid, 4mm edge) | 1 | `plate_368_cut_5x5.stl`, or cut the kit plate (see below) |
| d | Zip ties, **2.5mm wide** (only 2.5mm ties pass through the 4mm holes) | 12 | 8 for the 4 sheet chains + at least 4 to mount V2 (2 per side) |
| e | Rubber bands (all the same size) | 6 | 4 for the sheet chains + 2 to mount V2 (1 per side) |
| f | Super glue, thin CA (+ CA primer for PETG) | 1 | Zip tie locks only. Optional |

Optional: `plate_368_5x6_trim.stl` (40 x 48mm, 1 extra row added downward, trim to fit). STEP files for both plates are in the same folder.

### How they connect (2 chains per side, 4 in total)

Sheet hole -> zip tie loop -> rubber band -> zip tie loop -> rail guard hole

V2 rail guard hole positions under the slot (corrected): **y -32.5, -25.4, -18.3, -11.3, -4.2** (7.08mm pitch). The sheet is on an 8mm grid, so the holes are 0.1 to 2.7mm off. All 5 work with 2.5mm zip ties.

## Plate 368 fix (needed)

Kit plate 368 is the **back wall of the left servo box**, between plates 367 (left) and 369 (right), under U-channel 332. Its right end reaches about 30mm into the ball path.

| Option | What to do |
|---|---|
| **A. Print (recommended)** | Print `plate_368_cut_5x5.stl`: 100% infill, flat on the bed |
| B. Cut the kit plate | Cut **56mm (7 hole rows)** off the channel end. Keep the end at plate 367 |
| C. 5x6 trim version | Print `plate_368_5x6_trim.stl` and trim the extra row |

Keep the **left edge against plate 367**. The POLLEN ball then has **4mm of clearance**.

## Downloads

| File | Link |
|---|---|
| All 3D files (folder) | [V2 Shooter 3D files](https://github.com/Aarav-111/FTC-Bangalore-Resources/tree/main/FTC%20precise%20shooting%20mechanism/V2%20Shooter%203D%20files) |
| V2 rail guard | [FTC Shooter V2 Rail Guard.stl](https://github.com/Aarav-111/FTC-Bangalore-Resources/raw/main/FTC%20precise%20shooting%20mechanism/V2%20Shooter%203D%20files/FTC%20Shooter%20V2%20Rail%20Guard.stl) |
| Flex Sheet | [prolabs_plain_sheet_0p2.stl](https://github.com/Aarav-111/FTC-Bangalore-Resources/raw/main/FTC%20precise%20shooting%20mechanism/V2%20Shooter%203D%20files/prolabs_plain_sheet_0p2.stl) |
| Plate 368 (5x5) | [plate_368_cut_5x5.stl](https://github.com/Aarav-111/FTC-Bangalore-Resources/raw/main/FTC%20precise%20shooting%20mechanism/V2%20Shooter%203D%20files/plate_368_cut_5x5.stl) / [STEP](https://github.com/Aarav-111/FTC-Bangalore-Resources/raw/main/FTC%20precise%20shooting%20mechanism/V2%20Shooter%203D%20files/plate_368_cut_5x5.step) |
| Plate 368 (5x6 trim) | [plate_368_5x6_trim.stl](https://github.com/Aarav-111/FTC-Bangalore-Resources/raw/main/FTC%20precise%20shooting%20mechanism/V2%20Shooter%203D%20files/plate_368_5x6_trim.stl) / [STEP](https://github.com/Aarav-111/FTC-Bangalore-Resources/raw/main/FTC%20precise%20shooting%20mechanism/V2%20Shooter%203D%20files/plate_368_5x6_trim.step) |
| 3D simulator (download, open in Chrome or Safari) | [V2_shooter_simulator.html](https://github.com/Aarav-111/FTC-Bangalore-Resources/raw/main/FTC%20precise%20shooting%20mechanism/V2%20Shooter%203D%20files/V2_shooter_simulator.html) |

## Assembly

A step-by-step visual guide with 3D views is available: [Instruction Guide](https://github.com/Aarav-111/FTC-Bangalore-Resources/blob/main/FTC%20precise%20shooting%20mechanism/V2_flexplate_build_guide.pdf)

Quick steps:
1. Print the V2 rail guard, the Flex Sheet and plate 368 (settings below).
2. Replace kit plate 368 with the 5x5 plate (or cut 7 hole rows off). Keep the left edge against 367.
3. Mount V2 on hood E with rubber bands and zip ties, **at least 2 ties per side**. It must not move up or down when the ball hits it.
4. Bend the sheet by hand to fit the gap between V2 and the floor plate.
5. Slide one end of the sheet fully (40mm) into the slot on the front of V2.
6. Fit 2 rubber band chains on each side: sheet hole, zip tie loop, rubber band, zip tie loop, rail guard hole.
7. Keep the zip tie loops loose so the bands can stretch. Trim the zip tie tails so they don't touch the ball.
8. Optional: a drop of super glue on each zip tie lock. Do not glue the bends or the bands.
9. Rest the other end of the sheet on the floor plate.
10. Roll a ball by hand along the full path before driving.

## Fit check (1 to 3mm tolerance allowed)

| Item | Off by | Result |
|---|---|---|
| V2 width vs 88mm gap (channels 316 and 317) | 0 to 0.3mm | Pass |
| Standoff 378 into V2 / into ball path | 1.7mm / 1.6mm | Pass |
| Sheet width vs V2 slot | 0mm | Pass |
| POLLEN ball (71mm) in channel | 8.5mm room per side | Pass |
| Sheet in 1.7mm slot | 1.5mm loose | Pass |
| Step into V2 at slot | 2.5mm | Pass |
| Sheet length on slope | 1 to 2.5mm short | Pass (sheet flexes) |
| Sheet holes vs V2 holes | 0.1 to 2.7mm | Pass with 2.5mm ties |
| V2 mounting with bands and ties | covers the 3 to 38mm hole offset | Pass |
| Plate 368 after the fix | 4mm clear of the ball | Pass |
| V2 height above hood E | 2 to 22mm | **Check on robot** |
| Band stretch | 42 to 49mm span | **Check on robot** |
| Floor tilt (CAD) | about 6 deg, 8.6mm side to side | **Check on robot** |
| Intake roller to floor gap | 19.5mm | **Check on robot** |
| NECTAR ball (91mm) | 3mm too wide | **Borderline: POLLEN only** |

## 3D Printing

| Setting | V2 rail guard | Flex Sheet | Plate 368 |
|---|---|---|---|
| Material | PETG or PLA+ | PETG | PETG or PLA+ |
| Infill | **100%** | **100%** | **100%** |
| Orientation | **Sideways** | **Flat on the bed** | **Flat on the bed** |
| Supports | **None** | **None** | **None** |
| Layers | Normal | **One 0.2mm layer** | 0.2mm (1.5mm thick) |
| Adhesion | 5mm brim | Level bed, slow first layer | Normal |
| Size check | 129 x 149 x 88mm | 88 x 104 x 0.2mm | 40 x 40 x 1.5mm |

### Orientation

Print the rail guard sideways. Do not print it vertically or in its current orientation.

Why: printing sideways keeps the main shooter curve smooth. A rough curve will cause shooting problems.

### Supports

Do not use any supports for any part.

### Infill

Use 100% infill for all parts.

## Note

This design has not been tested on a robot yet. The 0.2mm sheet is very thin and can sag under the ball. Only the 71mm POLLEN ball fits the channel. Please check the fit by hand before competition use and share feedback with us.

## Contact

For more info, contact Prolabs Robotics, the team behind this design.

- Email: ProlabsRobotics@gmail.com
- Founder email: aaravjaisingh@gmail.com
- Phone: +91 90364 49179
