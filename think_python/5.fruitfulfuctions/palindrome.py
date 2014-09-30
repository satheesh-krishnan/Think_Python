
def check(s,t,m):
     
     if m!=0 and m!=1:
        if s==t:
             return ''
        else:
             return False
         
     else:
          
          return True  
         
           
             
             
       
def palindrome(a,y,z,c):
    
    v=a[y]
    r=a[z]
    j=check(v,r,c)
    if j==True or j==False:
         print j
         return
         
    palindrome(a,y+1,z-1,c-2)


h=raw_input('enter the string\n')
x=len(h)
p=0
q=x-1
palindrome(h,p,q,x)

         
         	
		

    

        
        
