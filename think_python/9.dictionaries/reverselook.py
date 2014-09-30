from histogram import *
def rev(s,v):
     a=[]
     for b in s:
         if s[b]==v:
             a.append(b)
     
     if len(a)==0:
         return 'none'
     else:
         return a
g='gdghdtghfgfhhj'
h=histogram(g)

i=rev(h,4)
print i
    


