def estpi():
     import math
     #p=9
     t=0
     k=0
     m=0
     c=1
     f=1
     a=2*(math.sqrt(2))/9801
     while True:
           t=4*k
           b=t
           c=t 
           
           while True:
                if b==1:
                     
                     break
                if b==0:
                      
                      c=1
                      break
                c=(b-1)*c
                
                b=b-1
                
                
               
       
           d=26390*k+1103
           v=k
           e=v
           f=v
           while True:
                
                
                if e==1:
                    break
                if e==0:
                    f=1
                    break
                f=(e-1)*f
                
                e=e-1
               
           
           w=f**4 
           g=4*k
           h=396**g
           z=w*h
           i=c*d
           l=i/z
           m=m+l
           k=k+1
           #p=p-1
           if l<0.000000000000015:
                  break 
     n=a*m
     return n
           
o=estpi()
q=1/o
q=float(q)
print q

         
