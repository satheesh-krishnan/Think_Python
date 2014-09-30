import time
def makelist():
    t=dict()
    a=dict()
    s=open('date.txt')
    for w in s:
        # w=line.strip(line)
        f=t.get(w,0)        
        t[w]=f+1
        if t[w]>1:
            a[w]=t[w]
            
    print 'original dictionary',t
    return a
#def duplicates(t):
    #a=dict()
    #for i in t:
       # if t[i]>1:
        #    a[i]=t[i]
    #return a
start=time.time()
f=makelist()
finish=time.time()-start
print 'filtered dictionary',f
print finish,'seconds'
