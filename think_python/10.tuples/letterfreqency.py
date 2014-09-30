
def freq():
    v=tuple()
    o=[]
    g=[]
    l=dict()
    w=open('words.txt')
    for line in w:
        line=line.strip()
        s=line
        for r in s:
             b=l.get(r,0)
             l[r]=b+1
    t=l.items()
    for k in t:
       v=k[:]
       o.append(v[1])
    o.sort(reverse=True)
    for p in o:
        for d in t:
            if p==d[1]:
                 g.append(d)
                 t.remove(d)
                 break
    return g
s=freq()
print s      
    
    
