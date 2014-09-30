def pri(a, b, z):
    print ((a+b*4)*2+a)+(b*4+a+b*4+a)*z
def plus(m):
    c='+'
    d='-'
    pri(c,d,m)
def sl(n):
    e ='/'
    f=' ' 
    pri(e,f,n)
    pri(e,f,n)
def twice(y):
    sl(y)
    sl(y)
    plus(y)
def four(r):
    twice(r)
    twice(r)
s=0
plus(s)     
four(s)
s=1
plus(s)
four(s)
four(s)
















