# Intake Calculations

This page types up the handwritten calculation paper in [Intake calculations (handwritten).jpg](./Images/Intake%20calculations%20%28handwritten%29.jpg). We walk through the math step by step. A few readings still need a check: those are marked **to confirm with Aarav**.

The printed part in this folder matches the hexagon and the 30 mm roller described here. See the [Printing Guide](./Printing%20Guide.md) for the measured sizes.

## 1. A regular hexagon ABCDEF

The paper starts with a regular hexagon, labelled ABCDEF.

In a regular hexagon:

- all 6 sides are the same length
- all 6 interior angles are the same

The interior angle of a regular hexagon is 120 degrees, so angle A = 120 degrees.

Why 120 degrees? The rule for the interior angle of a regular polygon is:

((n - 2) times 180) / n

For a hexagon, n = 6:

((6 - 2) times 180) / 6 = (4 times 180) / 6 = 720 / 6 = 120 degrees

## 2. The 30-30-120 triangle (side view, with feet)

The paper shows a triangle with angles 30 degrees, 30 degrees and 120 degrees, and a base of 7. The two equal sides are 7 / root 3, which is about 4.04. This is labelled as a side view, with feet.

Here is that triangle, step by step.

The 120 degree angle is the interior angle of the hexagon (angle A). The triangle is isosceles, so the two base angles are equal. A triangle adds up to 180 degrees, so each base angle is:

(180 - 120) / 2 = 60 / 2 = 30 degrees

That is why the angles are 30, 30 and 120.

The base of this triangle (the side opposite the 120 degree angle) is 7. This 7 mm is the width of the hexagon across the flats (from one flat side to the opposite flat side). That matches the hexagonal hole in the printed part, which we measured at 7.00 mm across the flats.

Now we find the two equal sides, which we will call x. We use the law of sines:

a / sin(A) = b / sin(B)

So:

7 / sin(120 degrees) = x / sin(30 degrees)

We need two sine values:

- sin(30 degrees) = 1/2
- sin(120 degrees) = sin(60 degrees) = root 3 / 2

Swap to solve for x:

x = 7 times sin(30 degrees) / sin(120 degrees)
  = 7 times (1/2) / (root 3 / 2)
  = 7 / root 3

7 / root 3 is about 4.041, which the paper rounds to 4.04.

If we want to rationalise the denominator:

7 / root 3 = (7 x root 3) / 3, which is the same number, about 4.041

These 4.04 mm lengths are the side lengths of the hexagon. In a regular hexagon the side length is also the distance from the centre to a vertex.

We can check this another way. For a regular hexagon:

width across the flats = root 3 x side length

If the side is 7 / root 3:

root 3 x (7 / root 3) = 7 mm

This matches the base of 7 mm, and it matches the 7.00 mm hex hole in the STL.

## 3. The stock wheel and our wheel

The paper then compares the stock wheel with our wheel.

| Item | What the paper shows |
|---|---|
| Stock wheel diameter | 48 mm |
| Our roller diameter | 30 mm (the paper notes "ours = 30 mm") |
| Stock wheel, 69 mm from the ground | See the question below |
| Our roller plus foam | 30 mm + 20 mm foam, for 50 mm total |

The 30 mm figure matches the printed roller, which measures about 29.97 mm by 29.99 mm (designed as 30 mm).

### To confirm with Aarav: what is the 69 mm?

The paper shows the 48 mm stock wheel at 69 mm from the ground. It is not yet clear whether 69 mm is measured to the centre of the wheel, or to the lowest point of the wheel.

A useful check: in the goBILDA StarterBot CAD, the lowest point of the 48 mm Gecko wheel is 69 mm above the ground. If the paper is using that same 69 mm as the lowest point, then the centre of the stock wheel would be:

69 + (48 / 2) = 69 + 24 = 93 mm above the ground

If 69 mm is instead the centre, the lowest point would be:

69 - 24 = 45 mm above the ground

We should confirm which one the paper means before we use 69 mm to set our roller height.

### To confirm with Aarav: does the 20 mm foam make a 50 mm outer diameter?

The paper adds the 30 mm roller and 20 mm of foam to get 50 mm total. 30 + 20 = 50 would mean the foam adds 20 mm to the diameter, which is about 10 mm of foam thickness all the way around the roller. We should confirm that this is what was intended, and how the foam is fitted.

If we later confirm both of those readings, we can compare the two wheels more carefully. We have not assumed those answers here.
