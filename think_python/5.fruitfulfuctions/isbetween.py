def isbetween(x,y,z):
    if x<=y:
	if y<=z:
		return True
        else:
	        return False
    else:
         return False
a=raw_input('enter x y z\n')
a=int(a)
b=raw_input()
b=int(b)
c=raw_input()
c=int(c)
d=isbetween(a,b,c)
print d
