def check_fermat():
    a= raw_input('input a,b,c and n \n')
    
    a=int(a)
    b= raw_input()
    
    b=int(b)
    c= raw_input()
   
    c=int(c)
    n= raw_input()
    
    n=int(n)
    
    s=a**n    
    
    u=b**n
    v=s+u
    
    t=c**n
    
    if v == t and n > 2:
         print 'holy smokes fermat was wrong'
    else:
         print 'it doesnt work'
       


check_fermat()
  
