# Run render_chassis.py first (makes img/), then make_chassis_guide.py (makes out/).
# Renders simple goBILDA-style mecanum chassis pictures for the Mecanum Chassis Guide (Prolabs Robotics).
import os, numpy as np, trimesh, pyvista as pv
OUT='img/'; os.makedirs(OUT,exist_ok=True)
DARK='#5c5c5c'; LIGHT='#ededed'; MID='#a8a8a8'; BLACK='#2b2b2b'
T=trimesh.transformations
# frame sizes (mm)
SIDE_L=384; CROSS_L=288; CH=48; XS=CROSS_L/2+CH/2   # side channel centre x
YC=SIDE_L/2-CH/2                                   # cross channel centre y
WY=120                                             # wheel centre y (front/back)
WR=52; WW=46; WX=XS+CH/2+6+WW/2                    # wheel centre x
def P(ws=(1400,1050)):
    p=pv.Plotter(off_screen=True,window_size=ws); p.set_background('white'); p.enable_anti_aliasing('ssaa'); return p
def add(p,m,col,op=1.0,edge=True):
    m=pv.wrap(m) if not isinstance(m,pv.DataSet) else m
    p.add_mesh(m,color=col,opacity=op,smooth_shading=False,specular=0.1,ambient=0.3)
    if edge and op>0.5:
        try: p.add_mesh(m.extract_feature_edges(35,boundary_edges=False,non_manifold_edges=False),color='black',line_width=1.5)
        except Exception: pass
def uchan(length,axis):
    # U-channel 48x48, open side up, length along axis ('x' or 'y'), centred at origin
    w=CH; t=2.5
    parts=[trimesh.creation.box([w,length,t]).apply_translation([0,0,-w/2+t/2]) if False else None]
    base=trimesh.creation.box([w,length,t]); base.apply_translation([0,0,-w/2+t/2])
    s1=trimesh.creation.box([t,length,w]); s1.apply_translation([-w/2+t/2,0,0])
    s2=trimesh.creation.box([t,length,w]); s2.apply_translation([w/2-t/2,0,0])
    m=trimesh.util.concatenate([base,s1,s2])
    # holes as small dark discs drawn later is costly; skip
    if axis=='x': m.apply_transform(T.rotation_matrix(np.pi/2,[0,0,1]))
    return m
def frame(cross=True,sides=True):
    out=[]
    if sides:
        for s in (-1,1):
            m=uchan(SIDE_L,'y'); m.apply_translation([s*XS,0,0]); out.append(m)
    if cross:
        for s in (-1,1):
            m=uchan(CROSS_L,'x'); m.apply_translation([0,s*YC,0]); out.append(m)
    return out
def motor(sx,sy):
    body=trimesh.creation.cylinder(radius=18,height=116,sections=40); body.apply_transform(T.rotation_matrix(np.pi/2,[0,1,0]))
    body.apply_translation([sx*(XS-CH/2-58),sy*WY,0]); return body
def mount(sx,sy):
    b=trimesh.creation.box([4,48,48]); b.apply_translation([sx*(XS-CH/2-2),sy*WY,0]); return b
def shaft(sx,sy):
    m=trimesh.creation.cylinder(radius=4,height=CH+WW+30,sections=6); m.apply_transform(T.rotation_matrix(np.pi/2,[0,1,0]))
    m.apply_translation([sx*(XS+ (WW+30)/2 - 4),sy*WY,0]); return m
def bearing(sx,sy,x):
    m=trimesh.creation.annulus(r_min=4.2,r_max=8,height=6,sections=40); m.apply_transform(T.rotation_matrix(np.pi/2,[0,1,0])); m.apply_translation([sx*x,sy*WY,0]); return m
def outer_plate(sx,sy):
    b=trimesh.creation.box([4,60,60]); b.apply_translation([sx*(WX+WW/2+8),sy*WY,0]); return b
def standoffs(sx,sy):
    out=[]
    for dy in (-24,24):
        for dz in (-24,24):
            c=trimesh.creation.cylinder(radius=3,height=WW+18,sections=12); c.apply_transform(T.rotation_matrix(np.pi/2,[0,1,0]))
            c.apply_translation([sx*(XS+CH/2+(WW+18)/2),sy*WY+dy*1.25,dz*1.25]); out.append(c)
    return out
def wheel(sx,sy,h=None):
    # hub + 11 rollers at 45 degrees. h = handedness. X pattern from above: h = sx*sy
    if h is None: h=sx*sy
    parts=[]
    hub=trimesh.creation.cylinder(radius=34,height=WW-6,sections=48); hub.apply_transform(T.rotation_matrix(np.pi/2,[0,1,0])); parts.append(hub)
    for side in (-1,1):
        d=trimesh.creation.cylinder(radius=44,height=3,sections=48); d.apply_transform(T.rotation_matrix(np.pi/2,[0,1,0])); d.apply_translation([side*(WW/2-1.5),0,0]); parts.append(d)
    c=np.cos(np.pi/4); s=np.sin(np.pi/4)
    for k in range(11):
        th=2*np.pi*k/11
        pos=np.array([0,WR*0.86*np.cos(th),WR*0.86*np.sin(th)])
        tan=np.array([0,-np.sin(th),np.cos(th)])
        ax=c*np.array([1,0,0]) - h*s*tan
        r=trimesh.creation.capsule(height=WW*1.0,radius=7.5,count=[10,10])
        # capsule along z -> align to ax
        R=trimesh.geometry.align_vectors([0,0,1],ax); r.apply_transform(R); r.apply_translation(pos); parts.append(r)
    m=trimesh.util.concatenate(parts); m.apply_translation([sx*WX,sy*WY,0]); return m
def hub_battery():
    hubm=trimesh.creation.box([103,143,15]); hubm.apply_translation([0,-40,32])
    bat=trimesh.creation.box([80,150,40]); bat.apply_translation([0,70,10])
    return hubm,bat
def cam(p,pos,foc=(0,0,0),up=(0,0,1),zoom=1.0,reset=True):
    p.camera_position=[pos,foc,up]
    if reset: p.reset_camera()
    p.camera.zoom(zoom)
def label(p,pts,txt,size=24):
    p.add_point_labels(np.array(pts,float),txt,font_size=size,point_size=1,shape_color='white',shape_opacity=1,text_color='black',always_visible=True,margin=5,show_points=False)
def arrow(p,a,b):
    a=np.array(a,float);b=np.array(b,float);d=b-a;n=np.linalg.norm(d)
    p.add_mesh(pv.Arrow(start=a,direction=d/n,scale=n,tip_length=0.25,tip_radius=0.08,shaft_radius=0.03),color='black')
def save(p,n): p.screenshot(OUT+n); p.close(); print(n,flush=True)
ISO=(700,-900,650); C=[(sx,sy) for sx in (-1,1) for sy in (-1,1)]
def full(p,hl=(),wheels=True,motors=True,hubbat=True,plates=True,whcol=None,h_override=None):
    for m in frame(): add(p,m,DARK if 'frame' in hl else LIGHT)
    for sx,sy in C:
        if motors:
            add(p,motor(sx,sy),DARK if 'motor' in hl else MID); add(p,mount(sx,sy),DARK if 'motor' in hl else LIGHT)
        add(p,shaft(sx,sy),BLACK,edge=False)
        if plates:
            for m in standoffs(sx,sy): add(p,m,DARK if 'plate' in hl else LIGHT,edge=False)
            add(p,outer_plate(sx,sy),DARK if 'plate' in hl else LIGHT)
            add(p,bearing(sx,sy,WX+WW/2+8),BLACK,edge=False)
        if wheels:
            h=None if h_override is None else h_override*sx*sy
            add(p,wheel(sx,sy,h),whcol or (DARK if 'wheel' in hl else MID))
    if hubbat:
        hb,bt=hub_battery(); add(p,hb,DARK if 'hub' in hl else LIGHT); add(p,bt,DARK if 'hub' in hl else LIGHT)
# cover
p=P(); full(p); cam(p,ISO,zoom=1.15); label(p,[[0,SIDE_L/2+30,30]],['FRONT']); save(p,'cover.png')
# step 1a side rails
p=P()
for m in frame(cross=False): add(p,m,DARK)
label(p,[[XS,0,40],[-XS,0,40]],['384 mm U-channel','384 mm U-channel']); cam(p,ISO,zoom=1.1); save(p,'s1a.png')
# 1b cross channels
p=P()
for m in frame(cross=False): add(p,m,LIGHT)
for m in frame(sides=False): add(p,m,DARK)
p.add_mesh(pv.Line((-XS,-YC,30),(XS,YC,30)),color='black',line_width=3); p.add_mesh(pv.Line((XS,-YC,30),(-XS,YC,30)),color='black',line_width=3)
label(p,[[0,YC,40],[60,30,40]],['288 mm U-channel','Measure both diagonals']); cam(p,(0,-200,1200),zoom=1.1); save(p,'s1b.png')
# 2a motors
p=P(); [add(p,m,LIGHT) for m in frame()]
for sx,sy in C: add(p,motor(sx,sy),DARK); add(p,mount(sx,sy),DARK); add(p,shaft(sx,sy),BLACK,edge=False)
cam(p,ISO,zoom=1.1); save(p,'s2a.png')
p=P((900,900)); [add(p,m,LIGHT) for m in frame()]; add(p,motor(1,1),DARK); add(p,mount(1,1),DARK); add(p,shaft(1,1),BLACK,edge=False)
cam(p,(XS+260,WY-260,200),(XS,WY,0),zoom=1.0,reset=False); p.reset_camera_clipping_range(); save(p,'s2a_ci.png')
# 2b top view motor lines
p=P(); [add(p,m,LIGHT) for m in frame()]
for sx,sy in C: add(p,motor(sx,sy),DARK); add(p,shaft(sx,sy),BLACK,edge=False)
for sy in (-1,1): p.add_mesh(pv.Line((-WX-60,sy*WY,40),(WX+60,sy*WY,40)),color='black',line_width=2)
cam(p,(0,0,1500),up=(0,1,0),zoom=1.2); save(p,'s2b.png')
# 3a bearings and spacers close-up exploded
p=P(); [add(p,m,LIGHT) for m in frame()]; add(p,motor(1,-1),MID); add(p,shaft(1,-1),BLACK,edge=False)
for m in standoffs(1,-1): add(p,m.copy().apply_translation([0,0,0]),DARK,edge=False)
pl=outer_plate(1,-1); pl.apply_translation([60,0,0]); add(p,pl,DARK); b=bearing(1,-1,WX+WW/2+8); b.apply_translation([60,0,0]); add(p,b,BLACK,edge=False)
arrow(p,(WX+WW/2+120,-WY,60),(WX+WW/2+40,-WY,60))
label(p,[[WX+70,-WY,50],[WX,-WY-40,-40]],['Bearing in outer plate','Spacers (standoffs)'])
cam(p,(XS+500,-WY-500,300),(XS+60,-WY,0),zoom=1.0,reset=False); p.reset_camera_clipping_range(); save(p,'s3a.png')
# 3b wheels on
p=P(); full(p,hl=('wheel',),hubbat=False); cam(p,ISO,zoom=1.1); save(p,'s3b.png')
p=P((900,900)); full(p,hl=('wheel',),hubbat=False); cam(p,(WX+300,WY-300,250),(WX,WY,0),zoom=1.0,reset=False); p.reset_camera_clipping_range(); save(p,'s3b_ci.png')
# 4a top view X pattern
p=P(); full(p,hl=('wheel',),hubbat=False,plates=False); cam(p,(0,0,1500),up=(0,1,0),zoom=1.2); label(p,[[0,SIDE_L/2+20,60]],['FRONT']); save(p,'top_X.png')
p=P(); full(p,hl=('wheel',),hubbat=False,plates=False,h_override=-1); cam(p,(0,0,1500),up=(0,1,0),zoom=1.2); label(p,[[0,SIDE_L/2+20,60]],['FRONT']); save(p,'top_O.png')
# 4b hub and battery
p=P(); full(p,hl=('hub',)); label(p,[[0,-40,50],[0,70,40]],['Control Hub','Battery']); cam(p,ISO,zoom=1.1); save(p,'s4b.png')
# finished views
p=P(); full(p); cam(p,(-700,-900,500),zoom=1.15); save(p,'fin2.png')
p=P(); full(p); cam(p,(0,-1200,250),zoom=1.2); save(p,'front.png')
