from visual import *

scene.range = (256, 256, 256)
scene.center = (128, 128, 128)
u=0
v=0
w=0
#color=(0.1,0.1,0.9)

#sphere(pos=scene.center, radius=128, color=color)
t =range(0, 256, 51)
for x in t:
    u=u+0.1
    if u>1.0:
        u=0.0
          
    for y in t:
        v=0.1+v
        if v>1.0:
            v=0.0
        
        for z in t:
            w=0.1+w
            if w>1.0:
                w=0.0
            pos = x, y, z
            print u,v,w
            color=(u,v,w)
            sphere(pos=pos, radius=10, color=color)

