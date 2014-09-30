def istriangle(a,b,c):
    d=a+b
    print d
    e=a+c
    f=b+c
    if d <= c or e <=b or f<=a:
        print 'no'
    else:
        print 'yes'

s=raw_input('enter the three sides\n')
s=int(s)
r=raw_input()
r=int(r)
t=raw_input()
t=int(t)
istriangle(s,r,t)

