def bisect(a,b):
    c=len(a)
    d=c
    q=0
    r=c
    j=0
    c=c/2
    while j<d/2:
        if a[c]==b:
            return c+1
        elif a[c]>b:
            r=c
            c=(q+c)/2
            j=j+1
        elif a[c]<b:
            q=c
            c=(c+r)/2
            j=j+1
    return 'none'
n=(3,5,8,12,16,18,20,22,23,31,32,34,37,40,45,55,56,62,67,68,71,73,87,94,99,102,104,106,112)
o=raw_input('enter search number\n')
o=int(o)
p=bisect(n,o)
print 'position',p     
         
        
        
