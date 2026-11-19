<p align="center">
  <img src="assets/banner.svg" alt="FTC Bangalore Resources banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/FTC-2027%20Challenge-orange" alt="FTC 2027 Challenge">
  <img src="https://img.shields.io/badge/Made%20in-India-green" alt="Made in India">
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="MIT License">
  <img src="https://img.shields.io/badge/Language-Python-yellow" alt="Python">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen" alt="Contributions Welcome">
</p>

# FTC Bangalore Resources

Welcome to **FTC-Bangalore-Resources**, an open collection of custom-built materials for the **FTC 2027 Challenge** (released in 2026).

This repository was started in Bangalore, but it is not just for Bangalore. It is for every FTC team in **India**. Whether you are a rookie team building your first robot or a veteran team chasing a spot at the next level, you will find something useful here.

---

## Very big change (18 to 19 Nov 2026)

The shooter upgrade kit is now **V3**, and both OP2 sheets are now fitted (one on each side). Here is what changed:

| Change | Details |
|---|---|
| V2 renamed to V3 | The kit, folder and guide are now called V3: `V3 Shooter 3D files` and `V3 Shooting Assembly Guide` |
| Kit is V3 only | The kit has 1 V3 main shooter, 2 Plate 368 (1 used, 1 spare), 2 Prolabs OP2 sheets (both used), electrical tape, zip ties and a small bottle of super glue. V2 is an older version, not in the kit |
| Both OP2 sheets fitted (19 Nov) | One sheet on each side of the shooter intake. The inner corner of each sheet goes into the V3 slot and the rest turns out about 15 degrees, like a funnel, onto the intake plate. 4 zip ties per sheet at V3 holes 1 to 4. The old zip tie links are gone |
| New assembly guide | [V3 Shooting Assembly Guide](./FTC%20precise%20shooting%20mechanism/V3%20Shooting%20Assembly%20Guide.pdf): 27 pages, 15 steps, 3D pictures for every step and 5 real photos |
| Zip ties only | No rubber bands. 16 zip ties per robot. Tape goes only over the zip ties |
| Super glue step | A few small drops fix the front edge of each sheet to the intake plate |
| 88mm channel gap step | Set U-channels 316 and 317 to exactly 88mm apart, measured at 3 heights |
| Intake plate tilt step | Raise the back of the intake plate a little (about 3 degrees, check on your robot) |
| Interactive simulator | [ftc-shooter-interactive-guide.netlify.app](https://ftc-shooter-interactive-guide.netlify.app/) (compares V3 with the older V2) |
| Testing videos and photos | New folder [Testing videos and photos](./FTC%20precise%20shooting%20mechanism/V3%20Shooter%203D%20files/Testing%20videos%20and%20photos), with 5 photos of the finished V3 shooter and a short walkaround video. Shooting test videos will be added later |

---

## Table of Contents

1. [Why This Repository Exists](#why-this-repository-exists)
2. [What You Will Find](#what-you-will-find)
3. [How to Navigate This Repository](#how-to-navigate-this-repository)
4. [Getting Started](#getting-started)
5. [Resource Details](#resource-details)
6. [Strategy Guide Overview](#strategy-guide-overview)
7. [Tips for Indian FTC Teams](#tips-for-indian-ftc-teams)
8. [Help Forum](#help-forum)
9. [Contributing](#contributing)
10. [Roadmap](#roadmap)
11. [Credits](#credits)
12. [Contact](#contact)
13. [License](#license)

---

## Why This Repository Exists

Many FTC teams in India start the season with the same problem. The game is released, the clock starts ticking, and every team spends weeks solving the same basic questions. Which chassis should we use? How do we make a shooter that hits the same spot every time? How do we use AprilTags to know where the robot is on the field?

Good answers to these questions exist, but they are often spread across forums, videos, and private team notes. New teams, especially those without an experienced mentor, lose a lot of time.

This repository puts tested designs, code, and strategy notes in one place. The goal is simple: help Indian teams spend less time reinventing the basics and more time building smart, competitive robots.

---

## What You Will Find

| Resource | What It Gives You |
|---|---|
| Chassis Designs | Proven chassis options to start your robot build |
| Precise Shooter Mechanism | A highly accurate shooter design with documentation |
| Shooting and Intake Guide | Strategy notes on how to design and build both systems |
| FTC Camera Code | Vision code with AprilTag support for precise positioning |
| Camera Buying Guide | Webcam comparison for AprilTag detection, with India prices |
| Shooter BOM and 3D Files | Bill of materials, print settings, and the 3 V3 print files |
| V3 Shooting Assembly Guide | Main assembly guide for the V3 shooter upgrade kit (PDF) |
| Intake mechanism Upgrade (v1) | v1 roller STL, printing guide, and intake calculations |
| Help Forum | A place to ask questions and get support |

---

## How to Navigate This Repository

```
FTC-Bangalore-Resources/
├── assets/
│ └── banner.svg # Images used in this README
├── FTC Camera/
│ ├── FTC-camera(v1).py # Camera + AprilTag positioning code
│ └── Camera buying Guide.md # Webcam buying guide for AprilTags
├── FTC Docs by Aarav Jaisingh/
│ └── FTC_Shooting_and_Intake_Mechanism.pdf # Strategy guide for shooter and intake
├── FTC precise shooting mechanism/
│ ├── BOM & 3D printing Guide.md # Parts list and print settings
│ ├── FTC Shooting and Intake Mechanism Theory.pdf # Theory behind the design
│ ├── V3 Shooting Assembly Guide.pdf # Main assembly guide (V3 kit)
│ ├── V3 Shooting Assembly Guide.html # Source of the main assembly guide
│ └── V3 Shooter 3D files/ # The 3 files to print
│ ├── FTC Shooter V3 Rail Guard.stl # Main shooter (in the kit)
│ ├── prolabs_plain_sheet_0p2.stl
│ ├── plate_368_cut_5x5.stl
│ ├── Older versions/ # FTC Shooter V2 Rail Guard.stl (not in the kit)
│ └── Testing videos and photos/ # 5 photos and a walkaround video of the finished V3 shooter
├── FTC Intake mechanism Upgrade/ # v1 intake roller, printing guide, calculations
│ ├── v1 by Aarav Jaisingh.md # Start here
│ ├── Intake Upgrade v1.stl # The part to print
│ ├── Printing Guide.md # Print settings and fit check
│ ├── Intake Calculations.md # Typed notes from the handwritten paper
│ └── Intake calculations (handwritten).jpg
├── FTC chassis options # Chassis design options
├── Help forum # Questions and support
├── LICENSE
└── README.md
```

### Quick Links

| Folder / File | Use It For |
|---|---|
| [FTC Camera](./FTC%20Camera) | AprilTag codes and camera setup for precise positioning |
| [Camera buying Guide](./FTC%20Camera/Camera%20buying%20Guide.md) | Choosing a webcam for AprilTag detection |
| [FTC Docs by Aarav Jaisingh](./FTC%20Docs%20by%20Aarav%20Jaisingh) | Shooting and intake strategy guide |
| [FTC precise shooting mechanism](./FTC%20precise%20shooting%20mechanism) | Shooter theory, V3 print files, and guides |
| [V3 Shooter 3D files](./FTC%20precise%20shooting%20mechanism/V3%20Shooter%203D%20files) | The 3 files to print |
| [Testing videos and photos](./FTC%20precise%20shooting%20mechanism/V3%20Shooter%203D%20files/Testing%20videos%20and%20photos) | Photos and a walkaround video of the finished V3 shooter on the robot |
| [BOM & 3D printing Guide](./FTC%20precise%20shooting%20mechanism/BOM%20%26%203D%20printing%20Guide.md) | Parts list and print settings for the V3 shooter |
| **[V3 Shooting Assembly Guide](./FTC%20precise%20shooting%20mechanism/V3%20Shooting%20Assembly%20Guide.pdf)** | **Main assembly guide** for the V3 shooter upgrade kit (PDF) |
| [FTC Intake mechanism Upgrade](./FTC%20Intake%20mechanism%20Upgrade) | v1 intake roller STL, printing guide, and calculations |
| [FTC chassis options](./FTC%20chassis%20options) | Picking the right chassis |
| [Help forum](./Help%20forum) | Getting help from the community |

### Suggested Path for New Teams

1. **Start with the chassis.** Open `FTC chassis options` and pick a base.
2. **Build the shooter.** Print the parts using the `BOM & 3D printing Guide`, then follow the main assembly guide: [V3 Shooting Assembly Guide](./FTC%20precise%20shooting%20mechanism/V3%20Shooting%20Assembly%20Guide.pdf).
3. **Plan intake and scoring.** Read the guide in `FTC Docs by Aarav Jaisingh`. The v1 intake roller files are in [`FTC Intake mechanism Upgrade`](./FTC%20Intake%20mechanism%20Upgrade).
4. **Add vision.** Pick a webcam with the `Camera buying Guide`, then use `FTC Camera/FTC-camera(v1).py` for AprilTag positioning.
5. **Stuck?** Check the `Help forum`.

---

## Getting Started

### Step 1: Get a Copy

You can browse files directly on GitHub. If you want a local copy, clone the repository:

```bash
git clone https://github.com/Aarav-111/FTC-Bangalore-Resources.git
cd FTC-Bangalore-Resources
```

If you do not use Git, click the green **Code** button on GitHub and choose **Download ZIP**.

### Step 2: Read Before You Build

Before cutting metal or printing parts, read the strategy guide and the shooter documentation fully. Most build mistakes happen because a team starts building before it understands the full design.

### Step 3: Adapt, Do Not Just Copy

Every team has different parts, budgets, and tools. Treat these designs as a strong starting point. Change sizes, motors, and materials to match what your team has.

---

## Resource Details

### Chassis Options

The chassis is the foundation of your robot. A weak or poorly planned chassis will limit everything else you build on top of it. The `FTC chassis options` file compares common choices so you can decide based on speed, control, and ease of building.

| Chassis Type | Strength | Best For |
|---|---|---|
| Mecanum Drive | Moves in every direction | Precise alignment and scoring |
| Tank Drive | Strong pushing power, simple build | Rookie teams and defence |
| Hybrid / Custom | Mix of speed and control | Teams with experience |

For mecanum programming, see the [Mecanum Wheels Presentation](./FTC%20Chassis%20options/Mecanum%20Wheels%20Presentation.pdf) (11 slides, also as [PowerPoint](./FTC%20Chassis%20options/Mecanum%20Wheels%20Presentation.pptx) and [Google Slides](https://docs.google.com/presentation/d/1pFk_TT_chwXeRFNPrxQcVsmS2CjazTeqLPL-VRhJ6fk/edit)).

### Precise Shooting Mechanism

The shooter design in `FTC precise shooting mechanism` focuses on repeatability. A shooter that scores 9 out of 10 times is worth more than a fast shooter that scores 5 out of 10. The folder covers:

- Flywheel setup and why speed control matters
- How to keep the launch angle consistent
- Feeding game elements smoothly into the shooter
- Tuning and testing to improve accuracy

What is inside:

| File / Folder | What It Is |
|---|---|
| `FTC Shooting and Intake Mechanism Theory.pdf` | Theory behind the shooter and intake design |
| `V3 Shooter 3D files` | The 3 files to print (see below), plus `Older versions` and `Testing videos and photos` |
| `BOM & 3D printing Guide.md` | Parts list and 3D printing settings |
| `V3 Shooting Assembly Guide.pdf` | **Main assembly guide** for the V3 shooter upgrade kit |

**What to print (V3):** all at 100% infill. Print 2 sheets, 1 of everything else.

| # | File | Part | Size |
|---|---|---|---|
| 1 | `FTC Shooter V3 Rail Guard.stl` | V3 rail guard (main shooter) | about 217 x 88 x 116mm |
| 2 | `prolabs_plain_sheet_0p2.stl` | Prolabs OP2 (Flex) Sheet, 2 per robot | 88 x 104 x 0.2mm |
| 3 | `plate_368_cut_5x5.stl` | Plate 368 replacement | 40 x 40 x 1.5mm |

The older V2 rail guard (`Older versions/FTC Shooter V2 Rail Guard.stl`, about 181 x 88 x 71mm) is not in the kit.

**V3 bill of materials:** the printed parts above (2 sheets), 16 zip ties (2.5mm wide), electrical tape and a small bottle of super glue. No rubber bands. The kit also has a spare plate 368. Full list in the BOM guide.

> Built on a robot (see the photos), not shooting tested yet. Fit numbers are from CAD.

**3D printing tips:**

- Use 100% infill for every part.
- Print the rail guard sideways. This keeps the main shooter curve smooth. A rough curve causes shooting problems. Do not use supports.
- Print the flex sheet and plate 368 flat on the bed.

### Intake mechanism Upgrade

The `FTC Intake mechanism Upgrade` folder has the first files for an intake upgrade by Aarav Jaisingh. v1 is a 180 mm roller, about 30 mm in diameter, with a 7 mm hexagonal hole through its length. Start with [v1 by Aarav Jaisingh](./FTC%20Intake%20mechanism%20Upgrade/v1%20by%20Aarav%20Jaisingh.md). The [Printing Guide](./FTC%20Intake%20mechanism%20Upgrade/Printing%20Guide.md) has the print settings (100% infill). [Intake Calculations](./FTC%20Intake%20mechanism%20Upgrade/Intake%20Calculations.md) walks through the handwritten size notes.

How the roller is mounted on the robot is still to confirm.

### FTC Camera and AprilTags

AprilTags are square markers placed on the field. A camera on your robot can detect them and calculate exactly where the robot is. The `FTC Camera/FTC-camera(v1).py` file gives you a starting point to:

- Detect AprilTags with the robot camera
- Estimate the robot's position and angle
- Use that position to aim, align, and drive more accurately

This is especially useful during the autonomous period, where small errors in position can cost a lot of points.

Not sure which camera to buy? The [Camera buying Guide](./FTC%20Camera/Camera%20buying%20Guide.md) compares four webcams available in India, from the budget BigPassport Pro-Live N3 (about Rs 999) to the Logitech C920 HD Pro. Its pick: the C920 for the best clarity and focus, and the Brio 100 as a cost effective 1080p option. Tip: lower the resolution in code (720p or 480p) to keep a stable 30 FPS loop on the Control Hub.

Ready to put the camera on the robot? The [Camera Integration Plan](./FTC%20Camera/Camera%20Integration%20Plan.md) explains how to move from the Python app to Java on the FTC SDK (VisionPortal and AprilTag clusters), with a starter OpMode, [`CameraAimTeleOp.java`](./FTC%20Camera/CameraAimTeleOp.java), for auto-aim and shooter speed from distance. Not robot tested yet.

---

## Strategy Guide Overview

The guide in `FTC Docs by Aarav Jaisingh` explains how the shooting and intake systems work together. A great shooter is useless if the robot cannot pick up game elements quickly, and a fast intake is wasted if the shooter misses.

Key ideas from the guide:

1. **Design the full cycle.** Think about pick up, transfer, aim, and shoot as one system.
2. **Reduce cycle time.** Every second saved in a cycle adds up over a full match.
3. **Make it reliable first.** A simple design that always works beats a complex one that breaks.
4. **Test with real game elements.** Practice under match conditions, not just on the bench.

---

## Tips for Indian FTC Teams

| Challenge | Practical Tip |
|---|---|
| Parts take long to ship | Order key parts early and keep spares of motors and servos |
| Limited budget | Use 3D printed parts and aluminium sheet where possible |
| No experienced mentor | Use this repository and the help forum, and connect with nearby teams |
| Hot and humid conditions | Check batteries and wiring often, heat affects performance |
| Limited field access | Build a partial practice field with key scoring zones |

Other habits that help:

- Keep an engineering notebook from day one. Judges value clear records.
- Share what you learn. Strong teams across India make the whole community better.
- Practice driving as much as you build. Driver skill wins close matches.

---

## Help Forum

Have a question? Open the `Help forum` file for guidance, or start a discussion by opening an issue on this repository. When you ask, include:

- What you are trying to build
- What you have tried so far
- Photos or code snippets if possible

Clear questions get faster and better answers.

---

## Contributing

Found a bug or have a better design? Contributions from every Indian FTC team are welcome.

1. Fork this repository.
2. Create a new branch for your change.
3. Add your design, code, or documentation with clear notes.
4. Open a pull request explaining what you added and why.

Please keep files organised in the existing folder structure and use simple, clear language so new teams can follow along.

---

## Roadmap

| Planned Addition | Status |
|---|---|
| More chassis CAD files | Planned |
| Improved AprilTag code (v2) | Planned |
| V3 shooter 3D files | Done |
| Shooter BOM and printing guide | Done |
| V3 Shooting Assembly kit guide | Done |
| Testing videos and assembly photos | Photos and a walkaround video are in [Testing videos and photos](./FTC%20precise%20shooting%20mechanism/V3%20Shooter%203D%20files/Testing%20videos%20and%20photos). Shooting test videos planned |
| AprilTag camera buying guide | Done |
| Intake mechanism documentation | v1 STL, printing guide and calculations are in [FTC Intake mechanism Upgrade](./FTC%20Intake%20mechanism%20Upgrade). More to come |
| Autonomous path examples | Planned |
| Video build guides | Planned |

---

## Credits

| Role | Name |
|---|---|
| Created by | Aarav Jaisingh |
| In collaboration with | Team R- Factor (FRC), led by Nilesh Shah |
| Supported by | Prolabs Robotics |

Thank you to every team and mentor who shares knowledge openly. This project grows because of you.

---

## Contact

**Prolabs Robotics**

Email: [prolabsrobotics@gmail.com](mailto:prolabsrobotics@gmail.com)

For questions about these resources, collaboration ideas, or support for your team, feel free to reach out.

---

## License

This project is under the MIT License. See the [LICENSE](./LICENSE) file for details.
