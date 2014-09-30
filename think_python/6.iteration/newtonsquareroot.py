def squareroot(a):
    x=a/2
    
    epsilon=0.0005
    while True:
        y=(x+a/x)/2
        if x==y or abs(y-x)<epsilon:
              return y
              break
        else:
               x=y
n=raw_input('enter a\n')
n=float(n)
m=squareroot(n)
print m

