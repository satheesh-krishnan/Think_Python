def ack(m,n):
     
     if m==0:
           a=n+1
	   
	   return a
     elif m>0 and n==0:
            
            
            a = ack(m-1,1) 
             
	    return a
     elif m>0 and n>0:
            
	    a=ack(m-1,ack(m,n-1))
            
	    return a
u=raw_input('enter m and n\n')
u=int(u)
v=raw_input()
v=int(v)
a=ack(u,v)
print a
         
         
