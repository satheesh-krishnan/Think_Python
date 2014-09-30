from Tkinter import *
from swampy.World import World
def drawrect(can,rec,col):
    can.rectangle(rec,outline='green',width=5,fill=col)
    
def drawpoint(can,point):
    can.rectangle(point,outline='white',fill='white')
    
def czhech(can):
    can.polygon([[-50,-50],[100,-50],[100,10],[10,10]],fill='red')
    can.polygon([[10,10],[100,10],[100,70],[-50,70]],fill='white')
    can.polygon([[-50,-50],[10,10],[-50,70]],fill='blue')
    world.mainloop()
    
world=World()
col='black'
can=world.ca(width=500,height=400,background='black')
rec=[[-100,-100],[100,100]]
point=[[150,150],[150,150]]
#drawrect(can,rec,col)
#drawpoint(can,point)
czhech(can)
