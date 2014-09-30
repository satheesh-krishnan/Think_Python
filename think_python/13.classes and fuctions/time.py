class time(object):
    "time of the day without if"
def tim(x,y):
    s=(3600*x.h+60*x.m+x.s)-(3600*y.h+60*y.m+y.s)
    t=89999
    u=(t+s)/t
    v=1-u
    d='true'
    e='false'
    print d*u+e*v
    
def main(): 
    a=time()
    b=time()
    a.h=raw_input('enter time one\n')
    a.m=raw_input()
    a.s=raw_input()
    a.h=int(a.h)
    a.m=int(a.m)
    a.s=int(a.s)
    b.h=raw_input('enter time two\n')
    b.m=raw_input()
    b.s=raw_input()
    b.h=int(b.h)
    b.m=int(b.m)
    b.s=int(b.s)
    tim(a,b)
main()
    
        
