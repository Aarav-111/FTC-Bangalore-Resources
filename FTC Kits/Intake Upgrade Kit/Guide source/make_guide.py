# How to rebuild: run 'python3 render.py' (needs trimesh and pyvista) to make the pictures in img/, then 'python3 make_guide.py' (needs Pillow, qrcode and Google Chrome) to make the HTML and PDF in out/.
# Generator for "Intake Assembly Guide" (Prolabs Robotics). Same print style as the V3 Shooting Assembly Guide.
import base64, io, os, re, subprocess, qrcode
from PIL import Image
IMG='img/'
OUTDIR='out/'; os.makedirs(OUTDIR,exist_ok=True)
TITLE='Intake Upgrade Assembly Guide'
def img(n,w=1100):
    im=Image.open(IMG+n).convert('L').convert('RGB')
    # crop white borders
    bg=Image.new('RGB',im.size,(255,255,255)); from PIL import ImageChops
    bb=ImageChops.difference(im,bg).getbbox()
    if bb: im=im.crop((max(bb[0]-20,0),max(bb[1]-20,0),min(bb[2]+20,im.width),min(bb[3]+20,im.height)))
    im.thumbnail((w,w)); b=io.BytesIO(); im.save(b,'PNG',optimize=True)
    return 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
def qr(url):
    q=qrcode.make(url,border=1); b=io.BytesIO(); q.save(b,'PNG'); return 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
KITURL='https://github.com/Aarav-111/FTC-India-Resources/tree/main/FTC%20Kits/Intake%20Upgrade%20Kit'
CSS=open('style.css').read()

# life-size SVG: page drawn in mm
def lifesize():
    import math
    hexr=7/math.sqrt(3)
    hexpts=' '.join(f'{40+hexr*math.cos(math.radians(30+60*i)):.2f},{60+hexr*math.sin(math.radians(30+60*i)):.2f}' for i in range(6))
    ruler=''.join(f'<line x1="{5+i}" y1="5" x2="{5+i}" y2="{9 if i%10==0 else (7.5 if i%5==0 else 6.5)}" stroke="#000" stroke-width=".25"/>'+(f'<text x="{5+i}" y="12.5" font-size="2.6" text-anchor="middle">{i}</text>' if i%10==0 else '') for i in range(101))
    return f'''<svg width="184mm" height="215mm" viewBox="0 0 184 215">
<rect x="5" y="2" width="100" height="3" fill="none" stroke="#000" stroke-width=".3"/>{ruler}
<text x="110" y="6" font-size="3.4" font-weight="bold">Check: this ruler must be 100 mm.</text><text x="110" y="10.5" font-size="3">If not, print again at 100% scale.</text>
<g><circle cx="40" cy="60" r="15" fill="#5c5c5c" stroke="#000" stroke-width=".4"/><polygon points="{hexpts}" fill="#fff" stroke="#000" stroke-width=".3"/>
<text x="40" y="82" font-size="3.6" font-weight="bold" text-anchor="middle">FTC intake attachment, end view</text><text x="40" y="87" font-size="3.2" text-anchor="middle">30 mm across. Hex hole 7 mm across flats.</text><text x="40" y="91.5" font-size="3.2" text-anchor="middle">Stand the printed part on this circle to check it.</text>
<line x1="25" y1="40" x2="55" y2="40" stroke="#000" stroke-width=".3"/><polygon points="25,40 28,39 28,41"/><polygon points="55,40 52,39 52,41"/><text x="40" y="38" font-size="3" text-anchor="middle">30 mm</text></g>
<g><circle cx="125" cy="60" r="25" fill="#cfcfcf" stroke="#000" stroke-width=".4"/><circle cx="125" cy="60" r="15" fill="#5c5c5c" stroke="#000" stroke-width=".3"/><polygon points="{hexpts}" transform="translate(85,0)" fill="#fff" stroke="#000" stroke-width=".3"/>
<line x1="100" y1="30" x2="150" y2="30" stroke="#000" stroke-width=".3"/><polygon points="100,30 103,29 103,31"/><polygon points="150,30 147,29 147,31"/><text x="125" y="28" font-size="3" text-anchor="middle">about 50 mm (starting point)</text>
<text x="125" y="92" font-size="3.6" font-weight="bold" text-anchor="middle">With foam, end view</text><text x="125" y="97" font-size="3.2" text-anchor="middle">Grey ring: foam, about 10 mm thick all round.</text><text x="125" y="101.5" font-size="3.2" text-anchor="middle">Your POLLEN check (step 5) decides the real size.</text></g>
<g><circle cx="60" cy="155" r="35.56" fill="none" stroke="#000" stroke-width=".6" stroke-dasharray="2 1.2"/><line x1="24.44" y1="155" x2="95.56" y2="155" stroke="#000" stroke-width=".3"/><polygon points="24.44,155 27.4,154 27.4,156"/><polygon points="95.56,155 92.6,154 92.6,156"/><text x="60" y="152.5" font-size="3.2" text-anchor="middle">71 mm (2.8 in)</text>
<text x="60" y="198" font-size="3.6" font-weight="bold" text-anchor="middle">POLLEN ball, life size</text><text x="60" y="203" font-size="3.2" text-anchor="middle">Dashed circle: the size of one POLLEN.</text></g>
<g font-size="3.3"><text x="112" y="130" font-weight="bold" font-size="3.8">Numbers to remember</text>
<text x="112" y="137">Attachment length: 180 mm</text><text x="112" y="143">Attachment diameter: 30 mm</text><text x="112" y="149">Hex hole: 7 mm across flats</text><text x="112" y="155">POLLEN: 2.8 in (about 71 mm)</text><text x="112" y="161">Foam target: about 50 mm across</text><text x="112" y="167">Squeeze on the POLLEN: light, 2 to 3 mm</text><text x="112" y="173">Zip ties: 4 along the length</text></g>
</svg>'''

def fitsvg():
    # side view, looking along the roller. roller centre (0,H). ball on floor.
    return '''<svg viewBox="0 0 160 120" style="width:100%;height:100%">
<line x1="5" y1="110" x2="155" y2="110" stroke="#000" stroke-width="1"/><text x="150" y="116" font-size="4" text-anchor="end">Floor</text>
<circle cx="62" cy="74.4" r="35.6" fill="#ededed" stroke="#000" stroke-width=".7"/><text x="62" y="76" font-size="5" text-anchor="middle" font-weight="bold">POLLEN</text><text x="62" y="82" font-size="3.6" text-anchor="middle">2.8 in</text>
<circle cx="109" cy="30" r="25" fill="#cfcfcf" stroke="#000" stroke-width=".7"/><circle cx="109" cy="30" r="15" fill="#5c5c5c" stroke="#000" stroke-width=".5"/><polygon points="113,30 111,33.5 107,33.5 105,30 107,26.5 111,26.5" fill="#fff"/>
<circle cx="88" cy="46" r="7" fill="none" stroke="#000" stroke-width=".7" stroke-dasharray="1.5 1"/>
<text x="138" y="12" font-size="3.8">Foam</text><line x1="137" y1="12" x2="128" y2="17" stroke="#000" stroke-width=".4"/>
<text x="138" y="52" font-size="3.8">Attachment</text><line x1="137" y1="51" x2="118" y2="38" stroke="#000" stroke-width=".4"/>
<text x="100" y="68" font-size="3.8" font-weight="bold">Look here:</text><text x="100" y="73" font-size="3.6">foam touches and</text><text x="100" y="78" font-size="3.6">squeezes 2 to 3 mm</text><line x1="100" y1="66" x2="92" y2="51" stroke="#000" stroke-width=".4"/>
<path d="M 120 57 A 31 31 0 0 0 140 30" fill="none" stroke="#000" stroke-width=".8"/><polygon points="140,26 137.5,32 142.5,32"/><text x="143" y="44" font-size="3.6">spin</text>
<line x1="10" y1="74" x2="22" y2="74" stroke="#000" stroke-width="1.2"/><polygon points="26,74 21,71.5 21,76.5"/><text x="6" y="69" font-size="3.6">ball comes in</text>
</svg>'''

def layertable():
    return '''<table style="font-size:10pt"><tr><th>What you see</th><th>What to do</th></tr>
<tr><td>The POLLEN rolls under the foam and is not pulled in</td><td>Add one more layer of foam</td></tr>
<tr><td>The foam touches but slips on the POLLEN</td><td>Add half a layer, or pull the last layer tighter</td></tr>
<tr><td>The POLLEN gets stuck, or the motor slows down a lot</td><td>Take off one layer</td></tr>
<tr><td>The foam is thick on one end and thin on the other</td><td>Unwrap and wrap again, keeping the edges in line</td></tr>
<tr><td>The POLLEN comes in with a light squeeze</td><td>Good. Go to step 6</td></tr></table>'''

STEPS=[
 ('1a','Sort the parts','Step 1 of 7: Lay out the kit','Take the parts out of the kit and put them on a clean table.',
  [('Parts','1 FTC intake attachment, 1 foam sheet, zip ties'),('Size and position','Attachment: 180 mm long, 30 mm across, 7 mm hex hole'),('Which way','Any'),('Tip','Keep the foam flat. Do not fold it or cut it yet.')],'s1a.png','s1b_ci.png','Close-up: the 7 mm hex hole'),
 ('1b','Check the print','Step 1 of 7: Lay out the kit','Look at both ends and along the full length. The part must be straight and solid, with no gaps or loose strings in the hex hole.',
  [('Size and position','Length 180 mm. Diameter 30 mm. Hex hole 7 mm across flats, all the way through.'),('Which way','Look down the hex hole from one end. You should see light from the other end.'),('Tip','Stand the part on the life size circle on page 4 to check the size. It is printed at 100% infill, so it should feel heavy, about 150 g.')],'s2a.png','att_side.png','Side view: 180 mm long'),
 ('2a','Slide the attachment onto the hex shaft','Step 2 of 7: Mount the attachment','Take the intake hex shaft out of one side of the robot, or loosen it. Slide the attachment onto the shaft.',
  [('Parts','1 FTC intake attachment'),('Tools','The hex key for your intake shaft collars'),('Which way','Either end first. Both ends are the same.'),('Tip','If the shaft is tight, lightly sand the flats inside the hole. Do not make it loose, or it will spin on the shaft.')],'s3a.png','s3a_ci.png','Close-up: the shaft going into the hex hole'),
 ('2b','Centre it and lock it','Step 2 of 7: Mount the attachment','Put the shaft back in its bearings. Move the attachment to the centre of the intake. Lock it with the shaft collars or spacers already on your robot.',
  [('Size and position','Same gap on both sides, between the attachment and the side plates.'),('Which way','The attachment must not slide along the shaft.'),('Tip','Spin the shaft by hand. It should turn freely and the attachment should turn with it, with no slipping.')],'s3b.png','s3b_ci.png','Close-up: shaft collar at the end'),
 ('3a','Start the foam','Step 3 of 7: Start the foam wrap','Cut the foam to the same width as the attachment, 180 mm. Lay the first edge of the foam along the full length of the attachment and hold it with 3 short pieces of tape.',
  [('Parts','Foam, tape (not in the kit, any tape is fine here)'),('Size and position','Foam width: 180 mm, the same as the attachment. Keep the foam edge straight along the part.'),('Which way','Start the foam on the side that faces you.'),('Tip','Make sure the foam does not stick out past the ends. It can rub on the side plates.')],'s4a.png','','' ),
 ('3b','Make the first wrap','Step 3 of 7: Start the foam wrap','Turn the shaft the same way the intake spins. Let the foam wrap around the attachment. Pull it gently so it sits tight with no air gaps.',
  [('Size and position','One full turn is one layer.'),('Which way','Wrap in the same direction the intake spins. Then the loose end of the foam trails behind and does not peel open.'),('Tip','Keep the foam edges in line with the ends of the attachment on every turn.')],'s4b.png','',''),
 ('4a','Keep wrapping, layer by layer','Step 4 of 7: Build up the layers','Keep turning and wrapping. Each new layer goes straight on top of the last one. Keep the same gentle pull every time.',
  [('Size and position','Grow the diameter slowly. About 50 mm across is a good place to stop and test.'),('Which way','Same direction as step 3b.'),('Tip','Do not stretch the foam hard. Stretched foam gets thin and loses its grip.')],'s5a.png','s5_ci.png','Close-up: end view of the layers'),
 ('4b','Stop when the foam reaches the POLLEN','Step 4 of 7: Build up the layers','Hold one POLLEN on the floor in front of the intake. Keep adding layers until the foam just touches the top of the POLLEN.',
  [('Parts','1 POLLEN ball (2.8 in)'),('Size and position','The foam should reach the POLLEN at the height your intake sits.'),('Which way','Check in the middle and at both ends of the attachment.'),('Tip','Do not cut the foam yet. Hold the loose end with your hand or one piece of tape until the fit check is done.')],'s5b.png','',''),
 ('5a','Check the fit with a POLLEN','Step 5 of 7: POLLEN fit check','Roll one POLLEN slowly into the intake. Turn the shaft by hand. The foam should touch the POLLEN, grip it, and pull it in.',
  [('Parts','1 POLLEN ball'),('Size and position','The foam squeezes the POLLEN a little, about 2 to 3 mm. A light squeeze, not a hard push.'),('Which way','Roll the POLLEN in from the front, the way it will come in during a match.'),('Tip','Try the POLLEN at the left, the centre and the right of the intake.')],'SVG:fit','s6b.png','The foam just touches the POLLEN'),
 ('5b','Add or take off a layer','Step 5 of 7: POLLEN fit check','Use this table. Change one layer at a time and test again.',
  [('Tip','When the fit is good, cut the foam so the end sits flat. Cut it straight across, along the full 180 mm.')],'TABLE:layers','',''),
 ('6a','Zip tie the foam','Step 6 of 7: Secure the foam','Put 4 zip ties around the foam, spread along the length. Pull each one tight enough to hold the foam, but not so tight that it cuts deep into it.',
  [('Parts','4 zip ties'),('Size and position','About 25 mm and 75 mm from the centre on each side. Keep the last tie 10 to 15 mm in from each end.'),('Which way','Put one zip tie over the loose end of the foam so it cannot open.'),('Tip','Cut the tails flush. Turn the zip tie heads so they sit in different places around the roller, not all in one line.')],'s7a.png','s7a_ci.png','Close-up: one zip tie, tail cut flush'),
 ('6b','Tape the ends (optional)','Step 6 of 7: Secure the foam','If the foam ends lift up, wrap one turn of tape around each end of the foam.',
  [('Parts','Tape (not in the kit)'),('Size and position','About 15 mm wide, at each end of the foam.'),('Which way','Wrap the tape the same way the intake spins.'),('Tip','Put the zip ties on first, then the tape. Keep tape off the middle of the foam, where it touches the POLLEN.')],'s7b.png','',''),
 ('7a','Spin test','Step 7 of 7: Test','Run the intake motor at low power, then full power. Feed in POLLEN one at a time.',
  [('Size and position','Watch the foam. It must stay tight and must not wobble or rub the side plates.'),('Which way','The intake must pull the POLLEN in, not push it away. If it pushes away, reverse the motor in your code.'),('Tip','Stop the motor at once if anything comes loose.')],'s8a.png','',''),
 ('7b','Final check','Step 7 of 7: Test','Check every part one last time before you drive.',
  [('Check','Attachment locked, no slipping on the shaft. Foam tight, no loose end. 4 zip ties tight, tails cut. Nothing rubs the side plates.'),('Tip','Check the foam after every few matches. Foam wears down. Add a layer when the grip gets weak.')],'fin_iso2.png','',''),
]
MISTAKES=[
 ('Printing the attachment with low infill','It can crack around the hex hole. Always print at 100% infill.'),
 ('Hex hole too tight, so you hammer the shaft in','The part can split. Lightly sand the flats inside the hole instead.'),
 ('Hex hole sanded too much','The attachment spins on the shaft and does not grip. Print a new one.'),
 ('Attachment not locked with collars','It slides along the shaft and rubs a side plate. Lock it in step 2b.'),
 ('Wrapping the foam the wrong way','The loose end lifts and peels open when the intake spins. Wrap the same way the intake spins.'),
 ('Too much foam','The POLLEN gets stuck and the motor slows down or stalls. Take off one layer.'),
 ('Too little foam','The POLLEN rolls under the intake and is not pulled in. Add one layer.'),
 ('Foam wider than 180 mm','It rubs on the side plates. Trim it flush with the ends.'),
 ('Stretching the foam hard','It gets thin and loses grip. Use a gentle, even pull.'),
 ('Zip ties too tight','They cut deep grooves in the foam and the POLLEN catches on them. Pull just tight enough to hold.'),
 ('Zip tie tails left long','They hit the POLLEN and the robot. Cut them flush.'),
 ('Tape over the whole foam','Tape is slippery and the POLLEN slides. Only tape the ends.'),
 ('Skipping the POLLEN fit check','The intake may work on the table but not on the field. Always test with a real POLLEN at the real intake height.'),
 ('Not checking the foam during the event','Foam wears and gets loose. Check it after every few matches.'),
]
def info(rows): return '<table class="info">'+''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a,b in rows)+'</table>'
def stepblock(s):
    sid,title,sp,tx,rows,main,ci,cap=s
    if main=='SVG:fit': mainh=f'<div class="mi">{fitsvg()}</div>'
    elif main=='TABLE:layers': mainh=f'<div class="mi" style="border:none;align-items:flex-start;flex:1 1 100%">{layertable()}</div>'
    else: mainh=f'<div class="mi"><img src="{img(main)}" alt="{sid}"></div>'
    cih=f'<div class="ii"><img src="{img(ci,700)}" alt="close-up {sid}"><div class="cap">{cap}</div></div>' if ci else '<div class="ii"></div>'
    if main=='TABLE:layers': cih=''
    return f'<div class="sb"><div class="sh"><span class="ck"></span><span class="sid">{sid}</span><span class="st">{title}</span><span class="sp">{sp}</span></div><div class="tx">{tx}</div>{info(rows)}<div class="imgs">{mainh}{cih}</div></div>'
pages=[]
QR=qr(KITURL)
pages.append(f'''<section class="page cover"><div class="band"><h1>{TITLE}</h1><div class="sub">Prolabs Robotics. FTC Intake Upgrade Kit, for a goBILDA FTC robot with a hex shaft intake, 2026-27. Detailed assembly steps only.</div></div>
<div class="covimg"><div><img src="{img('fin_iso.png')}" alt="Finished intake">Finished intake</div><div><img src="{img('att_iso.png')}" alt="FTC intake attachment">FTC intake attachment</div></div>
<div class="note">The kit has 1 FTC intake attachment and foam. Wrap the foam until it reaches the POLLEN, then test with a real POLLEN.</div>
<div class="covrow"><div class="cred"><b>Created by:</b> Aarav J.<br><b>Collaborators:</b> R-Factor FRC<br><br>7 steps, 14 sub-steps.<br>Only the robot parts around the intake are shown.</div><div class="qrs"><div class="qr"><img src="{QR}" style="width:34mm;height:34mm;display:block"><div class="qrlab">Scan for the kit files on GitHub</div></div><div class="qr"><div class="qrbox" style="width:34mm;height:34mm">QR code<br>Link coming soon</div><div class="qrlab">Scan for testing videos</div></div></div></div></section>''')
checklist=''.join(f'<div><span class="b"></span>{s[0]} {s[1]}</div>' for s in STEPS)
pages.append(f'''<section class="page"><h2 class="sec">Before you start</h2><table class="legend"><tr><th>In the pictures</th><th>Meaning</th></tr>
<tr><td><svg width="40mm" height="9mm" viewBox="0 0 40 9"><rect x="1" y="1" width="38" height="7" fill="#5c5c5c" stroke="#000" stroke-width=".6"/></svg></td><td>Dark part: the part you add or move in this step</td></tr>
<tr><td><svg width="40mm" height="9mm" viewBox="0 0 40 9"><rect x="1" y="1" width="38" height="7" fill="#cfcfcf" stroke="#000" stroke-width=".6"/></svg></td><td>Mid grey: foam that is already wrapped</td></tr>
<tr><td><svg width="40mm" height="9mm" viewBox="0 0 40 9"><rect x="1" y="1" width="38" height="7" fill="#ededed" stroke="#8f8f8f" stroke-width=".6"/></svg></td><td>Light grey part: already on the robot, do not touch</td></tr>
<tr><td><svg width="40mm" height="9mm" viewBox="0 0 40 9"><line x1="2" y1="4.5" x2="31" y2="4.5" stroke="#000" stroke-width="2"/><polygon points="38,4.5 30,0.5 30,8.5"/></svg></td><td>Black arrow: move the part this way</td></tr>
<tr><td><svg width="40mm" height="9mm" viewBox="0 0 40 9"><circle cx="20" cy="4.5" r="3.8" fill="none" stroke="#000" stroke-width=".7" stroke-dasharray="1.5 1"/></svg></td><td>Dashed circle: look here</td></tr>
<tr><td style="font-weight:bold">Close-up box</td><td>A zoomed view of the same step</td></tr></table>
<div class="note small">The POLLEN decides when to stop wrapping. The foam should just touch the POLLEN and give it a light squeeze. Always test with a real POLLEN at the real intake height.</div>
<p class="small"><b>Directions.</b> Front means the side of the robot where the POLLEN comes in. Left and right are as seen from the front. All sizes are in mm. The POLLEN is 2.8 in (about 71 mm) across.</p>
<p class="small"><b>Your robot may look different.</b> The side plates and motor in the pictures are simple shapes. Use the hex shaft, bearings and collars already on your intake.</p>
<p class="small"><b>Hex shaft.</b> The attachment has a 7 mm hex hole (across flats). Check that your intake shaft fits before you start.</p>
<h2 class="sec" style="margin-top:2mm">Checklist</h2><div class="cl">{checklist}</div></section>''')
pages.append(f'''<section class="page"><h2 class="sec">Kit contents</h2><img class="kitimg" src="{img('s1a.png')}" alt="Kit contents">
<table><tr><th>Part</th><th>Qty</th><th>Size</th><th>Notes</th></tr>
<tr><td>FTC intake attachment</td><td>1</td><td>180 mm long, 30 mm across, 7 mm hex hole</td><td>3D print, 100% infill, about 150 g</td></tr>
<tr><td>Foam</td><td>1 sheet</td><td>180 mm wide</td><td>Wrapped around the attachment until it reaches the POLLEN</td></tr>
<tr><td>Zip ties</td><td>1 bag</td><td>2.5 mm wide</td><td>4 used to hold the foam. The rest are spares</td></tr></table>
<p class="small">One robot uses 1 attachment, enough foam to reach about 50 mm across (your POLLEN check decides), and 4 zip ties.</p>
<h2 class="sec" style="margin-top:4mm">Tools and things you need</h2>
<table><tr><th>Tool</th><th>Used for</th></tr><tr><td>Hex key for your shaft collars</td><td>Taking the shaft out and locking the attachment</td></tr><tr><td>Scissors or a sharp knife</td><td>Cutting the foam to 180 mm wide and cutting the end</td></tr><tr><td>Flush cutters</td><td>Trimming zip tie tails</td></tr><tr><td>Ruler (mm)</td><td>Measuring the foam and checking the print</td></tr><tr><td>Tape (any)</td><td>Holding the start of the foam, and the ends (optional)</td></tr><tr><td>1 POLLEN ball</td><td>The fit check in step 5</td></tr><tr><td>Fine sandpaper</td><td>Only if the hex hole is tight</td></tr></table>
<div class="note">Adults should handle the knife. Cut away from your hands.</div></section>''')
pages.append(f'''<section class="page"><h2 class="sec">The attachment and the POLLEN, life size</h2>{lifesize()}</section>''')
for i in range(0,len(STEPS),2):
    pages.append('<section class="page">'+''.join(stepblock(s) for s in STEPS[i:i+2])+'</section>')
rows=''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a,b in MISTAKES)
pages.append(f'<section class="page"><h2 class="sec">Common mistakes</h2><table style="font-size:10.5pt"><tr><th style="width:42%">Mistake</th><th>What happens, and the fix</th></tr>{rows}</table><div class="note">If the intake does not pull the POLLEN in, go back to step 5 and test again with a real POLLEN.</div></section>')
pages.append(f'''<section class="page"><h2 class="sec">Finished assembly</h2>
<div class="fin2"><div><img src="{img('fin_iso.png')}" alt="Finished, right"><div class="c">Finished intake, front right</div></div><div><img src="{img('fin_iso2.png')}" alt="Finished, left"><div class="c">Finished intake, front left</div></div></div>
<div class="fin2" style="margin-top:2mm"><div><img src="{img('s5_ci.png')}" alt="End view"><div class="c">End view: attachment and foam layers</div></div><div><img src="{img('s7a_ci.png')}" alt="Zip tie"><div class="c">Close-up: zip tie, tail cut flush</div></div></div>
<div class="note">Test with a real POLLEN before every event. Check the foam and the zip ties after every few matches.</div>
<div class="covrow"><div class="cred small">Print files: github.com/Aarav-111/FTC-India-Resources (FTC Kits/Intake Upgrade Kit). Print every part at 100% infill.<br>Contact: ProlabsRobotics@gmail.com<br>Created by Aarav J. Collaborators: R-Factor FRC.</div><div class="qrs"><div class="qr"><img src="{QR}" style="width:30mm;height:30mm;display:block"><div class="qrlab">Scan for the kit files on GitHub</div></div></div></div></section>''')
N=len(pages)
pages=[p.replace('</section>',f'<div class="foot">{TITLE}  |  Page {k+1} of {N}</div></section>',1) if True else p for k,p in enumerate(pages)]
html=f'<!doctype html><html><head><meta charset="utf-8"><title>{TITLE}</title><style>{CSS}</style></head><body>\n'+'\n'.join(pages)+'</body></html>'
open(OUTDIR+'Intake Assembly Guide.html','w').write(html)
subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--no-pdf-header-footer','--print-to-pdf='+os.path.abspath(OUTDIR+'Intake Assembly Guide.pdf'),'file://'+os.path.abspath(OUTDIR).replace(' ','%20')+'/Intake%20Assembly%20Guide.html'],check=True,stderr=subprocess.DEVNULL)
print('pages',N)
