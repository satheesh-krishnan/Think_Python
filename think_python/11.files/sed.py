def sed(f1,f2,ps,rs):
    try:
        r=open(f1)
        w=open(f2,'w')
    
        for line in r:
             delimiter=' '
             s=line.split(delimiter)
             l=len(s)
             m=0
             while m<l:
                 if s[m]==ps:
                     w.write(rs)
                     w.write(' ')
                 else:
                     w.write(s[m])
                     w.write(' ')
                 m=m+1
        r.close()
        w.close()
    except:
        print 'something is wrong'
f=raw_input('enter source file\n')
d=raw_input('enter destination file\n')
p=raw_input('enter pattern string\n')
r=raw_input('enter replacement string\n')
sed(f,d,p,r)
    
