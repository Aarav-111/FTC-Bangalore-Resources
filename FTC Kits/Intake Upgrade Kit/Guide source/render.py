import pyvista as pv, trimesh, numpy as np
import os; OUT='img/'; os.makedirs(OUT,exist_ok=True)
DARK='#5c5c5c'; LIGHT='#ededed'; MID='#a8a8a8'; FOAM='#cfcfcf'
att=trimesh.load('../FTC Intake Attachment.stl')
c=att.bounds.mean(0); att.apply_translation(-c)
att.apply_transform(trimesh.transformations.rotation_matrix(-np.pi/2,[0,0,1]))  # y->x
ATT=pv.wrap(att)
L=180; R0=15; BALL=71.12/2
def P(ws=(1400,1050)):
    p=pv.Plotter(off_screen=True,window_size=ws); p.set_background('white'); p.enable_anti_aliasing('ssaa'); return p
def add(p,m,col,op=1.0,edge=True):
    p.add_mesh(m,color=col,opacity=op,smooth_shading=True,specular=0.15,ambient=0.25)
    if edge and op>0.5:
        try: p.add_mesh(m.extract_feature_edges(40,boundary_edges=True,non_manifold_edges=False,manifold_edges=False),color='black',line_width=2)
        except Exception: pass
def shell(r_in,r_out,length,x0=0,res=96,ang=360):
    if ang>=360:
        m=trimesh.creation.annulus(r_min=r_in,r_max=r_out,height=length,sections=res)
    else:
        # partial wrap
        th=np.radians(np.linspace(0,ang,max(8,int(res*ang/360))))
        pts=[];faces=[]
        n=len(th)
        for i,t in enumerate(th):
            for r in (r_in,r_out):
                for z in (-length/2,length/2): pts.append([r*np.cos(t),r*np.sin(t),z])
        pts=np.array(pts)
        def q(a,b,c_,d): faces.extend([[a,b,c_],[a,c_,d]])
        for i in range(n-1):
            a=4*i;b=4*(i+1)
            q(a+2,b+2,b+3,a+3)  # outer
            q(a,a+1,b+1,b)      # inner
            q(a,b,b+2,a+2)      # bottom
            q(a+1,a+3,b+3,b+1)  # top
        q(0,2,3,1); e=4*(n-1); q(e,e+1,e+3,e+2)
        m=trimesh.Trimesh(pts,np.array(faces),process=True); m.fix_normals()
    m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[0,1,0])); m.apply_translation([x0,0,0])
    return pv.wrap(m)
def zt(x,r):  # zip tie band around radius r at position x
    m=trimesh.creation.annulus(r_min=r,r_max=r+1.3,height=2.5,sections=96); m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[0,1,0])); m.apply_translation([x,0,0])
    head=trimesh.creation.box([5,6,4]); head.apply_translation([x,0,r+2.5])
    tail=trimesh.creation.box([2.5,12,1]); tail.apply_translation([x,-8,r+3.5])
    return pv.wrap(trimesh.util.concatenate([m,head,tail]))
def shaft(ext=60):
    m=trimesh.creation.cylinder(radius=7/np.sqrt(3)*0.98,height=L+2*ext,sections=6); m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[0,1,0]))
    m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0]))
    return pv.wrap(m)
def frame():
    out=[]
    for s in (-1,1):
        b=trimesh.creation.box([6,48,120]); b.apply_translation([s*(L/2+18),0,-20]); out.append(b)
        bb=trimesh.creation.cylinder(radius=7,height=8,sections=32); bb.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[0,1,0])); bb.apply_translation([s*(L/2+12),0,0]); out.append(bb)
    mot=trimesh.creation.cylinder(radius=18,height=70,sections=48); mot.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[0,1,0])); mot.apply_translation([L/2+56,0,0]); out.append(mot)
    return pv.wrap(trimesh.util.concatenate(out))
def collar(x):
    m=trimesh.creation.annulus(r_min=4,r_max=8,height=6,sections=48); m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[0,1,0])); m.apply_translation([x,0,0]); return pv.wrap(m)
def foamstrip(w=L,t=3.5,length=300,y0=-60):
    m=trimesh.creation.box([w,length,t]); m.apply_translation([0,y0-length/2,t/2-R0-4]); return pv.wrap(m)
def arrow(p,a,b,col='black'):
    a=np.array(a,float);b=np.array(b,float);d=b-a;n=np.linalg.norm(d)
    p.add_mesh(pv.Arrow(start=a,direction=d/n,scale=n,tip_length=0.25,tip_radius=0.08,shaft_radius=0.03),color=col)
def ring(p,ctr,r):
    p.add_mesh(pv.Circle(radius=r,resolution=60).translate(ctr).extract_feature_edges(),color='black',line_width=4)
def cam(p,pos,foc=None,up=(0,0,1),zoom=1.0):
    if foc is None:
        p.camera_position=[pos,(0,0,0),up]; p.reset_camera(); p.camera.zoom(zoom)
    else:
        p.camera_position=[pos,foc,up]; p.reset_camera_clipping_range(); p.camera.zoom(zoom)
def label(p,pts,txt,size=26):
    p.add_point_labels(np.array(pts,float),txt,font_size=size,point_size=1,point_color='black',shape_color='white',shape_opacity=1,text_color='black',always_visible=True,margin=5,show_points=False)
def save(p,n): p.screenshot(OUT+n); p.close(); print(n,flush=True)
ISO=(260,-420,260)
def ball(ctr): return pv.Sphere(radius=BALL,center=ctr,theta_resolution=60,phi_resolution=60)

# previews of the attachment alone
p=P(); add(p,ATT,DARK); cam(p,ISO,zoom=1.2); save(p,'att_iso.png')
p=P((1000,1000)); add(p,ATT,DARK); cam(p,(400,0,0),(0,0,0),zoom=1.0); p.camera.view_angle=8; save(p,'att_end.png')
p=P((1600,600)); add(p,ATT,DARK); cam(p,(0,-500,0),zoom=1.3); save(p,'att_side.png')

# 1a kit layout
p=P(); add(p,ATT.translate([0,40,0]),DARK); add(p,foamstrip(y0=-10),FOAM)
for i in range(6):
    m=trimesh.creation.box([150,2.5,1.2]); m.apply_translation([0,-370-i*8,-18]); add(p,pv.wrap(m),'#333333',edge=False)
label(p,[[0,40,25],[0,-180,-5],[60,-400,-15]],['1 x FTC intake attachment','Foam','Zip ties'])
cam(p,(250,-600,450),zoom=1.15); save(p,'s1a.png')
# 1b close-up hex hole
p=P((900,900)); add(p,ATT,DARK); cam(p,(L/2+90,-50,45),(L/2,0,0),zoom=1.0); save(p,'s1b_ci.png')
# 2a check print: end view with dims
p=P((1000,1000)); add(p,ATT,DARK); cam(p,(400,0,0),(0,0,0),zoom=1.0); p.camera.view_angle=8; save(p,'s2a.png')
# 3a slide shaft through
p=P(); add(p,frame(),LIGHT); add(p,shaft().translate([-120,0,0]),MID); add(p,ATT,DARK); arrow(p,(-L/2-150,0,40),(-L/2-40,0,40)); cam(p,ISO,zoom=1.1); save(p,'s3a.png')
p=P((900,900)); add(p,shaft().translate([-120,0,0]),MID); add(p,ATT,DARK); cam(p,(-L/2-110,-110,60),(-L/2-10,0,0),zoom=1.0); save(p,'s3a_ci.png')
# 3b centred + collars
p=P(); add(p,frame(),LIGHT); add(p,shaft(),MID); add(p,ATT,DARK); add(p,collar(-L/2-4),'#333333'); add(p,collar(L/2+4),'#333333'); ring(p,(0,0,0),1) ; cam(p,ISO,zoom=1.1); save(p,'s3b.png')
p=P((900,900)); add(p,shaft(),MID); add(p,ATT,LIGHT); add(p,collar(L/2+4),DARK); cam(p,(L/2+90,-90,50),(L/2,0,0),zoom=1.0); save(p,'s3b_ci.png')
# 4a tape the foam start
p=P(); add(p,frame(),LIGHT,edge=False); add(p,shaft(),LIGHT); add(p,ATT,MID); add(p,shell(R0,R0+3.5,L,ang=40),DARK)
for x in (-70,0,70):
    t=trimesh.creation.box([20,1,30]); t.apply_translation([x,-R0-3.5,8]); add(p,pv.wrap(t),'#222222',edge=False)
cam(p,(150,-420,200),zoom=1.2); save(p,'s4a.png')
# 4b first wrap
p=P(); add(p,frame(),LIGHT,edge=False); add(p,shaft(),LIGHT); add(p,ATT,MID); add(p,shell(R0,R0+3.5,L,ang=300),DARK); cam(p,(150,-420,200),zoom=1.2); save(p,'s4b.png')
# 5a layers - section view
for k,n in ((1,'s5a.png'),(3,'s5b.png')):
    p=P(); add(p,frame(),LIGHT,edge=False); add(p,shaft(),LIGHT); add(p,ATT,MID)
    for i in range(k): add(p,shell(R0+3.5*i,R0+3.5*(i+1),L),FOAM if i<k-1 else DARK)
    cam(p,(150,-420,200),zoom=1.2); save(p,n)
# 5 end view close-up of layers
p=P((900,900)); add(p,ATT,MID)
for i in range(3): add(p,shell(R0+3.5*i,R0+3.5*(i+1),L),[FOAM,'#bbbbbb',DARK][i])
cam(p,(400,0,0),(0,0,0),zoom=1.0); p.camera.view_angle=11; save(p,'s5_ci.png')
# 6a POLLEN fit check side view (looking along axis)
R=R0+10
H=80; dz=H-BALL; dist=R+BALL-3; dy=np.sqrt(dist**2-dz**2)
p=P(); add(p,frame(),LIGHT,edge=False); add(p,ATT.translate([0,0,H]),MID); add(p,shell(R0,R,L).translate([0,0,H]),DARK)
add(p,ball((0,-dy,BALL)),'#e0e0e0'); fl=pv.Plane(center=(0,-40,0),direction=(0,0,1),i_size=400,j_size=300); p.add_mesh(fl,color='#f4f4f4')
cam(p,(500,-120,90),(0,-40,60),zoom=1.4); save(p,'s6a.png')
p=P(); add(p,ATT.translate([0,0,H]),MID); add(p,shell(R0,R,L).translate([0,0,H]),DARK); add(p,ball((0,-dy,BALL)),'#e0e0e0'); add(p,ball((-60,-dy-5,BALL)).translate([0,0,0]),'#e0e0e0',op=0.0)
p.add_mesh(fl,color='#f4f4f4'); cam(p,(220,-420,220),(0,-40,60),zoom=1.3); save(p,'s6b.png')
# 7a zip ties
p=P(); add(p,frame(),LIGHT,edge=False); add(p,shaft(),LIGHT); add(p,shell(R0,R,L),FOAM)
for x in (-75,-25,25,75): add(p,zt(x,R),'#222222',edge=False)
cam(p,(150,-420,200),zoom=1.2); save(p,'s7a.png')
p=P((900,900)); add(p,shell(R0,R,L),FOAM); add(p,zt(75,R),'#222222',edge=False); cam(p,(110,-70,90),(75,0,R/2),zoom=1.0); save(p,'s7a_ci.png')
# 7b tape ends
p=P(); add(p,frame(),LIGHT,edge=False); add(p,shaft(),LIGHT); add(p,shell(R0,R,L),FOAM)
for x in (-75,-25,25,75): add(p,zt(x,R),'#555555',edge=False)
for x in (-L/2+8,L/2-8): add(p,shell(R,R+0.6,16,x0=x),DARK)
cam(p,(150,-420,200),zoom=1.2); save(p,'s7b.png')
# 8 spin test
p=P(); add(p,frame(),LIGHT,edge=False); add(p,shaft(),LIGHT); add(p,shell(R0,R,L).translate([0,0,H]) if False else shell(R0,R,L),DARK)
for x in (-75,-25,25,75): add(p,zt(x,R),'#222222',edge=False)
add(p,ball((0,-dist,-0)),'#e0e0e0'); arrow(p,(0,-dist-120,0),(0,-dist-45,0)); cam(p,ISO,zoom=1.0); save(p,'s8a.png')
# finished
p=P(); add(p,frame(),LIGHT); add(p,shaft(),MID); add(p,collar(-L/2-4),'#333333'); add(p,collar(L/2+4),'#333333'); add(p,shell(R0,R,L),FOAM)
for x in (-75,-25,25,75): add(p,zt(x,R),'#222222',edge=False)
cam(p,ISO,zoom=1.1); save(p,'fin_iso.png')
p=P(); add(p,frame(),LIGHT); add(p,shaft(),MID); add(p,shell(R0,R,L),FOAM)
for x in (-75,-25,25,75): add(p,zt(x,R),'#222222',edge=False)
cam(p,(-260,-420,160),zoom=1.1); save(p,'fin_iso2.png')
