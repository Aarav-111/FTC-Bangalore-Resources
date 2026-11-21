# Help Forum

This is the help page for [FTC India Resources](https://github.com/Aarav-111/FTC-India-Resources). We wrote it for Indian FTC teams who are using this repository, the V3 shooter kit, the intake upgrade kit, the camera plan, the mecanum presentation, or the docs.

We use simple English, and we only state facts we can stand behind. If something is a guess, a CAD number, or not yet tested on a robot, we say so. Approximate values are marked with "about" or "approximate".

This page is a team help guide. It is not the official rule book. For game rules, awards, inspection, and what is legal, the [FTC Competition Manual](https://ftc-resources.firstinspires.org/ftc/game/manual) is the source of truth. FIRST publishes Team Updates during the season, so please re-check the latest English PDF on the [Game and Season Materials](https://ftc-resources.firstinspires.org/ftc/game) page before an event. For software and hardware setup, use [FTC Docs](https://ftc-docs.firstinspires.org/).

If you have a question, [Ask your question here](https://forms.gle/SyWnmo3xL4crevMCA).

## Contents

1. [Frequently asked questions](#frequently-asked-questions)
   - [General FTC](#general-ftc)
   - [BIOBUZZ season basics](#biobuzz-season-basics)
   - [This repository](#this-repository)
   - [Team management](#team-management)
   - [Outreach](#outreach)
   - [Judging](#judging)
   - [The engineering portfolio](#the-engineering-portfolio)
   - [Budget and parts sourcing in India](#budget-and-parts-sourcing-in-india)
   - [SDK and Android Studio setup](#sdk-and-android-studio-setup)
   - [Blocks vs OnBot Java vs Android Studio](#blocks-vs-onbot-java-vs-android-studio)
   - [Road Runner and Pedro Pathing basics](#road-runner-and-pedro-pathing-basics)
   - [Odometry](#odometry)
   - [PID tuning](#pid-tuning)
   - [Sensors](#sensors)
   - [Wiring and power issues](#wiring-and-power-issues)
   - [Inspections](#inspections)
2. [The basics](#the-basics)
   - [How to use the guides](#how-to-use-the-guides)
   - [Printing](#printing)
   - [Wiring](#wiring)
   - [The SDK](#the-sdk)
   - [The Driver Hub](#the-driver-hub)
3. [Common mistakes](#common-mistakes)
4. [Troubleshooting](#troubleshooting)
5. [Glossary](#glossary)
6. [Ask a question](#ask-a-question)
7. [Links to files in this repository](#links-to-files-in-this-repository)

---

## Frequently asked questions

### General FTC

**What is FTC?**

FTC is FIRST Tech Challenge, a student robotics competition. This repository is for the **FTC 2027 Challenge**, which was released in 2026. The 2026-27 season game is **BIOBUZZ**, presented by RTX. We started this collection in Bangalore, but it is for every FTC team in India.

**What is the Control Hub, and what is the Driver Hub?**

The REV Control Hub is the computer on the robot. It runs your OpModes and talks to motors, servos and sensors. Official FTC Docs call this the Robot Controller. The REV Driver Hub is the driver station you hold. You use it to pick an OpMode, press INIT and START, watch telemetry, and (during INIT) open the camera preview.

FTC Docs say only the REV Control Hub and the REV Driver Hub are officially supported. An Android smartphone is legal in competition, but it is not supported, and teams who use one are responsible for their own testing and troubleshooting.

**What is an Expansion Hub?**

A REV Expansion Hub adds extra motor, servo and sensor ports. It connects to the Control Hub over a serial cable and shares the same 12V battery. Many teams add one when they run out of ports. Configure it in the robot configuration, and give every device a clear name.

**What do INIT and START mean?**

INIT is the period after you press INIT and before you press START. The robot can power up hardware, open the webcam, and show telemetry, but the match has not started. START runs the OpMode for real. This matters for the camera: the Driver Hub Camera Stream is meant to be used during INIT. See [The Driver Hub](#the-driver-hub).

For Autonomous, the official manual says drive teams who intend to run an OpMode during AUTO must select an OpMode with the 30 second timer enabled, then press INIT.

**What is an OpMode?**

An OpMode (Operational Mode) is a program that tells the robot what to do. There are two common types:

| Type | When it runs | Who is in control |
|---|---|---|
| Autonomous (`@Autonomous`) | The 30 second AUTO period | Only the pre-written program. Drivers may not give input |
| TeleOp (`@TeleOp`) | The 2 minute TELEOP period | Drivers use the gamepads |

In Java you will also see `LinearOpMode` (the program waits with `waitForStart()` and then runs step by step) and `OpMode` (it uses `init()`, `loop()` and `stop()`). Both are legal. Our starter camera file, [`CameraAimTeleOp.java`](../FTC%20Camera/CameraAimTeleOp.java), is a `LinearOpMode`.

**Which SDK should we use?**

Our Java camera plan and [`CameraAimTeleOp.java`](../FTC%20Camera/CameraAimTeleOp.java) were written for **FTC SDK v12.0**, the official 2026-27 release. Older AprilTag code that reads `detection.id` on every detection will not compile on SDK v12.0, because detections are now two types. Please see the [Camera Integration Plan](../FTC%20Camera/Camera%20Integration%20Plan.md). The official SDK is the [FtcRobotController](https://github.com/FIRST-Tech-Challenge/FtcRobotController) repository.

**Where do the official rules come from?**

This repository is a set of team resources. It is not the rule book. For game rules, tag print files, field setup, awards, and inspection, use the official [FTC Competition Manual and game resources](https://ftc-resources.firstinspires.org/ftc/game/manual). For software and hardware setup, use [FTC Docs](https://ftc-docs.firstinspires.org/). If a help page, chatbot, or this forum disagrees with the latest English Competition Manual, the manual wins.

**How is a match structured?**

The official BIOBUZZ Competition Manual describes each match as:

| Period | Official length | What happens |
|---|---|---|
| AUTO | 30 seconds | Robots run on their own. Drivers may not give input |
| Transition | 8 seconds | A short gap between AUTO and TELEOP, used for scoring as described in the manual |
| TELEOP | 2 minutes | Drivers operate the robots |

Two alliances play, and each alliance is two FTC teams. After the match there is a field reset. Please use the official manual for timing cues, penalties, and the full setup rules.

**Who may stand in the alliance area as the drive team?**

The official manual says a drive team is up to 4 people from the same team who are responsible for that match. Only 1 member of the drive team may be a non-student. The roles are:

| Role | Official limit | Who it may be |
|---|---|---|
| Drive Coach | 1 | Any team member, and this person may be an adult. This person must wear the Drive Coach badge |
| Drivers and Human Player | 3 in total | Students. They must wear a Drive Team badge |

The manual defines a student as a person who has not completed high school, secondary school, or the comparable level in their home region as of 1 September of the current season. Please re-check the latest manual if your event staff give you more specific badge or queuing instructions.

**What is Gracious Professionalism?**

Gracious Professionalism is a FIRST value: do your best work while treating others with respect and kindness. It applies on and off the field, including in the pits, in judging, and when you help another team.


### BIOBUZZ season basics

**What game is this season?**

The 2026-27 season game is **BIOBUZZ**, presented by RTX. Our V3 shooter kit and camera plan are written for the [goBILDA FTC StarterBot 2026-27](https://www.gobilda.com/ftc-starter-bot-resource-guide-2026-2027-season/) with our upgrades.

The official match overview says robots collect POLLEN and NECTAR to move them to their GARDEN, to place them into the FLOWERS, and to launch them into their CELLS to cause a HIVE TIP, all to earn points. Each time a HIVE is tipped, an alliance may enter one of five NECTAR initially staged in the alliance area. With 60 seconds left in the match, alliances may enter all remaining NECTAR. Robots conclude the match by claiming ownership of the FLOWERS by placing NECTAR and returning to their LOADING ZONE.

We have not copied the full scoring table into this page, because FIRST can update point values in Team Updates. Please use Table 10-2 and the rest of Section 10 in the official Competition Manual for current match points and ranking points.

**What are POLLEN and NECTAR?**

These are the official scoring elements. Our shooter fit checks use these sizes:

| Element | Size we used | How it fits our V3 shooter channel |
|---|---|---|
| POLLEN | 71 mm | Fits. CAD shows about 8.5 mm of room per side |
| NECTAR | 91 mm | About 3 mm too wide. The channel is borderline, so we treat it as **POLLEN only** until we test on a robot |

Those fit numbers are from CAD. The kit has been built on a robot, but **shooting has not been tested yet**. Please check the fit by hand before competition use. Details are in the [BOM and 3D printing Guide](../FTC%20Kits/Shooter%20Upgrade%20Kit/BOM%20%26%203D%20printing%20Guide.md).

The official setup (Section 10.3.1) stages 40 POLLEN and 16 NECTAR (8 red and 8 blue) on the field. That includes 4 POLLEN pre-loaded in each of the 4 robots. The official robot setup rule says robots must start the match contacting 4 pre-loaded POLLEN. POLLEN may be held in or on the robot, or on the tiles as the manual describes. Please read Section 10.3.4 for the exact pre-load wording.

**What is a HIVE, a CELL, a FLOWER, and a GARDEN?**

These are official field elements. In short, from the Competition Manual:

- Each HIVE has CELLS. A HIVE is considered tipped when it moves from one stable state to the other, with the downward-facing CELL becoming the upward-facing CELL, and then the damper that was not contacting the frame begins to contact the frame.
- Launching into the upward-facing CELL is the official way to earn a HIVE TIP. The manual warns that launching at the downward-facing CELL while a HIVE is tipping may disrupt the tip.
- At the end of the match, POLLEN and NECTAR left in an upward-facing CELL score for that alliance.
- FLOWERS have a scoring volume described in the manual (between the top ring and the middle ring). Flower scoring cannot begin until there is one minute remaining in the match (rule G410). Achievements scored earlier are still scored, but are subject to penalties.
- GARDENS are alliance specific. POLLEN or NECTAR must be at least partly in the garden zone to qualify. Gardens are not protected zones.

Use the official manual and field drawings for the exact legal definitions. Do not rely only on this short summary.

**What is a HIVE CELL AprilTag cluster, and how do AprilTags work this season?**

Each HIVE CELL has a **4-tag AprilTag cluster** on its underside. The tags are family **tag36h11**. According to the official FTC docs and SDK v12.0 (as summarised in our [Camera Integration Plan](../FTC%20Camera/Camera%20Integration%20Plan.md)):

- BIOBUZZ has **4 clusters and no single tags**.
- The four cluster names in SDK v12.0 are `RED SCORING`, `RED AUDIENCE`, `BLUE AUDIENCE` and `BLUE SCORING`.
- The cluster pose points to roughly the centre of the CELL opening, which is useful for aiming.
- CELLs tip during the match, so we should aim with the relative pose (`range` and `bearing`) and not trust field position (`robotPose`) from these tags.

Print practice tags at real size from the official game resources. Tag IDs should be checked against the Competition Manual before you print.

**Has the V3 shooter been shooting tested?**

No. It has been built on a robot. We have [photos and a short walkaround video](../FTC%20precise%20shooting%20mechanism/V3%20Shooter%203D%20files/Testing%20videos%20and%20photos) of the finished build. Shooting test videos are not online yet. Fit numbers in the guides are from CAD. For the maths behind a shot, see [Shooter Trajectory Calculations](../FTC%20Docs%20by%20Aarav%20Jaisingh/Shooter%20Trajectory%20Calculations.md). Those calculations still need to be checked against real shots.

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
| [FTC Docs by Aarav Jaisingh](../FTC%20Docs%20by%20Aarav%20Jaisingh) | Shooting and intake strategy guide, shooter trajectory calculations, and a copy of the mecanum presentation |
| [Help Forum](./README.md) | This page |

There is also a 1-byte placeholder file at the repo root named `FTC chassis options`. The real chassis materials are in the folder [`FTC Chassis options`](../FTC%20Chassis%20options) (capital C).

**What is in each kit, and where are the kit files?**

All kit files are in [FTC Kits](../FTC%20Kits):

- [Shooter Upgrade Kit](../FTC%20Kits/Shooter%20Upgrade%20Kit): 1 V3 shooter, 2 Plate 368 (1 spare), 2 OP2 sheets (one on each side, flared out), electrical tape, zip ties, and a small bottle of super glue. Guide: [V3 Shooting Assembly Guide](../FTC%20Kits/Shooter%20Upgrade%20Kit/V3%20Shooting%20Assembly%20Guide.pdf).
- [Intake Upgrade Kit](../FTC%20Kits/Intake%20Upgrade%20Kit): 1 FTC intake attachment, foam, and zip ties. Tape is not in the kit (any tape is fine to start the foam wrap). Guide: [Intake Assembly Guide](../FTC%20Kits/Intake%20Upgrade%20Kit/Intake%20Assembly%20Guide.pdf) (13 pages, 7 steps).

**How much foam goes on the intake attachment?**

Wrap the foam layer by layer until it reaches the POLLEN: it should just touch the POLLEN and give it a light squeeze, about 2 to 3 mm. About 50 mm across is a good place to start testing, but the POLLEN fit check (step 5 in the [Intake Assembly Guide](../FTC%20Kits/Intake%20Upgrade%20Kit/Intake%20Assembly%20Guide.pdf)) decides the real size. This has not been tested on a robot yet. The planned 50 mm figure comes from the [intake calculations](../FTC%20Intake%20mechanism%20Upgrade/Intake%20Calculations.md) and still needs a check on a real robot.

**Do we have to copy the designs exactly?**

No. Please treat these designs as a strong starting point. Every team has different parts, budgets, and tools. Change sizes, motors, and materials to match what your team has, and check the fit on your own robot.

**Where should a new team start?**

1. Read this Help Forum, then the main [README](../README.md).
2. For a chassis and for mecanum driving, open [FTC Chassis options](../FTC%20Chassis%20options).
3. For the shooter, read the [BOM and 3D printing Guide](../FTC%20Kits/Shooter%20Upgrade%20Kit/BOM%20%26%203D%20printing%20Guide.md), then follow the [V3 Shooting Assembly Guide](../FTC%20Kits/Shooter%20Upgrade%20Kit/V3%20Shooting%20Assembly%20Guide.pdf) (27 pages, 15 steps).
4. For intake and scoring ideas, read the guide in [FTC Docs by Aarav Jaisingh](../FTC%20Docs%20by%20Aarav%20Jaisingh). The v1 intake roller and [FTC Intake Attachment](../FTC%20Intake%20mechanism%20Upgrade/FTC%20Intake%20Attachment.stl) files are in [FTC Intake mechanism Upgrade](../FTC%20Intake%20mechanism%20Upgrade). To build the intake kit, follow the [Intake Assembly Guide](../FTC%20Kits/Intake%20Upgrade%20Kit/Intake%20Assembly%20Guide.pdf). The trajectory maths are in [Shooter Trajectory Calculations](../FTC%20Docs%20by%20Aarav%20Jaisingh/Shooter%20Trajectory%20Calculations.md).
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

### Team management

**How should we organise the team?**

FTC is a student-centred program. Adults may coach and mentor, but students should do the designing, building, coding, driving, and judging presentation. A simple structure that many teams use is:

| Area | Typical student work |
|---|---|
| Mechanical | Chassis, intake, shooter, CAD, 3D printing, repairs |
| Programming | TeleOp, Autonomous, sensors, cameras, version control |
| Electrical | Wiring, battery care, configuration, spare cables |
| Drive team | Driving practice, human player practice, match checklist |
| Outreach and documentation | Portfolio, outreach records, social media, sponsor notes |

You do not need a large team to be organised. Write down who owns each job, who is the backup person, and when you will practise. Keep a shared folder for CAD, code, the portfolio, and packing lists.

**How should we plan the season?**

A plan that usually works is: learn the game, pick a simple first robot that can score reliably, practise driving early, then improve one thing at a time. The main README already says this: make the design reliable first, reduce cycle time, and test with real game elements.

Leave time before each event for inspection practice, a portfolio review, a charged spare battery, and a packing list. Do not plan a major redesign the night before a competition.

**How do we keep code and CAD safe?**

Use version control (Git and GitHub, or a similar tool) for code. Save named copies of CAD files. Keep a known-good version of the robot code that you can reinstall at an event if a laptop fails. The official SDK already lives on GitHub, and your TeamCode should be backed up off the Control Hub as well as on it.

**What should we practise besides building?**

Driver skill wins close matches. Practise intake, shooting or scoring, defence awareness, and parking, under a timer. Practise the official drive team roles, including the human player rules in the manual. Practise the judging interview as a group, with a time limit.

### Outreach

**What counts as outreach in FTC?**

Outreach is how your team shares FIRST and STEM with other people: other teams, schools, families, sponsors, and your community. In the 2026-27 judged awards, outreach and team sustainability are recognised mainly under the Team Attributes awards: **Connect**, **Reach**, and **Sustain**. The official award descriptions live in Section 6 of the Competition Manual. In short:

| Award | What the official overview recognises |
|---|---|
| Connect | Connecting with the local STEM community and having a plan to develop team skills |
| Reach | Outreach that helps recruit new teams, coaches, mentors, or volunteers |
| Sustain | Leadership, resources, and plans for finances, seasons, and long-term team growth |

Not every award is given at every event. League meets do not present these judged awards. Please read the official criteria before you plan your season around a specific award.

**How should we record outreach?**

Write down the date, who you reached, what you did, and what you learned. Photos, attendance counts, and letters from schools or sponsors help, but judges will not click links in the portfolio, and they will not take extra printed papers from the interview back to the judging room. Put the evidence you want them to see **inside** the portfolio itself, within the page limits. Judges only consider the current season. For 2026-27, progress, challenges, and accomplishments since 1 January 2026 may be documented.

**What should we avoid?**

Do not invent numbers. Do not claim work you did not do. Do not use full student names in the portfolio (see the portfolio rules below). Outreach that only exists as a social media link, with no description in the portfolio, will not be reviewed.

### Judging

**How does judging work?**

The official manual says judges gather information from the Initial Interview, any follow-up interview, and the team portfolio (where applicable). Judges only consider published award criteria, and they only consider information from the current event and the current season. All judged award winners are recognised as positive examples of the criteria, not necessarily "the best" team.

You may participate in judging even if your robot has not passed inspection, and even if you attend without a robot.

**What are the team judged awards this season?**

The 2026-27 team judged awards fall into three groups, plus Judges' Choice:

| Group | Awards | Official focus |
|---|---|---|
| Overarching | Inspire | The most prestigious all-around award. It recognises teams who excel in Machine, Creativity, and Innovation (MCI), Team Attributes, and Documentation |
| Documentation | Think | The team's process and robot, documented in the portfolio |
| Team Attributes (TA) | Connect, Reach, Sustain | Skills, sustainability, and outreach |
| Machine, Creativity, and Innovation (MCI) | Innovate, Control, Design | Robot design, creativity, and control |
| Other | Judges' Choice | A team whose unique efforts do not fit the other categories |

"Motivate" is not in the 2026-27 team judged award list. Local program partners may give extra local awards, but those are not the team judged awards used for official advancement calculations.

The number of awards given depends on event size, and not every award is given at every event. No judged awards are presented at league meets. See Section 6 and Table 6-1 in the official manual.

**What happens in the interview?**

Students present the team and the robot (or the team's work) to judges. Practise a short, clear story: what you tried, what failed, what you changed, and why. Bring the robot if you can, and be ready to explain control, design choices, and outreach with examples from the portfolio. Adults may be present according to event instructions, but students should do the talking.

**What do the MCI awards look for, in short?**

From the official award summary materials:

- **Innovate** looks at engineering work that shows how the design was developed, and at a creative or unique robot or mechanism that is stable, reliable, and helps the team reach its game goals most of the time.
- **Control** requires a portfolio that lists control components, the challenge each one solves, and what each one does. The team must use one or more hardware or software solutions that use external feedback to control the robot and improve how it performs.
- **Design** looks at the whole robot, or the process used to create it, and whether the design is elegant, efficient, and practical to maintain.

Please read the full official criteria. The short lines above are a summary, not a substitute.

### The engineering portfolio

**What is the portfolio?**

The team portfolio is the official document judges may use as part of judging. It replaced the older idea of handing judges a full engineering notebook as the judged document. You can still keep a notebook or log for your own work. The document judges collect is the portfolio, and it has strict limits (rule A201 in the Competition Manual).

**What are the official portfolio limits for 2026-27?**

| Rule | Official requirement |
|---|---|
| Cover page | 1 cover page, which must include the team number. It may also include team name, contents list, organisations, sponsors, logo, motto, and a picture of the robot and/or team |
| Content pages | No more than 15 pages of content |
| Page size | US Letter (8.5 by 11 in.) or A4 (210 by 297 mm) |
| Digital size | If submitted digitally, the complete submission must be less than 15 MB |
| Date range | Only progress, challenges, and accomplishments since 1 January 2026 |

None of the content of the cover page is used to evaluate award criteria. The cover page is how judges identify the team. If judges cannot tell which team the portfolio belongs to, the team may be disqualified from judging. Any content beyond the 15 content pages will not be reviewed.

**How and when do we submit it?**

Rule A202 says portfolios must be submitted on time and as requested by the Event Director. If no other instructions are given, teams should submit 1 printed copy during the Initial Interview. Follow your event's instructions.

**What should we put in it?**

Put the evidence you want judges to see on the pages themselves. Official guidance includes:

- Design your portfolio for readability. Avoid fonts under 10 pt and low-contrast text on images.
- Judges will not click on links, websites, or videos.
- Judges cannot take extra printed papers from an interview back to the judging room.
- Minimise personally identifying information. For student privacy, use only first names and last initials. Student photographs are permitted, but full names must not be disclosed.
- You may use AI and research aids if you respect intellectual property rights and include a footnote or endnote credit. The official example is: "Portfolio created by Team XXXXX and ChatGPT".
- You may mention previous seasons to show growth, but the emphasis must be on the current season.

For the Think Award, the official materials say the portfolio must include at least one of: evidence of the engineering process, lessons learned and applied to the robot design, a comparison of choices (trade-offs), and/or maths used to make design or programming decisions. For the Control Award, the portfolio must include the control components, the challenges they solve, and their functions.

Our [Shooter Trajectory Calculations](../FTC%20Docs%20by%20Aarav%20Jaisingh/Shooter%20Trajectory%20Calculations.md) and intake calculation notes can help you show maths, but only include work your team actually used and understood, and say clearly what is calculated and what is still untested.


### Budget and parts sourcing in India

**How should we plan a budget?**

Write a simple list: what you already have, what you must buy, and what can wait. Typical groups are:

| Group | Examples |
|---|---|
| Control system | Control Hub, Driver Hub, legal 12V battery, charger, cables, gamepads |
| Drivetrain | Motors, wheels, hubs, channel or extrusion, bearings |
| Mechanisms | Intake, shooter, servos, 3D printed parts, fasteners |
| Sensors and vision | Webcam, extra sensors, mounting |
| Consumables and spares | Zip ties, tape, spare motor, spare battery, spare wires |
| Event costs | Registration, travel, printing the portfolio, team shirts if you want them |

The official robot construction rules require a legal battery and legal control system parts. Do not spend money on a battery or motor that is not allowed. Check Section 12 of the latest Competition Manual before you order.

**What does the V3 shooter kit already include?**

All kit files are in [FTC Kits](../FTC%20Kits).

| Kit | What the kit README says is included | Main guide |
|---|---|---|
| [Shooter Upgrade Kit](../FTC%20Kits/Shooter%20Upgrade%20Kit) | 1 V3 rail guard, 2 Plate 368 (1 used, 1 spare), 2 Prolabs OP2 sheets (both used), electrical tape, zip ties, and a small bottle of super glue. No rubber bands. No V2 | [V3 Shooting Assembly Guide](../FTC%20Kits/Shooter%20Upgrade%20Kit/V3%20Shooting%20Assembly%20Guide.pdf) |
| [Intake Upgrade Kit](../FTC%20Kits/Intake%20Upgrade%20Kit) | 1 FTC intake attachment, foam, and zip ties. Tape is not in the kit | [Intake Assembly Guide](../FTC%20Kits/Intake%20Upgrade%20Kit/Intake%20Assembly%20Guide.pdf) |

You still need the robot, motors, and the rest of the StarterBot or your own chassis.

**How do we buy parts in India?**

Plan for long shipping times. The main README already says this is a common challenge for Indian teams: order key parts early, and keep spares of motors and servos. Some webcams and electronics are easier to find on Indian storefronts. Our [Camera buying Guide](../FTC%20Camera/Camera%20buying%20Guide.md) compares four webcams available in India, with approximate prices (these can change by seller and stock):

| Webcam | Approximate price in the guide (22 October 2026) | Our note in the camera plan |
|---|---|---|
| BigPassport Pro-Live N3 | about Rs 999 | Bench testing only, no built-in SDK calibration |
| Logitech C270 | about Rs 2,000 to Rs 2,200 | Built-in SDK calibration at 640x480, good budget pick |
| Logitech Brio 100 | about Rs 2,750 to Rs 3,500 | No built-in SDK calibration until you calibrate it |
| Logitech C920 HD Pro | about Rs 7,000 to Rs 9,000 | Best pick in our plan, built-in calibration at 640x480 |

Those prices are estimates from the buying guide, not live offers. Confirm the current price and specifications on the seller's page before you order.

For goBILDA, REV, and other FTC parts, teams often order from official or authorised sellers, or from international distributors. We do not maintain a complete vendor list in this repository. Compare shipping time, customs, and whether the part is the official model named in the manual. A cheaper look-alike battery or cable may not be legal.

**How can we keep costs down?**

The main README suggests using 3D printed parts and aluminium sheet where possible, and ordering early so you do not pay for last-minute shipping. Print kit parts at 100% infill so you do not reprint after a break. Reuse legal parts from last season if the current rules still allow them. A simple, reliable mechanism often costs less than a complex one that fails in inspection or in a match.

**What about customs and taxes?**

Import rules and taxes can change, and they depend on the seller and the item. We cannot give a tax rate here. Ask the seller what is included, keep invoices, and leave extra time for a shipment that has to clear customs.

### SDK and Android Studio setup

**How do we install the FTC software?**

There are three official paths, described in [Choosing a Programming Tool](https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/choosing_program_lang/choosing-program-lang.html) and the [FtcRobotController](https://github.com/FIRST-Tech-Challenge/FtcRobotController) README:

1. **Blocks** or **OnBot Java**: you only need a web browser and a Control Hub (or official programming connection). You do not need Android Studio.
2. **Android Studio**: you install Android Studio on a computer, download or clone the official SDK, and write Java in the TeamCode module.

Update the Control Hub and Driver Hub apps to the season's official versions, not only the code on your laptop. A first check is that the official sample `ConceptAprilTag` builds and appears in the OpMode list.

**What version of Android Studio do we need?**

The official FtcRobotController README for the BIOBUZZ SDK says you need **Android Studio Narwhal 3 Feature Drop or later** to use the Android Studio project. That requirement can change when FIRST updates the SDK, so re-check the README when you install. FIRST also recommends that even advanced Java programmers start with the Blocks tutorial, then move to OnBot Java or Android Studio.

**Where does our code go?**

In Android Studio, team code belongs in the TeamCode module, for example:

`TeamCode/src/main/java/org/firstinspires/ftc/teamcode/`

That is where we tell you to put [`CameraAimTeleOp.java`](../FTC%20Camera/CameraAimTeleOp.java). Do not edit official sample files unless you are only enabling a sample by removing `@Disabled`. Keep your own files separate so SDK updates are easier.

**How do we get the code onto the Control Hub?**

- Blocks and OnBot Java build on the hub through the web interface.
- Android Studio installs the Robot Controller app to the Control Hub over USB or Wi-Fi, as described in FTC Docs.

After you install, restart the Robot Controller if the new OpMode does not appear, and check that you installed the app you meant to install, not an old copy.

**The project will not sync or build. What should we check first?**

Common setup problems, in order:

| Check | Why it matters |
|---|---|
| Official SDK for this season, not last season | Hardware names, AprilTag clusters, and samples change |
| Android Studio version meets the current SDK README | Older Studio may not open the project |
| Internet on the first Gradle sync | The project downloads dependencies |
| JDK and SDK components that Android Studio asks for | A missing platform or build tool will fail the build |
| File is in TeamCode and has `@TeleOp` or `@Autonomous` | Otherwise it will not show on the Driver Hub |

If the error message mentions a missing webcam class, AprilTag cluster type, or `VisionPortal`, you are probably on the wrong SDK version.

### Blocks vs OnBot Java vs Android Studio

**Which programming tool should we use?**

FIRST describes three official tools, and strongly recommends that all users begin by learning Blocks:

| Tool | How you write code | Official recommendation |
|---|---|---|
| Blocks | Drag and drop in a web browser | Best starting point for new programmers, and for people who prefer a visual tool |
| OnBot Java | Type Java in a web browser | For people who already have basic to advanced Java skills |
| Android Studio | Full Java development on a computer | Only for advanced users with extensive Java experience |

With Blocks and OnBot Java, you can create, edit and build OpModes with only a web browser. FTC Docs note that this can be an iPad, an Android phone, or a Chromebook. Android Studio needs a dedicated computer, and it has more editing and debugging features, but it is more complicated.

**Can we mix them?**

You can learn in Blocks and later move to Java. Our camera starter code is Java, because the VisionPortal and AprilTag cluster APIs we use are shown in the official Java samples. There are also official Blocks samples for AprilTags and the IMU. If your team is not ready for Android Studio, you can still use OnBot Java to paste or type Java on the hub.

**What should rookies do first?**

1. Complete an official Blocks tutorial OpMode that drives the robot and prints telemetry.
2. Learn INIT, START, and the gamepad blocks.
3. Add one sensor or the official AprilTag sample.
4. Move to OnBot Java or Android Studio only when the team is comfortable debugging simpler programs.

Do not start by copying a large community Autonomous (Road Runner or Pedro Pathing) if nobody on the team can yet drive the robot in a 20-line TeleOp.

### Road Runner and Pedro Pathing basics

**What are Road Runner and Pedro Pathing?**

They are popular **community** libraries for FTC Autonomous movement. They are not official FIRST software, and they are not included in this repository. Both help a robot follow paths on the field using a localizer (a way of estimating where the robot is) and a follower (a way of driving along a planned path).

| Library | Official docs | What it is, in short |
|---|---|---|
| Road Runner | [rr.brott.dev](https://rr.brott.dev/) | A widely used FTC motion planning and path following library, with tools for odometry and trajectory following |
| Pedro Pathing | [pedropathing.com/docs](https://pedropathing.com/docs) | Another widely used FTC path following library, with installation, drivetrain and localizer tuning, and a follower you configure in code |

We do not pick a winner here. Use the official docs for the library you choose, and use a version that supports the current season SDK. If a tutorial was written for an older SDK, check that it still compiles on SDK v12.0.

**When should we use one of them?**

They help when you want repeatable Autonomous paths: drive to a spot, turn, and score, with less hard-coded `sleep()` timing. They do not replace a working TeleOp, a tuned drivetrain, or a reliable scoring mechanism. If wheel directions, encoder signs, or the IMU heading are wrong, pathing libraries will also be wrong.

**What do we have to tune?**

Follow that library's official tuning guide. In general you will measure things such as wheel radius, track width, and localizer constants, then test path following on the field. Do not copy another team's constants. Their robot is not your robot. Tune on a charged battery, then recheck late in a practice day when the battery is lower.

**How does this relate to our camera code?**

Road Runner and Pedro Pathing estimate where the robot is on the field (odometry). Our camera plan is for aiming at a HIVE CELL with `range` and `bearing`. Those are different jobs. For BIOBUZZ, official AprilTag cluster docs and our plan say not to trust `robotPose` from CELL tags for field position, because CELLs tip. You can still use odometry for driving, and the camera for aiming, but do not mix the two without thinking about that limit.

### Odometry

**What is odometry?**

Odometry is a way to estimate the robot's position and heading from motion, usually from encoders and often with an IMU. It is used in Autonomous so the robot can drive to a point on the field. It always drifts over time. Vision or a known field feature can be used as a check, but for BIOBUZZ CELL tags, use care as described above.

**What are common FTC odometry setups?**

| Method | How it works | Honest limit |
|---|---|---|
| Drive motor encoders | The software counts the built-in encoders in the drive motors | Wheel slip (especially when you strafe, turn, or push) adds error |
| Dead-wheel (odometry pod) encoders | Free-spinning wheels with encoders rub on the field and are not driven by the motors | Usually more accurate than drive encoders if the pods stay in contact and the geometry is measured well |
| IMU heading | The Control Hub or Expansion Hub has a built-in IMU | Helps heading. It must be initialised, and the robot should be still during calibration |

Many pathing libraries support several localizers. Follow that library's docs for the one you install. We do not have a finished odometry CAD or code package in this repository yet.

**What should we measure carefully?**

Wheel diameter, the distance between odometry wheels, and the direction sign of each encoder. A small error in diameter grows as the robot drives farther. Mark these measurements in your notebook or portfolio, and say whether they were measured or copied from a datasheet. goBILDA and similar vendors publish nominal wheel sizes, but worn or different tyres can differ.

**The IMU on the Control Hub: which API should we use?**

Official SDK notes say newer Control Hubs may have a BHI260AP IMU, and older hubs have a BNO055 IMU. There is a newer `IMU` interface that works with both. The BHI260AP can only be used through the new `IMU` interface. You can see which IMU you have on the Manage page of the Control Hub web interface. FTC Docs: [Using the IMU](https://ftc-docs.firstinspires.org/programming_resources/imu/imu.html). If you want to swap hubs later, migrate to the new `IMU` interface now.

### PID tuning

**What is PID?**

PID is a control method that tries to reach a target and stay there. The three terms are:

| Term | Name | What it does |
|---|---|---|
| P | Proportional | Push harder when the error is larger |
| I | Integral | Slowly remove leftover error that P leaves behind |
| D | Derivative | Slow the motion when the error is changing quickly, which can reduce overshoot |

A fourth term, **F** (feedforward), is often used on FTC motors. It is a base power or velocity command for the target, so the PID only has to correct the rest. The REV hub velocity controller is often described as PIDF. Our [`CameraAimTeleOp.java`](../FTC%20Camera/CameraAimTeleOp.java) uses `DcMotorEx` launcher velocity and mentions PIDF coefficients from goBILDA's StarterBot example. Those example numbers are a starting point, not a guarantee for your robot.

**Where do we use PID in FTC?**

Common uses are flywheel or launcher speed, drivetrain heading or position, arm or lift position, and path following. For auto-aim, our starter OpMode uses a simple gain on bearing error (`TURN_GAIN`), with a maximum turn and a deadband (`AIM_TOLERANCE_DEG`). Those values are marked TUNE and have not been robot tested.

**How should we tune?**

Change **one** number at a time and write down what happened. Official advice in our camera plan is the same. A practical order many teams use:

1. Get the mechanism able to move smoothly with a safe, limited power.
2. Raise P until it reaches the target but starts to oscillate, then lower it a little.
3. Add D if it oscillates or overshoots.
4. Add a little I only if a steady leftover error remains. Too much I causes slow wobble or wind-up.
5. For velocity control, start from the motor or vendor example PIDF, then adjust.

Tune with a charged battery, then recheck with a partly used battery. Our camera plan already warns that a distance table is only as good as the battery.

**What should we not do?**

Do not copy PID values from another team and call the system tuned. Do not raise I first. Do not tune on blocks for a drive-position controller and then assume the same values work on the field. Do not leave a launcher PID so aggressive that it overshoots and fires at the wrong speed.

### Sensors

**What sensors do we already have?**

The Control Hub and Expansion Hub each have a built-in IMU on I2C bus 0. When you configure the hub, the app adds this IMU for you. Many FTC motors have built-in encoders. Our camera plan adds a USB webcam named `Webcam 1`.

**What other sensors do teams commonly use?**

Only use sensors that are legal in the current Section 12 rules. Common legal categories include:

| Type | Typical use |
|---|---|
| Motor encoders | Distance, velocity, and closed-loop motor control |
| IMU | Heading and tilt |
| Touch or limit switch | Know when an arm or intake has reached a stop |
| Colour and short-range sensors | Detect a game element or a line, at short range |
| Distance sensors | Measure a gap, if the range and lighting work in your tests |
| Webcam | AprilTags and other vision |

Configure every sensor in the robot configuration with a stable name, and use that exact name in code. Test each sensor with a small OpMode that only prints telemetry before you add it to the main program.

**What are common sensor limits?**

- I2C devices on the same bus can conflict. The built-in IMU already uses I2C bus 0. Official OnBot Java and Blocks guides say you add other I2C devices on that bus with the Add button, or use another bus (the hub has buses 0 to 3).
- Colour and distance readings change with lighting, distance, and the surface. Test on the field, not only on a desk.
- Encoder wires can come loose and suddenly read zero or jump. Strain-relieve the cables.
- A webcam is not a substitute for a well-mounted, calibrated camera. See the camera sections below.

### Wiring and power issues

**What powers the robot?**

The Control Hub and Expansion Hub are powered by a 12V rechargeable battery. Official FTC Docs describe a mechanical switch in the power path, and they note that the legal battery design includes a fuse for safety. The official construction rules require **exactly one approved 12V NiMH main battery**, used as the manual allows (including the legal fuse and any permitted connector changes). The legal part list is in Section 12 of the Competition Manual. Do not use a random 12V pack, a modified pack, or two main batteries.

REV and FTC Docs also publish [battery care and charging guidance](https://ftc-docs.firstinspires.org/en/latest/tech_tips/tech-tips/tech-tip-battery-care/tech-tip-battery-care.html). Charge with a compatible charger, inspect the pack and Anderson or XT30 connectors, and replace a swollen, damaged, or overheating battery.

**What is a brownout?**

A brownout is when battery voltage drops far enough under load that the Control Hub or motors reset or misbehave. Heavy acceleration, a stalled intake, or a flywheel spin-up on a low battery can cause it. Signs include a sudden reboot, a lost robot connection, or motors that stop and then restart. Use a charged legal battery, avoid stalling motors, and fix tight wiring or short circuits.

**How should we wire the robot?**

- Run power from the legal battery through the official switch to the hub, with the connector fully seated.
- Plug the webcam into the Control Hub **USB 3.0 port** (the blue one). Official FTC docs warn that ESD on the USB 2.0 port can cause Wi-Fi disconnects.
- Zip tie the camera cable every 10 to 15 cm, with slack loops at the camera and at the hub.
- Keep cables away from the launcher wheel, intake, and belts.
- Strain-relieve motor and encoder cables so a bump does not pull a connector out.
- Do not force connectors. If a JST connector is upside down, it will not seat.
- In hot and humid conditions, check batteries and wiring often. Heat can affect performance.

**The robot disconnects from the Driver Hub. What should we check?**

Loose 12V power, a tired battery, the webcam on USB 2.0, a damaged USB cable, or ESD. Official docs have ESD advice for webcams and hubs. Also keep the Driver Hub charged, and stay within the normal range of the field's wireless setup at an event. Event Wi-Fi rules are in the manual. Do not add your own illegal wireless devices.

### Inspections

**What is inspection?**

Before qualification or playoff matches, teams must pass a robot inspection. The official goal is to make sure the robot meets baseline safety and competition requirements. Student team members present the robot, all components that will be used, and the operator console. Inspectors review the requirements and help you find a fix if something fails. The Lead Robot Inspector (LRI) has the final authority on construction questions for eligibility.

An official inspection checklist is available from FIRST. Teams are strongly encouraged to self-inspect before every event.

**What are the BIOBUZZ robot size rules?**

From the official Robot Construction Rules (Section 12), as we read them in the Competition Manual. Re-check the latest manual before you cut or print a new mechanism.

| Rule | Official requirement |
|---|---|
| Starting configuration (R102) | In the starting configuration, all parts of the robot must be fully stationary, and the robot must be fully self-contained within an 18 in. (45.70 cm) wide by 18 in. (45.70 cm) long by 18 in. (45.70 cm) high volume |
| Pre-loaded scoring elements | Pre-loaded scoring elements may extend outside the starting size constraint |
| Support (R103) | The robot must be fully self-supported in the starting configuration (it must not push on the sides or top of a sizing tool). It may hold this with mechanical means while powered off, and/or by initialising an OpMode that holds motors and servos still |
| Weight (R104) | There is no official robot weight limit in BIOBUZZ. Weight still affects battery use, transport, field tiles, and performance |
| Expansion after the match starts (R105) | The robot may expand, but at all times must remain within an 18 in. (45.70 cm) by 24 in. (61.0 cm) by 29 in. (73.65 cm) tall volume. The 29 in. dimension is always the vertical height above the field. Limits must be physical, not only software. The robot may not be designed to deliberately detach components |

Inspectors will want to see maximum mechanical extensions. A robot that can mechanically go outside the volume is not legal even if software tries to stop it. If you use interchangeable mechanisms, be ready to show that every configuration complies.

If you hold the starting configuration with motors, the manual warns that this may last several minutes and can overheat a stalled motor. Tell the inspector if the robot is live or has stored energy (for example a stretched spring).

**Can we play practice matches before we pass inspection?**

The official manual says teams may participate in scheduled practice matches before passing inspection, but they may not participate in unscheduled or "filler line" practice matches before passing inspection. The FTA, LRI, or Head Referee may still stop a practice match if the robot is unsafe or likely to damage the field. You must pass inspection before qualification or playoff matches.

**What should we bring to inspection?**

Rule I301 says to bring the complete robot and supporting equipment: the robot and operator console with all components, including decorative parts, that will be used during matches. You do not have to use every inspected part in every match, but you should not add un-inspected components without re-inspection. Demonstrate all the ways the robot will be configured for a match.

**Inspection is not a complete search of every part.** The manual says teams must still follow the spirit of the construction rules even if an inspector does not check every item. Trying to hide an illegal part is a Competition Integrity Contract issue.

If something is still unclear, [Ask your question here](https://forms.gle/SyWnmo3xL4crevMCA).


---

## The basics

### How to use the guides

- Read the guide for a part **before** you print or cut anything. Most build mistakes happen when a team starts building before it understands the full design.
- For the V3 shooter, the **main** assembly guide is the [V3 Shooting Assembly Guide PDF](../FTC%20Kits/Shooter%20Upgrade%20Kit/V3%20Shooting%20Assembly%20Guide.pdf). The BOM page also has a short list of steps, but the PDF is the full, updated version (27 pages, 15 steps, 3D pictures, and 5 real photos). There is also an [interactive 3D simulator](https://ftc-shooter-interactive-guide.netlify.app/) that compares V3 with the older V2.
- The shooter kit is **V3 only**. The older V2 rail guard is in [Older versions](../FTC%20precise%20shooting%20mechanism/V3%20Shooter%203D%20files/Older%20versions). It is not in the kit. Do not print V2 unless you want that older part on purpose.
- For the intake kit, print [`FTC Intake Attachment.stl`](../FTC%20Intake%20mechanism%20Upgrade/FTC%20Intake%20Attachment.stl) using the [Printing Guide](../FTC%20Intake%20mechanism%20Upgrade/Printing%20Guide.md). In the slicer, rotate that STL by 90 degrees so it stands on one flat end, 180 mm tall (the file is exported lying on its side). Then follow the [Intake Assembly Guide](../FTC%20Kits/Intake%20Upgrade%20Kit/Intake%20Assembly%20Guide.pdf) (13 pages, 7 steps): slide the attachment onto the intake hex shaft, centre it, lock it with your shaft collars, and wrap the foam layer by layer until it reaches the POLLEN. The guide has not been tested on a robot yet. Check that your hex shaft fits the 7 mm hole before you start.
- For shot maths, use [Shooter Trajectory Calculations](../FTC%20Docs%20by%20Aarav%20Jaisingh/Shooter%20Trajectory%20Calculations.md). It covers projectile motion, hood angle and launch speed, the CELL entry window, flywheel energy and RPM recovery, air drag and the Magnus effect, and shooting while moving, with a worked example and Python 3.13 code. Treat calculated speeds and angles as a starting point until you test them on the robot.
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

The kit part to print is also in [FTC Kits/Intake Upgrade Kit](../FTC%20Kits/Intake%20Upgrade%20Kit) as [`FTC Intake Attachment.stl`](../FTC%20Kits/Intake%20Upgrade%20Kit/FTC%20Intake%20Attachment.stl), with a copy in the Intake mechanism Upgrade folder. The attachment STL is exported lying on its side. Rotate it 90 degrees so it stands on a flat end before you print, then use the same settings (100% infill, 3 or 4 walls, 5 to 8 mm brim, no supports).

After printing, let the part cool, peel the brim carefully, and check length, diameter, and the hex hole at both ends. The hex hole is about 0.06 mm off the centre line. That is very small, but we should still check the fit on the shaft. If the hole is tight, lightly sand the flats. Do not open it out so much that the shaft spins. Check that your intake hex shaft fits the 7 mm hex hole before you start, as the intake assembly guide says.

### Wiring

We do not have a full robot wiring diagram in this repository yet. These points come from our camera plan, official FTC Docs, and normal FTC practice:

- Use exactly one legal 12V NiMH main battery, as listed in the Competition Manual, through a legal switch, with the connector fully seated.
- Plug the webcam into the Control Hub **USB 3.0 port** (the blue one). Official FTC docs warn that ESD on the USB 2.0 port can cause Wi-Fi disconnects. See [Configuring an External Webcam](https://ftc-docs.firstinspires.org/en/latest/hardware_and_software_configuration/configuring/configuring_external_webcam/configuring-external-webcam.html).
- Zip tie the camera cable to the frame every 10 to 15 cm, with a small loop of slack at the camera and at the hub, so a hit does not pull the plug.
- Keep the cable away from the launcher wheel and the intake.
- If you add a second camera, use a USB hub on the USB 3.0 port. A Logitech C920 may need a powered hub.
- On the Driver Hub, use **Configure Robot, Scan**. Give each motor, servo and webcam a clear name, and keep those names exactly the same in code.
- If you add an Expansion Hub, use the official serial connection and include it in the same configuration.
- Do not force connectors. Check that the battery is locked in and that power cables cannot rub on wheels or belts.
- In hot and humid conditions, check batteries and wiring often. Heat can affect performance.

### The SDK

- Install **FTC SDK v12.0** (Android Studio Narwhal 3 Feature Drop or later, or the current version named in the official README) or use OnBot Java or Blocks. Then update the Control Hub and the Driver Hub.
- A good first check is the official sample `ConceptAprilTag`. Remove `@Disabled` so it shows in the OpMode list, then confirm it builds and appears on the Driver Hub.
- In SDK v12.0, `getDetections()` can return `AprilTagSingleDetection` or `AprilTagClusterDetection`. Check the type before you read fields. Old code that always reads `detection.id` will not compile.
- Our starter OpMode uses `VisionPortal` and `AprilTagProcessor`, at 640 x 480, with MJPEG, and with the official BIOBUZZ tag library. 640 x 480 has a built-in SDK calibration for the Logitech C920 and C270.
- Use the new `IMU` interface so the same code can work on older BNO055 hubs and newer BHI260AP hubs.
- Tune one number at a time, and write down what happened. Test on blocks with the wheels off the ground first.

### The Driver Hub

- Pick the configuration you saved, then pick the OpMode.
- Press **INIT** first, not START, when you want to look at the camera.
- Open the **3-dot menu**, choose **Camera Stream**, and tap the picture to refresh it. The Driver Hub camera preview is meant to be used **during INIT**. After START, many teams turn the preview off so the robot stays responsive. Our camera plan also says to turn off the preview during matches, because a live preview adds load.
- Wait until telemetry or the preview shows that the camera is actually running (for official samples, you should see a clear, steady image). If the camera never reaches a streaming state, the Driver Hub has nothing useful to show.
- Telemetry is the text on the Driver Hub. Our starter OpMode prints target name, range, bearing, aim state and launcher speed. Read it before you blame the hardware.
- If an OpMode does not appear in the list, check that the file is in TeamCode, that it has `@TeleOp` or `@Autonomous`, and that it is not `@Disabled`. Then rebuild and restart the Robot Controller.
- For Autonomous at a match, select an OpMode with the 30 second timer enabled, then press INIT, as the official manual requires.

---

## Common mistakes

### Using the FTC guides

- Starting to cut, print or assemble before reading the full guide.
- Following an old V2 step after the kit became V3 only (18 to 19 Nov 2026). There are no rubber bands, no zip-tie links, and both OP2 sheets are used.
- Treating the short BOM step list as the full assembly guide. Use the [27-page PDF](../FTC%20Kits/Shooter%20Upgrade%20Kit/V3%20Shooting%20Assembly%20Guide.pdf).
- Opening the 1-byte `FTC chassis options` file at the repo root, instead of the folder [`FTC Chassis options`](../FTC%20Chassis%20options).
- Putting [`FTC-camera(v1).py`](../FTC%20Camera/FTC-camera(v1).py) on the Control Hub. That file is a laptop tool.
- Treating CAD fit numbers, example launcher speeds, or untested tilt values as proven match settings.
- Treating the trajectory maths as a substitute for robot testing. The calculations are a tool. They still need real shots.
- Copying a design without checking it on your own robot, parts, and field.
- Using this Help Forum as if it were the Competition Manual. When they disagree, the latest official manual wins.

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
- Launching at the downward-facing CELL, or launching into a HIVE that is already tipping, in a way that disrupts the tip. The official manual warns about this.

### Building the intake

These points come from the [intake printing guide](../FTC%20Intake%20mechanism%20Upgrade/Printing%20Guide.md), [Intake Calculations](../FTC%20Intake%20mechanism%20Upgrade/Intake%20Calculations.md), and the [Intake Assembly Guide](../FTC%20Kits/Intake%20Upgrade%20Kit/Intake%20Assembly%20Guide.pdf). The intake assembly guide has not been tested on a robot yet, and we mark untested details below.

- Printing the roller on its side. Print it **standing on one flat end**, 180 mm tall, so each layer is a circle and the hex hole is a clean vertical hole.
- Leaving the slicer at the 3MF default of 15% infill and 2 walls. Use **100% infill** and 3 or 4 walls.
- Printing without a brim, or printing two tall rollers at once, so the part tips or gets knocked over.
- Starting a print on a machine with less than 180 mm of Z height, or not checking the brim and lid clearance on an A1 mini.
- Pulling the part off the bed while it is still hot, which can bend or snap it.
- Forcing a hex shaft through a tight hole, or sanding the hex so wide that the shaft spins.
- Skipping the POLLEN fit check and wrapping to a fixed diameter only. The [Intake Assembly Guide](../FTC%20Kits/Intake%20Upgrade%20Kit/Intake%20Assembly%20Guide.pdf) says to wrap layer by layer until the foam reaches the POLLEN, with a light squeeze of about 2 to 3 mm. About 50 mm across is a good place to start testing, but the fit check decides the real size. This has not been tested on a robot yet.
- Wrapping the foam in the wrong direction. The guide says to wrap in the same direction the intake spins.
- Gluing the foam before the fit is right, or skipping the 4 zip ties that hold the foam. Use zip ties as the guide says, and tape the ends if they lift. Tape is not in the kit.
- Forgetting to rotate `FTC Intake Attachment.stl` 90 degrees in the slicer so it stands on a flat end.
- Forcing the attachment onto a shaft that does not fit the 7 mm hex hole. Check the fit before you start.

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

### Pathing, odometry and PID

- Copying Road Runner or Pedro Pathing constants from another team.
- Using a tutorial written for an older SDK without checking that it compiles on SDK v12.0.
- Starting with a large pathing project before basic TeleOp, motor directions, and encoder signs are correct.
- Using the old `BNO055IMU` interface on a hub that has a BHI260AP IMU. Use the new `IMU` interface.
- Treating odometry as exact. It drifts. Recheck heading and position after long paths.
- Raising the I term first when a PID oscillates, or changing several PIDF values at once.
- Tuning a launcher PID on a full battery and never rechecking it on a used battery.

### Wiring, power and sensors

- Using a battery that is not on the official legal list, or using more than one main battery.
- Leaving the 12V connector half seated, or running without the legal switch and fuse arrangement the manual requires.
- Stalling a motor for a long time to hold the starting configuration, which the inspection rules warn can overheat the motor.
- Putting extra I2C sensors on bus 0 without adding them correctly in the configuration (the IMU is already on bus 0).
- Skipping a sensor-only test OpMode, then debugging a huge TeleOp when the sensor was unplugged or named wrongly.

### Inspections, judging and the portfolio

- Arriving at inspection without having self-inspected with the official checklist.
- Building a mechanism that can mechanically go outside the 18 by 24 by 29 in. tall limit, and hoping software will stop it. That is not legal.
- Forgetting that the starting configuration must fit the 18 in. cube and be self-supported, except that pre-loaded scoring elements may extend outside the starting size.
- Adding a part after inspection without going back for re-inspection.
- Trying to play an unscheduled or filler practice match before passing inspection.
- Submitting a portfolio without a cover page that shows the team number, or going over 15 content pages.
- Using fonts under 10 pt, or putting the important evidence only in a link or QR code. Judges will not click links.
- Using full student names, or including work from before 1 January 2026 as if it were this season's judged work.
- Letting only the coach talk in the judging interview.
- Planning the season around the old "Motivate" award name. The 2026-27 Team Attributes awards are Connect, Reach, and Sustain.

### General team mistakes

- Ordering key parts late. Shipping to many places in India takes time. Keep spares of motors, servos and a battery.
- Skipping the portfolio until the week of the event. The page limit is small, but the work it describes should span the season.
- Building more than you drive. Driver practice wins close matches.
- Testing only on the bench, never with real game elements or under match conditions.
- Changing the robot the night before a competition without time to test.
- Not labelling wires, or not bringing a toolkit, zip ties, tape and a charged battery to the venue.
- Keeping useful notes inside one team only. If something in these guides is wrong, please tell us so we can fix it.
- Spending the budget on a complex mechanism before you have a legal battery, a working control system, and a robot that can pass inspection.


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
| Calculated launch angle or speed does not score | The maths is not yet checked against real shots, or drag and hood angle differ from the model | Use [Shooter Trajectory Calculations](../FTC%20Docs%20by%20Aarav%20Jaisingh/Shooter%20Trajectory%20Calculations.md) as a starting point, then fill a real distance table from test shots |
| HIVE does not tip after a launch | Wrong CELL, a tip that was disrupted, or not enough elements in the CELL | Launch only into the upward-facing CELL, wait if a tip is already in progress, and read the official HIVE TIP criteria |

### Intake roller

| Symptom | Likely cause | Fix |
|---|---|---|
| Roller tips during the print | No brim, dirty bed, two rollers at once, or high speed up the part | 5 to 8 mm brim, clean bed, one roller at a time, slower outer walls in the upper half |
| Print will not start, or hits the lid | Printer Z height is under 180 mm, or the brim was not included in the height check | Check Z height in the slicer. An A1 mini is exactly 180 mm, so this is tight |
| Roller feels weak or the hex rounds out | Infill left at 15%, or only 2 walls | Reprint at 100% infill with 3 or 4 walls |
| Hex shaft will not go through | Hole is tight, or there is debris | Check about 7.00 mm across flats at both ends. Lightly sand. Do not force it |
| Shaft spins in the roller | Hole sanded too large | Reprint the roller. Do not open the hex out past a firm fit |
| Foam unwraps when the intake spins | Wrapped the wrong way, or not held with zip ties | Wrap in the same direction the intake spins, use 4 zip ties, and tape the ends if they lift |
| Attachment will not slide onto the shaft | Hex hole or shaft size mismatch, or the hole is tight | Check about 7.00 mm across flats. Lightly sand if needed. Do not force it. The guide says to centre the attachment and lock it with shaft collars |
| Foam diameter looks wrong, or POLLEN is not gripped | Wrapped to a guessed size, or the 50 mm starting size was treated as final | Follow the [Intake Assembly Guide](../FTC%20Kits/Intake%20Upgrade%20Kit/Intake%20Assembly%20Guide.pdf): wrap until the foam just touches the POLLEN with a light squeeze (about 2 to 3 mm). About 50 mm across is only a starting point, and it has not been tested on a robot yet |

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
| New OpMode does not appear on the Driver Hub | Wrong module, missing annotation, `@Disabled`, or old app installed | Put the file in TeamCode, add `@TeleOp` or `@Autonomous`, rebuild, install, and restart the Robot Controller |
| Android Studio will not import the SDK | Studio is older than the version in the official README | Install Android Studio Narwhal 3 Feature Drop or later, or the version currently named in the FtcRobotController README, then re-open the project |

### Mecanum drive

| Symptom | Likely cause | Fix |
|---|---|---|
| Robot will not strafe, or it curves when it should go sideways | Wheel rollers are not in an X, or one motor direction is reversed | Check wheel orientation against the [presentation](../FTC%20Chassis%20options/Mecanum%20Wheels%20Presentation.pdf), then check motor directions in code |
| Direction feels wrong at full stick, but better at half stick | Wheel powers not normalised | Normalise so the largest wheel power is 1, as the presentation shows |
| Field-centric drive drifts or goes the wrong way | IMU heading not initialised, or inverted | Recalibrate the IMU, set heading at the start of the match, and test as the presentation describes. Use the new `IMU` interface |
| Robot is hard to line up in front of the shooter | Using only tank turns to shift sideways | That is a reason teams use mecanum: you can strafe a little left or right without turning in a circle. See the presentation for the drive methods |

### Pathing, odometry and PID

| Symptom | Likely cause | Fix |
|---|---|---|
| Autonomous path starts in the wrong direction | Motor or encoder sign is wrong, or the starting pose is wrong | Reverse the sign in a small test, then set the starting pose to match how you place the robot |
| Paths look right at first, then drift | Odometry error, wrong wheel diameter, or a dead wheel that lifts off the field | Re-measure diameter and track width. Check that pods stay in contact. Do not expect zero drift |
| Heading slowly rotates while the robot sits still | IMU not calibrated, or the robot was moved during init | Calibrate on a still robot, and re-set heading if you bump the robot after INIT |
| `BNO055IMU` code fails on a new Control Hub | The hub has a BHI260AP IMU | Switch to the new `IMU` interface. Check the hub type on the Manage page |
| Launcher never holds a steady speed | PIDF not tuned, or battery voltage changing | Tune one term at a time from a vendor or example starting point. Recheck on a used battery |
| Robot oscillates around a heading or position target | P or I too high | Lower P, reduce I, and add a little D if needed. Widen the tolerance slightly if it is hunting at the target |
| Copied Road Runner or Pedro Pathing project will not compile | SDK version or library version mismatch | Use docs for a version that supports SDK v12.0, and update Gradle dependencies as those docs say |

### Wiring, power and sensors

| Symptom | Likely cause | Fix |
|---|---|---|
| Robot reboots when you accelerate or spin up the launcher | Brownout from a low or weak battery, or a stall | Use a charged legal battery. Avoid stalling. Check the 12V connector and switch |
| Robot dies in the middle of a match | Loose power connector, damaged battery, or blown fuse | Reseat the connector, inspect the pack, and replace a blown legal fuse with the type the manual allows |
| Driver Hub says the robot is disconnected | Power, USB 2.0 webcam ESD, or a tired Driver Hub | Check 12V power, move the webcam to USB 3.0, charge the Driver Hub, and follow official ESD advice |
| Motor does not move, but others do | Wrong port, wrong name, or a loose motor or encoder cable | Check the configuration, the port, and the connector. Confirm with a tiny test OpMode |
| Servo jitters or will not hold | Loose servo cable, a shared power problem, or a stall | Reseat the servo plug, check 12V voltage, and avoid commanding a servo into a hard stop for a long time |
| I2C sensor reads zero or drops out | Bus conflict, loose JST-PH cable, or wrong bus in the configuration | The IMU is already on bus 0. Add the sensor correctly, try another bus, and strain-relieve the cable |
| Colour or distance reading is different on the field | Lighting, range, or surface change | Retune thresholds on the actual field, and print the raw values in telemetry |

### Printing and first-layer problems

| Symptom | Likely cause | Fix |
|---|---|---|
| Shooter curve is rough or ridged | Printed upright, or supports marked the curve | Reprint sideways, 100% infill, no supports |
| 0.2 mm sheet fails or is the wrong thickness | Wrong layer height, or unlevel bed | One 0.2 mm layer, PETG, slow first layer, level bed |
| Tall intake roller comes off the bed | Weak first layer or no brim | 5 to 8 mm brim, clean bed or glue stick, slow first layer |
| Printed part is the wrong size | Slicer scaled the STL | Reset scale to 100%. Files are already in mm. Check 88 mm width on V3, 180 mm length and 7 mm hex on the roller |

### Inspection, judging and event day

| Symptom | Likely cause | Fix |
|---|---|---|
| Robot will not fit the starting sizing tool | Starting configuration is larger than the 18 in. cube, or it pushes on the tool | Fold or reset to the legal starting pose. It must be self-supported. Pre-loaded POLLEN may extend outside the cube, but the robot itself may not |
| Inspector says the expansion is illegal | A mechanism can physically go outside 18 by 24 by 29 in. tall | Add a hard mechanical stop. Software-only limits are not enough. Show the maximum extension |
| Motors get hot while waiting for inspection or a match | Starting pose is held by a stalled motor for several minutes | Change the hold so motors are not stalled against a hard stop. Tell the inspector if the robot is live |
| You are told you cannot play a filler practice match | Inspection is not finished | Finish inspection first. Scheduled practice may be allowed before inspection, filler practice is not |
| Judges cannot use your portfolio | Missing team number on the cover, too many pages, or it was late | Follow A201 and A202: 1 cover page with the team number, at most 15 content pages, submitted as the Event Director asked |
| Judges never saw your video or website | Links in the portfolio are not reviewed | Put the evidence on the pages. Do not depend on a URL or QR code |
| Interview ran out of time before the important point | The story was not practised | Practise a short student-led talk: problem, test, change, result |

If you still cannot fix the problem, [Ask your question here](https://forms.gle/SyWnmo3xL4crevMCA).

---

## Glossary

This glossary explains terms used in this Help Forum and in the linked guides. Official game terms are defined in Section 16 of the Competition Manual. If a short line here disagrees with the manual, use the manual.

| Term | Meaning |
|---|---|
| Alliance | In BIOBUZZ, two FTC teams who play together on one side of a match |
| Android Studio | The official advanced Java tool for writing FTC OpModes on a computer |
| AprilTag | A square printed marker that a camera can detect. BIOBUZZ uses family tag36h11 in 4-tag clusters on HIVE CELLS |
| AUTO | The first 30 seconds of a match, when drivers may not give input |
| Bearing | In the FTC AprilTag pose, the angle you need to turn to face the target. Positive means the target is to the left |
| Blocks | The official drag-and-drop programming tool in a web browser |
| Brownout | A drop in battery voltage under load that can reset or disrupt the Control Hub or motors |
| CAD | Computer-aided design. Some fit numbers in our guides come from CAD, not from a shooting test |
| CELL | Part of a HIVE. Teams launch scoring elements into an upward-facing CELL to help cause a HIVE TIP |
| Control Hub | The REV computer on the robot (Robot Controller) that runs OpModes and talks to devices |
| Dead wheel | A free-spinning encoder wheel used for odometry, not driven by a motor |
| Decimation | An AprilTag setting that shrinks the image before the tag search. Higher is faster, lower can see farther |
| Driver Hub | The REV driver station device used to select OpModes, press INIT and START, and view telemetry |
| Drive team | Up to 4 people from the same team for a match, with at most 1 non-student, in the roles defined in the manual |
| ESD | Electrostatic discharge. Official webcam docs warn that ESD on the USB 2.0 port can cause Wi-Fi disconnects |
| Expansion Hub | A REV module that adds motor, servo and sensor ports, connected to the Control Hub |
| Feedforward (F) | A base command in PIDF control, used so the PID only has to correct the rest |
| Field-centric | Drive control where "left" means left on the field, not left relative to the robot. Needs a heading sensor |
| FLOWER | A BIOBUZZ field element that scores POLLEN and NECTAR in a defined volume, with ownership and timing rules in the manual |
| FTC | FIRST Tech Challenge |
| GARDEN | An alliance-specific BIOBUZZ zone where POLLEN or NECTAR can score if they are at least partly inside it |
| goBILDA StarterBot | The official-style 2026-27 BIOBUZZ starter robot our V3 shooter kit is written for |
| Gradle | The build tool Android Studio uses to compile the FTC SDK project |
| Gracious Professionalism | A FIRST value: do your best work while treating others with respect and kindness |
| HIVE | A BIOBUZZ field structure that can tip between two stable states |
| HIVE TIP | The official condition when a HIVE has moved to the other stable state and the damper contacts the frame, as the manual defines |
| IMU | Inertial measurement unit. The Control Hub and Expansion Hub have a built-in IMU on I2C bus 0 |
| Infill | How solid a 3D printed part is inside. Our kit parts use 100% infill |
| INIT | The period after you press INIT and before START, used to set up hardware and to view the camera stream |
| Inspire Award | The most prestigious all-around 2026-27 team judged award |
| Inspection | The official robot check that must be passed before qualification or playoff matches |
| Java | The text language used in OnBot Java, Android Studio, and our `CameraAimTeleOp.java` |
| LEAVE | An official AUTO achievement: the robot must no longer contact the perimeter wall |
| LinearOpMode | A Java OpMode style that waits for START and then runs step by step |
| Loading zone | A BIOBUZZ field area named in the official manual. Robots return there at the end of the match as part of the official overview |
| Localizer | The part of a pathing library that estimates the robot's position and heading |
| LRI | Lead Robot Inspector, who has the final authority on construction questions at an event |
| Mecanum | A wheel type that can move the robot sideways as well as forward, when the rollers are mounted correctly |
| MJPEG | A camera stream format. Our Java plan uses MJPEG at 640x480 to save USB bandwidth |
| NECTAR | A BIOBUZZ scoring element. Our CAD uses 91 mm, and the V3 channel is borderline for it |
| Odometry | Estimating position from encoders and often an IMU |
| OnBot Java | The official browser-based Java programming tool |
| OpMode | An Operational Mode: a program that tells the robot what to do in AUTO or TELEOP |
| OP2 sheet | The Prolabs flex sheet in the V3 kit. Two sheets are used, one on each side, flared about 15 degrees |
| Operator console | The official name for the driver station setup that is brought to the field and to inspection |
| PARK | An official scoring achievement at the end of AUTO or TELEOP, as defined in the manual |
| Pedro Pathing | A community FTC path following library. Docs: [pedropathing.com/docs](https://pedropathing.com/docs) |
| PID or PIDF | A control method using proportional, integral, derivative, and often feedforward terms |
| Plate 368 | A StarterBot plate that must be replaced or cut so it does not block the POLLEN path |
| POLLEN | A BIOBUZZ scoring element. Our CAD uses 71 mm, and the V3 channel is designed around it |
| Portfolio | The official 2026-27 judged team document: 1 cover page plus at most 15 content pages, with other A201 limits |
| Range | In the FTC AprilTag pose, the straight-line distance from the camera to the target, in inches in our starter code |
| REV | REV Robotics, the maker of the official Control Hub and Driver Hub used by most teams |
| Road Runner | A community FTC motion planning and path following library. Docs: [rr.brott.dev](https://rr.brott.dev/) |
| Robot-centric | Drive control where "left" means the robot's left |
| RP | Ranking points, used with match points to rank teams in qualification, as described in the official manual |
| SDK | Software Development Kit. The official 2026-27 FTC release we use is v12.0 |
| Starting configuration | The pose in which the robot starts a match, which must fit the 18 in. cube rule |
| Strafe | Sideways motion, a common reason to use mecanum wheels |
| TELEOP | The 2 minute teleoperated period, when drivers control the robots |
| Telemetry | Text shown on the Driver Hub, used to debug sensors, pose, and motor speeds |
| TeamCode | The Android Studio module where your team's Java files belong |
| Trajectory | The path a launched POLLEN follows through the air. See our trajectory calculations doc |
| U-channels 316 and 317 | The StarterBot pillars beside the shooter. Their gap must be exactly 88 mm |
| USB 3.0 | The blue USB port on the Control Hub, which official docs recommend for the webcam |
| V2 | The older shooter rail guard. It is not in the kit |
| FTC Intake Attachment | The 180 mm printed intake part in the Intake Upgrade Kit, with a 7 mm hex hole, that the foam wraps around |
| FTC Kits | The folder that holds the Shooter Upgrade Kit and the Intake Upgrade Kit, including the main assembly guides |
| V3 | The current Prolabs shooter rail guard and kit this repository documents |
| VisionPortal | The official FTC SDK class that opens a camera and sends frames to processors such as AprilTagProcessor |
| Webcam 1 | The default webcam name in official samples and in our starter OpMode. The name in code must match the configuration |

---

## Ask a question

If this page and the guides do not answer your question, please ask us.

To send us a question, [Ask your question here](https://forms.gle/SyWnmo3xL4crevMCA).

You can also:

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
| FTC Docs by Aarav Jaisingh | [FTC Docs by Aarav Jaisingh](../FTC%20Docs%20by%20Aarav%20Jaisingh) |
| Shooter Trajectory Calculations | [Shooter Trajectory Calculations.md](../FTC%20Docs%20by%20Aarav%20Jaisingh/Shooter%20Trajectory%20Calculations.md) |
| Shooting and intake strategy guide | [FTC_Shooting_and_Intake_Mechanism.pdf](../FTC%20Docs%20by%20Aarav%20Jaisingh/FTC_Shooting_and_Intake_Mechanism.pdf) |
| Camera buying guide | [Camera buying Guide.md](../FTC%20Camera/Camera%20buying%20Guide.md) |
| Camera integration plan (Java) | [Camera Integration Plan.md](../FTC%20Camera/Camera%20Integration%20Plan.md) |
| Starter OpMode | [CameraAimTeleOp.java](../FTC%20Camera/CameraAimTeleOp.java) |
| Laptop AprilTag app | [FTC-camera(v1).py](../FTC%20Camera/FTC-camera(v1).py) |
| Mecanum presentation (PDF) | [Mecanum Wheels Presentation.pdf](../FTC%20Chassis%20options/Mecanum%20Wheels%20Presentation.pdf) |
| Mecanum presentation (PowerPoint) | [Mecanum Wheels Presentation.pptx](../FTC%20Chassis%20options/Mecanum%20Wheels%20Presentation.pptx) |
| Mecanum presentation (Google Slides) | [Google Slides](https://docs.google.com/presentation/d/10t6m5lrtCYghSzNBLcLgv_6zWi-kxssT0vhTHXqJd7Y/edit) |

Official docs we relied on include the [BIOBUZZ Competition Manual](https://ftc-resources.firstinspires.org/ftc/game/manual), [FTC Docs](https://ftc-docs.firstinspires.org/), and the sources listed in the [Camera Integration Plan, section 12](../FTC%20Camera/Camera%20Integration%20Plan.md).
