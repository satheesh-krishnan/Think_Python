def compare(x,y):
    if x>y:
	n=1         
	return n
    elif x==y:
	n=0
        return n
    else:
	n=-1
	return n
a=raw_input('enter x and y\n')
a=int(a)
b=raw_input()
b=int(b)
n=compare(a,b)
print n

