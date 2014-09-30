import time
def makelist():
    t=[]
    s=open('date.txt')
    for line in s:
       # w=line.strip(line)
                
        t.append(line)
    print 'original list',t
    
    s=t
    s.sort()
    return s
def duplicates(t):
    m=0
    a=[]
    z=1 
    n=len(t)
    while z!=n:
         
        while t[m]==t[z]:
            if z-m>1:
                
                z=z+1
            else:
                a.append(t[m])
                 
                z=z+1

        m=z
        z=m+1
    return a  
start=time.time()   
f=makelist()
g=duplicates(f)
finish=time.time()-start
print 'filtered list',g
print finish,'seconds'
