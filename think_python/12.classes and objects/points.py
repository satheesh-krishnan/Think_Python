import math
class point(object):
    "points in plane"
def dist(s,t):
    d=t.x-s.x
    e=t.y-s.x
    f=math.sqrt(d**2+e**2)
    print f
def main():
    a=point()
    b=point()
    print 'enter x'
    a.x=raw_input()
    b.x=raw_input()
    print 'enter y'
    a.y=raw_input()
    b.y=raw_input()
    a.x=float(a.x)
    a.y=float(a.y)
    b.x=float(b.x)
    b.y=float(b.y)
    dist(a,b)




main()
