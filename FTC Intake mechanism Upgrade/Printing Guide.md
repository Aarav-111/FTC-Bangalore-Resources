# Printing Guide: Intake Upgrade v1

This guide is for [`Intake Upgrade v1.stl`](./Intake%20Upgrade%20v1.stl) in this folder. We converted it from Aarav's 3MF file (opened in Bambu Studio, title `FTC_intake`). The 3MF has only one object, so this is a single STL, not a set of separate parts.

The notes below describe the shape of the part and how we recommend printing it. How the part is used on the robot is to confirm with Aarav.

## Previews

![Intake Upgrade v1, isometric view](./intake_v1_iso.png)

![End view, looking along the 180 mm length](./intake_v1_end.png)

## What we measured

We loaded the 3MF in millimetres, as the file itself specifies. The mesh is watertight, with consistent outward normals. We did not need to flip or repair the normals.

| Measurement | Value |
|---|---|
| Length | 180.00 mm |
| Outer width (X) | 29.97 mm |
| Outer height (Z) | 29.99 mm |
| Outer diameter (designed) | about 30 mm |
| Hex hole, across flats | 7.00 mm |
| Hex hole, side length | 4.04 mm |
| Hex hole length | through the full 180.00 mm |
| Volume (solid) | 119.27 cm3 |
| Triangles | 636 |
| Vertices | 318 |
| Watertight | Yes |

A small note: the hex hole is about 0.06 mm off the centre line of the cylinder. That is very small, but we should still check the fit on the shaft.

## Recommended orientation

Print the roller lying on its side, with the long 180 mm axis along the bed, and one flat of the hex hole facing up (parallel to the bed). This is how the part was already placed in the 3MF, and the STL in this folder is already sitting this way (the bottom is at z = 0).

Why we recommend this:

- A flat of the hex hole is on top, so the printer only has to bridge a short 4.04 mm flat. That is a small bridge, so we do not need supports inside the hole.
- Printing it standing on one end would also avoid supports (the hole would be vertical), but the part is 180 mm tall, which is the full height of a Bambu Lab A1 mini. That is a tight fit. The layers would also run across the roller, which is weaker if the shaft bends.

## Print settings

The 3MF was a Bambu Studio project for a Bambu Lab A1 mini, 0.4 mm nozzle, "0.20 mm Standard" profile, and a textured PEI plate. That profile had 15% infill and 2 walls, and supports were off. We should change the infill to 100% before we print. 100% infill (fully solid) is our standing rule for these kit parts.

| Setting | Our recommendation | Notes |
|---|---|---|
| Material | PETG or PLA | See the material section below |
| Layer height | 0.2 mm | Matches the 3MF |
| Walls | 3 or 4 | The 3MF had 2. Extra walls help the hex hole hold its shape |
| Infill | 100% (fully solid) | Please change this. The 3MF still has 15% |
| Infill pattern | gyroid or grid | At 100% the pattern matters less |
| Supports | None | The top of the hex hole is a short 4 mm bridge |
| Brim | None on a 180 mm bed. A small brim is fine on a larger bed | See the bed size warning |
| Bed | Textured PEI, if you have it | As in the 3MF |
| First layer | Slow, with a good squish | The part is long and skinny, so bed adhesion matters |
| Nozzle | 0.4 mm | As in the 3MF |

## Material and temperatures

The 3MF has both PLA and PETG profiles loaded, and it looks like the plate was set to print in PETG. Please confirm with Aarav which filament to use. The starting temperatures below come from the 3MF profiles. If your spool lists different values, use those.

| Material | Nozzle | Bed (textured PEI) | Why we might choose it |
|---|---|---|---|
| PETG | 245 C | 70 C | Tougher, and a bit more heat resistant. Better if the roller takes load or wear |
| PLA | 220 C | 65 C | Easier to print, and easier to get a clean first layer |

## Bed size warning

The part is 180.00 mm long. A Bambu Lab A1 mini bed is 180 x 180 mm, so the part uses the full length of that bed. In the 3MF it was already placed to span the bed from one edge to the other.

If we print on an A1 mini:

- Do not add a brim or a skirt. There is no extra room.
- Align the long axis with the bed, not at an angle.
- Check that the first layer does not get clipped at the ends.
- A larger printer (for example an A1, P1P or X1, with a 256 mm bed) is more comfortable.

## Filament use (estimated)

These numbers are from the solid mesh volume (119.27 cm3) at 100% infill. They do not include purge, prime, or a brim, so the real use will be a little higher.

| Material | Density used | Estimated mass |
|---|---|---|
| PLA | 1.24 g/cm3 | about 148 g |
| PETG | 1.27 g/cm3 | about 151 g |

## After printing: post-processing and fit check

1. Let the part cool on the bed before we remove it, so it does not bend.
2. Check the length with a ruler or calipers. We want 180 mm.
3. Check the outer diameter. We want about 30 mm.
4. Check the hex hole, across flats, at both ends. We want about 7.00 mm.
5. Test that the hex shaft (exact size to confirm with Aarav) slides through the full length without forcing it. If the hole is tight, we can lightly sand the flats. Do not open it out so much that the shaft spins.
6. Look down the hole to check it is straight.
7. If we add foam around the roller, the planned sizes are in [Intake Calculations](./Intake%20Calculations.md). How the foam is fitted is to confirm with Aarav.
8. Test the fit on the robot before we glue or pin anything. The mounting is to confirm with Aarav.

## To confirm with Aarav

- Which filament to use, PLA or PETG.
- The exact hex shaft size that should go through the 7 mm hole.
- How the roller is mounted on the robot, and how any foam is fitted.
- Whether the 0.06 mm hole offset causes a real fit problem.
