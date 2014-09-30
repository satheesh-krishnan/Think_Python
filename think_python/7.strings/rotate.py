def rotateword(x,y):
    a='abcdefghijklmnopqrstuvwxyz'
    r=''
    for c in x:
        d=ord(c)
        n=d-97
        e=(n+y)%26
        r +=a[e]
    return r    
f=raw_input('enter the string and number\n')
g=raw_input()
g=int(g)
p=rotateword(f,g)
print p
        
        
