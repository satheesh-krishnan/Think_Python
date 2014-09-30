def power(a,b):
     x=a%b
     y=a/b
     z=y%b
     if x==0:
          if z==0:
                return True
          else:
		return False
     else:
          return False
u=raw_input('enter a and b\n')
v=raw_input()
u=int(u)
v=int(v)
n=power(u,v)
print n

 
