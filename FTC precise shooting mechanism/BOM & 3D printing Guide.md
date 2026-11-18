# V3 Shooter: BOM and 3D Printing Guide

**V3 Rail Guard + Prolabs Flex Sheet**, by Aarav Jaisingh, Prolabs Robotics. For the goBILDA FTC StarterBot 2026-27 (BIOBUZZ).

> **NOT ROBOT TESTED.** Everything here is checked in CAD only. Updated 18 Nov 2026 (very big change): the kit is now **V3 only** (V2 is an older version, not in the kit), folders and guide renamed to V3, no rubber bands (zip ties only, 24 per robot), super glue fixes the sheet front edge to the intake plate, intake plate tilted up a little, U-channels 316 and 317 set to exactly 88mm. Earlier 18 Nov 2026: V3 rail guard added (test both V2 and V3, use the one that shoots best), 20 zip ties per robot, tape only over the zip ties. 15 Nov 2026: only the 3 print files kept, simulator removed. 13 Nov 2026: plate 368 fix, V2 mounting, corrected V2 hole positions, fit check.

## What to print (3 files)

| # | File | Part | Size | Qty |
|---|---|---|---|---|
| 1 | `FTC Shooter V3 Rail Guard.stl` | V3 rail guard (main shooter): V2 shape + about 58mm straight top at about 55 deg | about 217 x 88 x 116mm | 1 |
| 2 | `prolabs_plain_sheet_0p2.stl` | Prolabs Flex Sheet | 88 x 104 x 0.2mm | 1 |
| 3 | `plate_368_cut_5x5.stl` | Plate 368 replacement | 40 x 40 x 1.5mm | 1 |
| old | `Older versions/FTC Shooter V2 Rail Guard.stl` | V2 rail guard: **older version, not in the kit** | about 181 x 88 x 71mm | 0 |

All at **100% infill**. V3 is the main shooter. It uses the same gap, slot and holes as the older V2.

**One kit contains:** 1 V3 rail guard (main shooter), 2 Plate 368 (1 used, 1 spare), 2 Prolabs OP2 (Flex) sheets (1 used, 1 spare), 1 roll of electrical tape, zip ties and 1 small bottle of super glue. No rubber bands. No V2.

## Bill of Materials

| # | Part | Qty | File / notes |
|---|------|-----|------|
| a | 3D printed V3 shooter rail guard by Aarav Jaisingh, Prolabs Robotics (100% infill) | 1 | `FTC Shooter V3 Rail Guard.stl` |
| b | 3D printed Prolabs Flex Sheet: 88 x 104 x 0.2mm, 143 holes (11 x 13, Ø4mm, 8mm grid) | 1 (+1 spare in the kit) | `prolabs_plain_sheet_0p2.stl` |
| c | **Plate 368 replacement**: 40 x 40 x 1.5mm, 25 holes (5 x 5, Ø4mm, 8mm grid, 4mm edge) | 1 (+1 spare in the kit) | `plate_368_cut_5x5.stl`, or cut the kit plate (see below) |
| d | Zip ties, **2.5mm wide** (only 2.5mm ties pass through the 4mm holes) | 24 | 8 to tie the shooter to the U-channels, 4 to tie the sheet in the slot, 12 for the 4 sheet links (3 each). Pull every tie tight. **No rubber bands** |
| e2 | Electrical tape, 18mm | 1 roll | Only over the zip ties, never straight onto V3 |
| f | Super glue, small bottle (in the kit) | 1 | A few small drops to fix the sheet front edge to the intake plate (floor plate 375). Not on the bent part, the slot, the zip ties or the shooter |


### How they connect (2 zip tie links per side, 4 in total)

Sheet hole -> zip tie loop -> joining zip tie -> zip tie loop -> rail guard hole (holes 1 and 2)

No rubber bands. Each link is 3 zip ties, about 46 to 48mm loop to loop. The joining tie goes about 110mm around, so use a long enough tie. Pull it snug, not so tight that the sheet lifts off the intake plate.

Rail guard hole positions under the slot (same on V3 and the older V2): **y -32.5, -25.4, -18.3, -11.3, -4.2** (7.08mm pitch). The sheet is on an 8mm grid, so the holes are 0.1 to 2.7mm off. All 5 work with 2.5mm zip ties.

## Plate 368 fix (needed)

Kit plate 368 is the **back wall of the left servo box**, between plates 367 (left) and 369 (right), under U-channel 332. Its right end reaches about 30mm into the ball path.

| Option | What to do |
|---|---|
| **A. Print (recommended)** | Print `plate_368_cut_5x5.stl`: 100% infill, flat on the bed |
| B. Cut the kit plate | Cut **56mm (7 hole rows)** off the channel end. Keep the end at plate 367 |

Keep the **left edge against plate 367**. The POLLEN ball then has **4mm of clearance**.

## Downloads

| File | Link |
|---|---|
| All 3D files (folder) | [V3 Shooter 3D files](./V3%20Shooter%203D%20files) |
| V3 rail guard (main) | [FTC Shooter V3 Rail Guard.stl](./V3%20Shooter%203D%20files/FTC%20Shooter%20V3%20Rail%20Guard.stl) |
| Flex Sheet | [prolabs_plain_sheet_0p2.stl](./V3%20Shooter%203D%20files/prolabs_plain_sheet_0p2.stl) |
| Plate 368 (5x5) | [plate_368_cut_5x5.stl](./V3%20Shooter%203D%20files/plate_368_cut_5x5.stl) |
| V2 rail guard (older version, not in the kit) | [FTC Shooter V2 Rail Guard.stl](./V3%20Shooter%203D%20files/Older%20versions/FTC%20Shooter%20V2%20Rail%20Guard.stl) |
| Testing videos and photos | [Testing videos and photos](./V3%20Shooter%203D%20files/Testing%20videos%20and%20photos) (coming soon) |

## Assembly

Interactive 3D simulator (compares V3 with the older V2): [ftc-shooter-interactive-guide.netlify.app](https://ftc-shooter-interactive-guide.netlify.app/)

Main assembly guide (V3, 26 pages, 15 steps): [V3 Shooting Assembly Guide](./V3%20Shooting%20Assembly%20Guide.pdf). Older detailed guide (V2): [V2 flexplate build guide](./V2_flexplate_build_guide.pdf)

Quick steps (the main guide is the full, updated version):
1. Print V3, the Flex Sheet and plate 368 (settings below), all at 100% infill.
2. Remove hood E (part 374).
3. Set the gap between U-channels 316 and 317 (the pillars beside the shooter) to **exactly 88mm**. Measure at the bottom, middle and top with a ruler. Loosen their screws, slide them sideways, tighten and measure again.
4. Replace kit plate 368 with the 5x5 plate (or cut 7 hole rows off). Keep the left edge against 367.
5. Tilt the intake plate (floor plate 375) up a little: raise the back edge (shooter end) about 4 to 5mm, about 3 deg more slope. Keep the front edge down. This is a CAD suggestion, check it on your robot and keep at least 5mm under the shooter. Use washers under the back screws if the holes don't allow it.
6. Fit V3 in the 88mm gap and zip-tie it to the U-channels: 4 ties per side, holes 16 to 19. It must not move at all.
7. Bend the sheet by hand and slide one end fully (40mm) into the slot. Rest the free end on the intake plate.
8. Zip-tie the sheet in the slot: holes 3 and 4, both sides.
9. Fit 2 zip tie links per side (holes 1 and 2). No rubber bands.
10. Glue the sheet front edge to the intake plate: 4 small drops (about 2mm each, about 20mm apart) along the edge, after the zip ties. Hold 30 to 60 seconds, wait 10 minutes before taping, full strength in about 24 hours.
11. Tape the sheet front edge onto the intake plate, then wrap tape over every zip tie. Never tape straight onto V3.

## Fit check (1 to 3mm tolerance allowed)

V3 has the same front, slot, width and holes as the older V2, so these CAD checks apply to V3.

| Item | Off by | Result |
|---|---|---|
| V3 width vs 88mm gap (channels 316 and 317) | 0 to 0.3mm | Pass |
| Standoff 378 into V3 / into ball path | 1.7mm / 1.6mm | Pass |
| Sheet width vs V3 slot | 0mm | Pass |
| POLLEN ball (71mm) in channel | 8.5mm room per side | Pass |
| Sheet in 1.7mm slot | 1.5mm loose | Pass |
| Step into V3 at slot | 2.5mm | Pass |
| Sheet length on slope | 1 to 2.5mm short | Pass (sheet flexes) |
| Sheet holes vs V3 holes | 0.1 to 2.7mm | Pass with 2.5mm ties |
| V3 mounting with zip ties | covers the 3 to 38mm hole offset | Pass |
| Plate 368 after the fix | 4mm clear of the ball | Pass |
| V3 top vs brackets 393/394 | about 3mm | **Check on robot** |
| Shooter height above hood E | 2 to 22mm | **Check on robot** |
| Zip tie link length | 46 to 48mm loop to loop | **Check on robot** |
| U-channel gap 316 to 317 | must be 88mm at all heights | **Set with a ruler** |
| Intake plate tilt | +3 deg suggested (back edge up 4 to 5mm, about 7.7mm left under the shooter in CAD) | **Check on robot** |
| Floor tilt (CAD) | about 6 deg, 8.6mm side to side | **Check on robot** |
| Intake roller to floor gap | 19.5mm | **Check on robot** |
| NECTAR ball (91mm) | 3mm too wide | **Borderline: POLLEN only** |

## 3D Printing

| Setting | V3 rail guard | Flex Sheet | Plate 368 |
|---|---|---|---|
| Material | PETG or PLA+ | PETG | PETG or PLA+ |
| Infill | **100%** | **100%** | **100%** |
| Orientation | **Sideways** | **Flat on the bed** | **Flat on the bed** |
| Supports | **None** | **None** | **None** |
| Layers | Normal | **One 0.2mm layer** | 0.2mm (1.5mm thick) |
| Adhesion | 5mm brim | Level bed, slow first layer | Normal |
| Size check | 217 x 88 x 116mm | 88 x 104 x 0.2mm | 40 x 40 x 1.5mm |

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
