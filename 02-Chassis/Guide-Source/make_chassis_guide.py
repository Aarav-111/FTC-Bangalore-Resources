# How to rebuild: run 'python3 render_chassis.py' (needs trimesh and pyvista) to make img/, then
# 'python3 make_chassis_guide.py' (needs Pillow, qrcode and Google Chrome) to make out/Mecanum Chassis Guide.html and .pdf.
import base64, io, os, subprocess, html, qrcode
from PIL import Image, ImageChops
IMG='img/'; OUTDIR='out/'; os.makedirs(OUTDIR,exist_ok=True)
TITLE='Mecanum Chassis Guide'
def img(n,w=1100):
    im=Image.open(IMG+n).convert('L').convert('RGB')
    bb=ImageChops.difference(im,Image.new('RGB',im.size,(255,255,255))).getbbox()
    if bb: im=im.crop((max(bb[0]-20,0),max(bb[1]-20,0),min(bb[2]+20,im.width),min(bb[3]+20,im.height)))
    im.thumbnail((w,w)); b=io.BytesIO(); im.save(b,'PNG',optimize=True)
    return 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
def qr(url):
    b=io.BytesIO(); qrcode.make(url,border=1).save(b,'PNG'); return 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
CSS=open('style.css').read()+'''
pre{font-family:"DejaVu Sans Mono",Menlo,monospace;font-size:7.3pt;line-height:1.25;border:1.5px solid #000;padding:2mm 3mm;margin:1.5mm 0;white-space:pre-wrap;background:#fff}
.two{display:flex;gap:4mm}.two>div{flex:1}
.src td{font-size:8.5pt;word-break:break-all}
h3{font-size:12pt;margin:3mm 0 1.5mm}
'''
FOLDER='https://github.com/Aarav-111/FTC-India-Resources/tree/main/02-Chassis'

# ---------- SVG diagrams ----------
def wheel_svg(cx,cy,pattern):
    # top view wheel: rectangle with roller lines. pattern '/' or '\\'
    s=f'<rect x="{cx-9}" y="{cy-22}" width="18" height="44" rx="2" fill="#fff" stroke="#000" stroke-width=".8"/>'
    for k in range(-3,4):
        y=cy+k*6
        if pattern=='/': s+=f'<line x1="{cx-7}" y1="{y+4}" x2="{cx+7}" y2="{y-4}" stroke="#000" stroke-width="1.6"/>'
        else: s+=f'<line x1="{cx-7}" y1="{y-4}" x2="{cx+7}" y2="{y+4}" stroke="#000" stroke-width="1.6"/>'
    return s
def chassis_svg(good=True,title=''):
    fl,fr,bl,br=('\\','/','/','\\') if good else ('/','\\','\\','/')
    s=f'<svg viewBox="0 0 100 120" style="width:100%;height:78mm">'
    s+='<text x="50" y="7" font-size="5" text-anchor="middle" font-weight="bold">FRONT</text>'
    s+='<rect x="22" y="14" width="56" height="92" fill="#ededed" stroke="#000" stroke-width=".8"/>'
    s+=wheel_svg(12,32,fl)+wheel_svg(88,32,fr)+wheel_svg(12,88,bl)+wheel_svg(88,88,br)
    if good:
        s+='<line x1="12" y1="32" x2="88" y2="88" stroke="#000" stroke-width=".5" stroke-dasharray="2 1.5"/><line x1="88" y1="32" x2="12" y2="88" stroke="#000" stroke-width=".5" stroke-dasharray="2 1.5"/>'
    else:
        s+='<ellipse cx="50" cy="60" rx="44" ry="34" fill="none" stroke="#000" stroke-width=".5" stroke-dasharray="2 1.5"/>'
    s+=f'<text x="50" y="117" font-size="4.6" text-anchor="middle" font-weight="bold">{title}</text></svg>'
    return s
def hub_svg():
    names=[('0','frontLeftMotor'),('1','backLeftMotor'),('2','frontRightMotor'),('3','backRightMotor')]
    s='<svg viewBox="0 0 170 110" style="width:100%;height:100%">'
    s+='<rect x="55" y="20" width="60" height="70" rx="3" fill="#ededed" stroke="#000" stroke-width="1"/><text x="85" y="50" font-size="6" text-anchor="middle" font-weight="bold">Control Hub</text><text x="85" y="58" font-size="4.2" text-anchor="middle">motor ports 0 to 3</text>'
    pos=[(30,30,'FL'),(30,80,'BL'),(140,30,'FR'),(140,80,'BR')]
    for (p,n),(x,y,t) in zip(names,pos):
        s+=f'<rect x="{x-14}" y="{y-8}" width="28" height="16" fill="#5c5c5c" stroke="#000"/><text x="{x}" y="{y+2}" font-size="5" text-anchor="middle" fill="#fff" font-weight="bold">{t} motor</text>'
        hx=58 if x<85 else 112; hy=30+int(p)*14
        s+=f'<line x1="{x+(14 if x<85 else -14)}" y1="{y}" x2="{hx}" y2="{hy}" stroke="#000" stroke-width="1"/><rect x="{hx-3 if x<85 else hx}" y="{hy-3}" width="3" height="6" fill="#000"/>'
        s+=f'<text x="{x}" y="{y+15}" font-size="4" text-anchor="middle">port {p}: {n}</text>'
    s+='<text x="85" y="104" font-size="4.2" text-anchor="middle">Plug each encoder cable into the encoder port with the same number.</text></svg>'
    return s

def page(inner): return f'<section class="page">{inner}</section>'
def info(rows): return '<table class="info">'+''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a,b in rows)+'</table>'
def sb(sid,title,sp,tx,rows,main,ci='',cap='',mainhtml=None):
    mh=mainhtml if mainhtml else f'<img src="{img(main)}" alt="{sid}">'
    cih=f'<div class="ii"><img src="{img(ci,700)}" alt=""><div class="cap">{cap}</div></div>' if ci else '<div class="ii"></div>'
    return f'<div class="sb"><div class="sh"><span class="ck"></span><span class="sid">{sid}</span><span class="st">{title}</span><span class="sp">{sp}</span></div><div class="tx">{tx}</div>{info(rows)}<div class="imgs"><div class="mi">{mh}</div>{cih}</div></div>'

STEPS=[
 ('1a','Lay out the two side rails','Step 1 of 5: Build the frame','Put the two 384 mm U-channels on a flat table, open side up, parallel to each other.',
  [('Parts','2 x 1120 Series U-Channel, 15 hole, 384 mm'),('Size and position','Outside to outside, the frame is 288 mm + 2 x 48 mm = 384 mm wide, so the frame is about 384 x 384 mm.'),('Tip','Build on a flat table. A frame built on an uneven floor can twist, and then one wheel lifts off the mat.')],'s1a.png'),
 ('1b','Add the cross channels and check square','Step 1 of 5: Build the frame','Fit the two 288 mm U-channels between the side rails, one at the front and one at the back. Screw them in loosely, then measure both diagonals.',
  [('Parts','2 x 1120 Series U-Channel, 11 hole, 288 mm, corner brackets or plates, M4 screws'),('Size and position','The two diagonals must be the same length, within about 1 mm. Then tighten every screw.'),('Tip','If the diagonals differ, push the long diagonal corners together a little, then measure again.')],'s1b.png'),
 ('2a','Mount the four motors','Step 2 of 5: Motors','Bolt one 312 RPM Yellow Jacket motor at each corner, with the 8 mm REX output shaft pointing out through the side rail.',
  [('Parts','4 x 5203 Series Yellow Jacket, 19.2:1, 312 RPM, motor mounts, M4 screws'),('Size and position','All four shafts at the same height. Front and back shafts at the same distance from the frame ends.'),('Tip','Mark each motor FL, FR, BL and BR with tape now. It saves a lot of time when wiring.')],'s2a.png','s2a_ci.png','Close-up: shaft through the side rail'),
 ('2b','Check the shaft lines from above','Step 2 of 5: Motors','Look down on the frame. The left and right shafts at the front must be on one straight line. Do the same for the back.',
  [('Size and position','Front pair on one line, back pair on one line, and the two lines parallel.'),('Tip','A motor that is a little crooked makes the robot drift and wobble. Fix it now, before the wheels go on.')],'s2b.png'),
 ('3a','Add spacers and the outer bearing','Step 3 of 5: Bearings, spacers and wheels','Fit spacers (standoffs) from the side rail, and an outer plate with a bearing, so the wheel shaft is held on both sides of the wheel.',
  [('Parts','Spacers, 1 outer plate per wheel, 1 bearing per wheel, M4 screws'),('Size and position','Leave a small gap (about 1 to 2 mm) between the wheel and the rail, and between the wheel and the outer plate.'),('Which way','The bearing sits on the same line as the motor shaft.'),('Tip','A wheel held only by the motor shaft can bend the shaft when the robot is hit. The outer bearing stops this.')],'s3a.png'),
 ('3b','Fit the four wheels','Step 3 of 5: Bearings, spacers and wheels','Put each wheel on its shaft with a hub. The GripForce set has 2 left wheels and 2 right wheels. Put them on so the rollers make an X when you look from above (see page 5).',
  [('Parts','1 x GripForce Mecanum Wheel Set, 104 mm (4 wheels), 4 hubs'),('Size and position','Front left and back right are the same type. Front right and back left are the other type.'),('Tip','Check the X before you tighten the hubs. Swapping two wheels later is slow.')],'s3b.png','s3b_ci.png','Close-up: wheel between the rail and the outer plate'),
 ('4a','Check the X from above','Step 4 of 5: Check and balance','Look straight down on the robot. The top rollers of the four wheels must point towards the centre, making an X.',
  [('Size and position','Front left rollers: top left to bottom right. Front right: top right to bottom left. Back wheels: the mirror.'),('Which way','If you see an O (rollers going round the robot), two wheels are swapped. See page 5.'),('Tip','Take a photo from above and draw the lines on it. It makes the X easy to see.')],'top_X.png'),
 ('4b','Place the hub and battery low and central','Step 4 of 5: Check and balance','Mount the Control Hub and the battery inside the frame, low down and near the centre.',
  [('Size and position','Try to keep the centre of mass near the middle of the four wheels. Heavy parts low.'),('Which way','Keep the USB and ports of the Control Hub easy to reach.'),('Tip','If one corner is much lighter, that wheel slips and the robot drifts when strafing.')],'s4b.png'),
]

pages=[]
QR=qr(FOLDER)
pages.append(f'''<section class="page cover"><div class="band"><h1>{TITLE}</h1><div class="sub">Prolabs Robotics. A goBILDA style FTC chassis with 4 x 104 mm mecanum wheels and 312 RPM Yellow Jacket motors. Build, wiring, configuration, code and testing.</div></div>
<div class="covimg"><div><img src="{img('cover.png')}" alt="Mecanum chassis">Mecanum chassis, front right</div><div><img src="{img('top_X.png')}" alt="Top view">Top view: rollers make an X</div></div>
<div class="note">Rollers must make an X when you look from above. If you see an O, two wheels are swapped.</div>
<div class="covrow"><div class="cred"><b>Created by:</b> Aarav J.<br><b>Collaborators:</b> R-Factor FRC<br><br>5 build steps, then wiring, configuration, code, a first drive test and troubleshooting.<br>Costs are approximate. Nothing in this guide has been tested on our robot yet unless we say so.</div><div class="qrs"><div class="qr"><img src="{QR}" style="width:34mm;height:34mm;display:block"><div class="qrlab">Scan for this folder on GitHub (presentation and files)</div></div></div></div></section>''')

checklist=''.join(f'<div><span class="b"></span>{s[0]} {s[1]}</div>' for s in STEPS)+''.join(f'<div><span class="b"></span>{t}</div>' for t in ['5a Wire the motors','5b Make the configuration','6 Set motor directions','7 Load the drive code','8 First drive test'])
pages.append(page(f'''<h2 class="sec">Before you start</h2><table class="legend"><tr><th>In the pictures</th><th>Meaning</th></tr>
<tr><td><svg width="40mm" height="9mm" viewBox="0 0 40 9"><rect x="1" y="1" width="38" height="7" fill="#5c5c5c" stroke="#000" stroke-width=".6"/></svg></td><td>Dark part: the part you add or move in this step</td></tr>
<tr><td><svg width="40mm" height="9mm" viewBox="0 0 40 9"><rect x="1" y="1" width="38" height="7" fill="#ededed" stroke="#8f8f8f" stroke-width=".6"/></svg></td><td>Light grey part: already on the robot</td></tr>
<tr><td><svg width="40mm" height="9mm" viewBox="0 0 40 9"><line x1="2" y1="4.5" x2="31" y2="4.5" stroke="#000" stroke-width="2"/><polygon points="38,4.5 30,0.5 30,8.5"/></svg></td><td>Black arrow: move the part this way</td></tr></table>
<p class="small"><b>What this guide is.</b> A simple, goBILDA style mecanum chassis: a U-channel frame, 4 direct drive motors, and 4 mecanum wheels held by the motor shaft on one side and a bearing on the other. It is one good way to build it, not the only way. If you want everything in one box, the goBILDA Strafer Chassis Kit is a complete, tested alternative (see the parts list).</p>
<p class="small"><b>Directions.</b> Front is the side marked FRONT in the pictures. Left and right are as seen from behind the robot, looking forward. All sizes are in mm.</p>
<p class="small"><b>3D printed parts.</b> This chassis does not need printed parts. If you print any extra parts (wire guides, covers, mounts), print them at 100% infill.</p>
<p class="small"><b>More reading.</b> The <i>Mecanum Wheels Presentation</i> in this same folder explains how mecanum wheels move, with the maths. Our <i>Shooter Trajectory Calculations</i> doc (FTC Docs folder) uses the robot position this chassis gives you.</p>
<h2 class="sec" style="margin-top:2mm">Checklist</h2><div class="cl">{checklist}</div>'''))

pages.append(page(f'''<h2 class="sec">Parts list (approximate costs)</h2>
<table><tr><th>Part</th><th>Qty</th><th>goBILDA SKU</th><th>Approx. cost (USD)</th></tr>
<tr><td>1120 Series U-Channel, 15 hole, 384 mm (side rails)</td><td>2</td><td>1120-0015-0384</td><td>about 38 (18.99 each)</td></tr>
<tr><td>1120 Series U-Channel, 11 hole, 288 mm (cross channels)</td><td>2</td><td>1120-0011-0288</td><td>about 30 (14.99 each)</td></tr>
<tr><td>5203 Series Yellow Jacket motor, 19.2:1, 312 RPM, 8 mm REX shaft</td><td>4</td><td>5203-2402-0019</td><td>about 220 (54.99 each)</td></tr>
<tr><td>GripForce Mecanum Wheel Set, 104 mm, 40A rollers (set of 4)</td><td>1 set</td><td>3625-0202-0104</td><td>about 190 (189.99)</td></tr>
<tr><td>Motor mounts, hubs, bearings, spacers, outer plates, brackets, M4 screws</td><td>as needed</td><td>various</td><td>about 60 to 100 (our estimate)</td></tr>
<tr><td><b>Total for the chassis parts above</b></td><td></td><td></td><td><b>about 540 to 580</b></td></tr>
<tr><td>Alternative: Strafer Chassis Kit, 104 mm GripForce (complete kit)</td><td>1</td><td>3209-0001-0007</td><td>about 700 (699.99)</td></tr></table>
<p class="small">Prices are goBILDA list prices in US dollars, read from goBILDA product pages in November 2026. <b>All costs are approximate.</b> Prices in India are usually higher because of shipping, import duty and GST, and they change often. Please check with your supplier before you order. The Control Hub, battery, power switch and cables are not included in the totals.</p>
<h2 class="sec" style="margin-top:3mm">Tools</h2>
<table><tr><th>Tool</th><th>Used for</th></tr><tr><td>2.5 mm hex key (M4 screws)</td><td>Frame, motor mounts, plates</td></tr><tr><td>Ruler or tape measure</td><td>Checking the frame is square</td></tr><tr><td>Zip ties and flush cutters</td><td>Cable management</td></tr><tr><td>Thread locker (optional)</td><td>Screws near the wheels that shake loose</td></tr></table>
<h2 class="sec" style="margin-top:3mm">How fast will it go?</h2>
<p class="small">Wheel circumference = pi x 104 mm = about 327 mm. At 312 RPM (no load), that is 312 / 60 x 0.327 m = <b>about 1.70 m/s (about 5.57 ft/s)</b> forward, in theory. goBILDA lists the same 5.57 ft/s for the Strafer kit. Real speed is lower because of load and battery voltage, and strafing sideways is slower than driving forward.</p>'''))

pages.append(page(f'''<h2 class="sec">The roller pattern: X is right, O is wrong</h2>
<div class="two"><div>{chassis_svg(True,'RIGHT: rollers make an X from above')}</div><div>{chassis_svg(False,'WRONG: rollers make an O from above')}</div></div>
<div class="note">Look straight down on the robot. The top rollers of all four wheels should point towards the centre of the robot, like the two lines of an X.</div>
<p class="small">Each mecanum wheel has rollers at 45 degrees. A set has two kinds of wheels, often called left and right. The front left and back right wheels are one kind, and the front right and back left wheels are the other kind. gm0 explains that a standard mecanum drive has the wheels in an X shape, with the rollers angled towards the centre when you look from above.</p>
<p class="small"><b>The O mistake.</b> If two wheels are swapped, the rollers make an O. The robot still drives forward, backward and turns, so the mistake is easy to miss. But when you try to strafe, it moves badly or turns on the spot instead. Always do the strafe test in the first drive checklist.</p>
<div class="two" style="margin-top:2mm"><div><img src="{img('top_X.png',800)}" style="width:100%;height:62mm;object-fit:contain;border:1.5px solid #000"><div class="small" style="text-align:center;font-weight:bold">Our 3D model, from above (X)</div></div><div><img src="{img('top_O.png',800)}" style="width:100%;height:62mm;object-fit:contain;border:1.5px solid #000"><div class="small" style="text-align:center;font-weight:bold">Same robot with wheels swapped (O)</div></div></div>
<p class="small">In the bottom rollers (the ones touching the mat), the pattern looks the other way round. That is normal. Always check from above.</p>'''))

for i in range(0,len(STEPS),2):
    pages.append(page(''.join(sb(*s) for s in STEPS[i:i+2])))

pages.append(page(f'''<h2 class="sec">Step 5a: Wire the motors to the Control Hub</h2>
<div style="height:85mm">{hub_svg()}</div>
<table><tr><th>Motor</th><th>Control Hub motor port</th><th>Encoder port</th><th>Configuration name</th></tr>
<tr><td>Front left (FL)</td><td>0</td><td>0</td><td>frontLeftMotor</td></tr><tr><td>Back left (BL)</td><td>1</td><td>1</td><td>backLeftMotor</td></tr>
<tr><td>Front right (FR)</td><td>2</td><td>2</td><td>frontRightMotor</td></tr><tr><td>Back right (BR)</td><td>3</td><td>3</td><td>backRightMotor</td></tr>
<tr><td>Built-in IMU</td><td>inside the hub</td><td></td><td>imu (added by default)</td></tr></table>
<p class="small">The port numbers are our choice. Any order works, as long as the names in the configuration match the code. The names above are the same as the gm0 sample code, so you can use that code without changes.</p>
<ul class="small"><li>The motor power cable goes into the motor port. The encoder cable goes into the encoder port <b>with the same number</b>. If they do not match, the encoder reads the wrong motor.</li>
<li>Battery to the power switch, power switch to the Control Hub. Mount the switch where the referee can reach it.</li>
<li>Zip tie every cable to the frame, away from the wheels. A cable caught in a mecanum roller can rip out a connector.</li>
<li>Pull gently on every connector before each match. Loose cables are the most common reason a robot stops in a match.</li></ul>'''))

pages.append(page(f'''<h2 class="sec">Step 5b: Make the robot configuration</h2>
<ol class="small"><li>On the Driver Hub, tap the 3 dots menu, then <b>Configure Robot</b>, then <b>New</b>.</li>
<li>Tap <b>Control Hub Portal</b>, then <b>Control Hub</b>, then <b>Motors</b>.</li>
<li>For ports 0 to 3, choose the motor type <b>goBILDA 5202/3/4 series</b> and type the names from the table on the last page. Names are case sensitive: <b>frontLeftMotor</b> is not the same as <b>FrontLeftMotor</b>.</li>
<li>Check that the IMU is listed as <b>imu</b> (under I2C bus 0). It is added by default on a new configuration.</li>
<li>Tap Done, then Save. Give the configuration a name (for example <b>mecanum</b>) and activate it. The robot restarts.</li></ol>
<p class="small">These steps follow the FTC Docs page <i>Creating a Configuration</i> (see Sources). If the code says it cannot find a device, the name in the configuration and the name in the code do not match.</p>
<h2 class="sec" style="margin-top:3mm">Step 6: Set the motor directions</h2>
<p class="small">gm0 notes that most FTC motors spin counterclockwise (seen from the shaft end) when given positive power. On a direct drive chassis like ours, the motors on the two sides face opposite ways, so one side must be reversed in code. The gm0 sample reverses the right side. We start the same way:</p>
<pre>frontRightMotor.setDirection(DcMotorSimple.Direction.REVERSE);
backRightMotor.setDirection(DcMotorSimple.Direction.REVERSE);</pre>
<p class="small"><b>Test each wheel on its own</b> before you drive. Put the robot on a box so the wheels are off the ground. Then give each motor a small positive power, one at a time:</p>
<pre>// Test OpMode idea: hold a button to spin one motor forward slowly
if (gamepad1.x) frontLeftMotor.setPower(0.3);   // X = front left
if (gamepad1.y) frontRightMotor.setPower(0.3);  // Y = front right
if (gamepad1.a) backLeftMotor.setPower(0.3);    // A = back left
if (gamepad1.b) backRightMotor.setPower(0.3);   // B = back right</pre>
<table><tr><th>What you see</th><th>What to do</th></tr>
<tr><td>Every wheel spins so the robot would move forward</td><td>Good. Go to the code</td></tr>
<tr><td>All four spin backward</td><td>Reverse the left side instead of the right</td></tr>
<tr><td>One wheel spins the wrong way</td><td>Reverse only that motor in code, or check it is in the right port</td></tr>
<tr><td>The wrong wheel spins</td><td>The cable is in the wrong port, or the names are swapped in the configuration</td></tr></table>'''))

ROBOT=r'''package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;

// Robot-centric mecanum drive. Based on the gm0 "Mecanum TeleOp" sample.
@TeleOp
public class MecanumTeleOp extends LinearOpMode {
    @Override
    public void runOpMode() throws InterruptedException {
        // Names must match the robot configuration
        DcMotor frontLeftMotor = hardwareMap.dcMotor.get("frontLeftMotor");
        DcMotor backLeftMotor = hardwareMap.dcMotor.get("backLeftMotor");
        DcMotor frontRightMotor = hardwareMap.dcMotor.get("frontRightMotor");
        DcMotor backRightMotor = hardwareMap.dcMotor.get("backRightMotor");

        // Reverse the right side. If the robot drives backward, reverse the left side instead.
        frontRightMotor.setDirection(DcMotorSimple.Direction.REVERSE);
        backRightMotor.setDirection(DcMotorSimple.Direction.REVERSE);

        waitForStart();
        if (isStopRequested()) return;

        while (opModeIsActive()) {
            double y = -gamepad1.left_stick_y;      // Y stick is reversed
            double x = gamepad1.left_stick_x * 1.1; // 1.1 counteracts imperfect strafing
            double rx = gamepad1.right_stick_x;     // turning

            // Normalise: divide by the largest total so every power stays in [-1, 1]
            // and the ratio between the wheels is kept.
            double denominator = Math.max(Math.abs(y) + Math.abs(x) + Math.abs(rx), 1);
            double frontLeftPower = (y + x + rx) / denominator;
            double backLeftPower = (y - x + rx) / denominator;
            double frontRightPower = (y - x - rx) / denominator;
            double backRightPower = (y + x - rx) / denominator;

            frontLeftMotor.setPower(frontLeftPower);
            backLeftMotor.setPower(backLeftPower);
            frontRightMotor.setPower(frontRightPower);
            backRightMotor.setPower(backRightPower);
        }
    }
}'''
FIELD=r'''package org.firstinspires.ftc.teamcode;

import com.qualcomm.hardware.rev.RevHubOrientationOnRobot;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;
import com.qualcomm.robotcore.hardware.IMU;
import org.firstinspires.ftc.robotcore.external.navigation.AngleUnit;

// Field-centric mecanum drive. Based on the gm0 "Field-Centric Final Sample Code".
@TeleOp
public class FieldCentricMecanumTeleOp extends LinearOpMode {
    @Override
    public void runOpMode() throws InterruptedException {
        DcMotor frontLeftMotor = hardwareMap.dcMotor.get("frontLeftMotor");
        DcMotor backLeftMotor = hardwareMap.dcMotor.get("backLeftMotor");
        DcMotor frontRightMotor = hardwareMap.dcMotor.get("frontRightMotor");
        DcMotor backRightMotor = hardwareMap.dcMotor.get("backRightMotor");
        frontRightMotor.setDirection(DcMotorSimple.Direction.REVERSE);
        backRightMotor.setDirection(DcMotorSimple.Direction.REVERSE);

        IMU imu = hardwareMap.get(IMU.class, "imu");
        // Change these two to match how YOUR Control Hub is mounted
        IMU.Parameters parameters = new IMU.Parameters(new RevHubOrientationOnRobot(
                RevHubOrientationOnRobot.LogoFacingDirection.UP,
                RevHubOrientationOnRobot.UsbFacingDirection.FORWARD));
        imu.initialize(parameters);

        waitForStart();
        if (isStopRequested()) return;

        while (opModeIsActive()) {
            double y = -gamepad1.left_stick_y;
            double x = gamepad1.left_stick_x;
            double rx = gamepad1.right_stick_x;

            if (gamepad1.options) {   // reset "forward" to where the robot faces now
                imu.resetYaw();
            }
            double botHeading = imu.getRobotYawPitchRollAngles().getYaw(AngleUnit.RADIANS);

            // Rotate the joystick direction against the robot heading
            double rotX = x * Math.cos(-botHeading) - y * Math.sin(-botHeading);
            double rotY = x * Math.sin(-botHeading) + y * Math.cos(-botHeading);
            rotX = rotX * 1.1;  // counteract imperfect strafing

            double denominator = Math.max(Math.abs(rotY) + Math.abs(rotX) + Math.abs(rx), 1);
            frontLeftMotor.setPower((rotY + rotX + rx) / denominator);
            backLeftMotor.setPower((rotY - rotX + rx) / denominator);
            frontRightMotor.setPower((rotY - rotX - rx) / denominator);
            backRightMotor.setPower((rotY + rotX - rx) / denominator);
        }
    }
}'''
pages.append(page(f'''<h2 class="sec">Step 7a: Robot-centric drive code (Java)</h2>
<p class="small">Left stick moves the robot (forward, back, sideways, any angle). Right stick turns it. "Forward" on the stick is always the front of the robot. This is the gm0 sample, with our comments.</p>
<pre>{html.escape(ROBOT)}</pre>
<p class="small"><b>The 1.1 strafe factor.</b> Mecanum wheels strafe a little slower than they drive forward, because of roller friction. Multiplying x by 1.1 makes sideways and diagonal driving feel more even. gm0 uses 1.1, but it is up to your driver: try 1.0 to 1.2.</p>'''))
pages.append(page(f'''<h2 class="sec">Step 7b: Field-centric drive code (Java)</h2>
<p class="small">With field-centric drive, pushing the stick forward always moves the robot away from the driver, whichever way the robot is facing. It uses the IMU inside the Control Hub. Press OPTIONS (START on Xbox style gamepads) to reset forward.</p>
<pre>{html.escape(FIELD)}</pre>
<p class="small"><b>Normalising.</b> The SDK clips any power above 1 to 1. Without the denominator, powers like 0.4, 0.1, 1.1 and 1.4 would become 0.4, 0.1, 1.0 and 1.0, and the robot would curve. Dividing all four by the largest total keeps the same ratio (gm0).</p>'''))

pages.append(page('''<h2 class="sec">Step 8: First drive test checklist</h2>
<p class="small">Do these in order, at low speed first, on a clear floor or field tiles. One person drives, one person holds the power switch.</p>
<div class="cl" style="columns:1;font-size:10.5pt">'''+''.join(f'<div><span class="b"></span>{t}</div>' for t in [
 'Battery charged, power switch easy to reach, every cable zip tied away from the wheels',
 'Robot on a box: each wheel spins forward on its own (step 6)',
 'Rollers make an X from above (page 5)',
 'Left stick forward: robot drives straight forward',
 'Left stick back: robot drives straight back',
 'Left stick right: robot strafes right without turning much',
 'Left stick left: robot strafes left without turning much',
 'Left stick diagonal: robot moves at about 45 degrees',
 'Right stick: robot turns on the spot, both ways',
 'Drive forward and turn at the same time: smooth curve, no jerks',
 'Full speed for 2 tile lengths: robot stays straight, no wobble or noise',
 'Field-centric only: turn the robot 90 degrees, push forward, robot still moves away from you',
 'After 5 minutes of driving: check every screw, hub and wheel for looseness',
 ])+'''</div>
<div class="note">If the robot turns when you ask it to strafe, check the X pattern first, then the motor directions, then the weight balance.</div>'''))

TROUBLE=[('It drifts or turns when strafing','Check the X pattern from above. Check every wheel spins the right way. Move heavy parts so the weight is even on all 4 wheels. Check all 4 wheels touch the mat (a twisted frame lifts one). Try a strafe factor between 1.0 and 1.2. For autonomous, use the IMU to hold the heading.'),
 ('A wheel spins the wrong way','Reverse that motor with setDirection in code, or check that the motor cable is in the right port and the names in the configuration are not swapped.'),
 ('The wrong wheel spins','The motor is in a different port from the one in the configuration. Move the cable or fix the name.'),
 ('Wobble or shaking at speed','A hub or set screw is loose, a wheel is not straight on its shaft, a roller is damaged or has dirt in it, or a shaft is bent. Check the outer bearing is fitted and in line.'),
 ('Robot is heavy on one side or the front','Move the battery and the Control Hub towards the centre, low down. A light corner slips and drifts. Weigh each corner with a kitchen scale if you can.'),
 ('Robot curves when driving forward','A motor is weaker or a wheel is dragging. Spin each wheel by hand to feel for rubbing. Check the frame is square (step 1b).'),
 ('Robot does nothing, or the code crashes on INIT','Names in the code and the configuration do not match (case sensitive), or the configuration is not active.'),
 ('Field-centric goes the wrong way','The IMU orientation (logo and USB direction) does not match how the hub is mounted, or you did not reset the yaw facing forward.'),
 ('Strafing is very slow','This is normal for mecanum, a little. If very slow, check the X pattern and the strafe factor.')]
MIST=['Wheels in an O pattern instead of an X','Encoder cable in a different port number from its motor','Frame not square, so one wheel lifts off the mat','Wheel held only by the motor shaft, with no outer bearing, on a heavy robot','Cables near the wheels, where a roller can catch them','Heavy parts all on one side or high up','Forgetting to normalise the powers, so the robot curves at full stick']
pages.append(page('<h2 class="sec">Troubleshooting</h2><table style="font-size:9.5pt"><tr><th style="width:30%">Problem</th><th>What to check, and the fix</th></tr>'+''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a,b in TROUBLE)+'</table><h2 class="sec" style="margin-top:3mm">Common mistakes</h2><div class="cl" style="font-size:9.5pt">'+''.join(f'<div><span class="b"></span>{m}</div>' for m in MIST)+'</div>'))

SRC=[('gm0: Mecanum TeleOp (code, 1.1 strafe factor, normalising, field-centric)','https://gm0.org/en/latest/docs/software/tutorials/mecanum-drive.html'),
 ('gm0: Holonomic drivetrains','https://gm0.org/en/latest/docs/robot-design/drivetrains/holonomic.html'),
 ('FTC Docs: Creating a Configuration','https://ftc-docs.firstinspires.org/en/latest/hardware_and_software_configuration/configuring/getting_started/getting-started.html'),
 ('FTC Docs: IMU interface','https://ftc-docs.firstinspires.org/en/latest/programming_resources/imu/imu.html'),
 ('goBILDA: GripForce Mecanum Wheel Set, 104 mm (3625-0202-0104)','https://www.gobilda.com/gripforce-mecanum-wheel-set-o104mm-40a-durometer-rollers/'),
 ('goBILDA: Yellow Jacket motor, 19.2:1, 312 RPM (5203-2402-0019)','https://www.gobilda.com/5203-series-yellow-jacket-planetary-gear-motor-19-2-1-ratio-24mm-length-8mm-rex-shaft-312-rpm-3-3-5v-encoder/'),
 ('goBILDA: U-Channel, 15 hole, 384 mm (1120-0015-0384)','https://www.gobilda.com/1120-series-u-channel-15-hole-384mm-length/'),
 ('goBILDA: U-Channel, 11 hole, 288 mm (1120-0011-0288)','https://www.gobilda.com/1120-series-u-channel-11-hole-288mm-length/'),
 ('goBILDA: Strafer Chassis Kit, 104 mm GripForce (3209-0001-0007)','https://www.gobilda.com/strafer-chassis-kit-104mm-gripforce-mecanum-wheels/'),
 ('goBILDA: Bearings / Hubs / Spacers / Motor mounts','https://www.gobilda.com/bearings/ , https://www.gobilda.com/hubs/ , https://www.gobilda.com/spacers/ , https://www.gobilda.com/motor-mounts/'),
 ('REV: Control Hub getting started','https://docs.revrobotics.com/duo-control/control-hub-gs'),
 ('This repository: Mecanum Wheels Presentation (same folder)','github.com/Aarav-111/FTC-India-Resources/tree/main/02-Chassis'),
 ('This repository: Shooter Trajectory Calculations','github.com/Aarav-111/FTC-India-Resources/tree/main/07-Docs-and-Calculations')]
pages.append(page(f'''<h2 class="sec">Finished chassis</h2>
<div class="fin2"><div><img src="{img('fin2.png')}"><div class="c">Front left</div></div><div><img src="{img('front.png')}"><div class="c">Front view</div></div></div>
<h2 class="sec" style="margin-top:3mm">Sources</h2><table class="src"><tr><th style="width:42%">Source</th><th>Link</th></tr>'''+''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a,b in SRC)+'''</table>
<div class="covrow"><div class="cred small">Created by Aarav J. Collaborators: R-Factor FRC. Contact: ProlabsRobotics@gmail.com<br>Code adapted from gm0 (Game Manual 0). Prices read from goBILDA product pages, November 2026, approximate.<br>Any printed parts: 100% infill.</div></div>'''))

N=len(pages)
pages=[p.replace('</section>',f'<div class="foot">{TITLE}  |  Page {k+1} of {N}</div></section>',1) for k,p in enumerate(pages)]
out=f'<!doctype html><html><head><meta charset="utf-8"><title>{TITLE}</title><style>{CSS}</style></head><body>\n'+'\n'.join(pages)+'</body></html>'
open(OUTDIR+TITLE+'.html','w').write(out)
subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--no-pdf-header-footer','--print-to-pdf='+os.path.abspath(OUTDIR+TITLE+'.pdf'),'file://'+os.path.abspath(OUTDIR).replace(' ','%20')+'/'+TITLE.replace(' ','%20')+'.html'],check=True,stderr=subprocess.DEVNULL)
print('pages',N)
