class rectangle(object):
    "it a rectangle"
def rect(c,y,z):
    b=rectangle()
    
    b.l=y.len+c.cor
    b.w=z.wid+c.cor1
    print 'current co-ordiantes of the rectangle (',c.cor,',',c.cor1,')(',b.l,',',c.cor1,')(',b.l,',',b.w,')(',c.cor,',',b.w,')'

    return b
def movrect(rect,g,dx,dy):
    g.cor+=dx.lenx
    g.cor1+=dy.widx
    rect.l+=dx.lenx
    rect.w+=dy.widx
    print 'new co-ordiantes of the rectangle (',g.cor,',',g.cor1,')(',rect.l,',',g.cor1,')(',rect.l,',',rect.w,')(',g.cor,',',rect.w,')'

def main():
    g=rectangle()
    h=rectangle()
    i=rectangle()
    g.cor=raw_input('enter corner\n')
    g.cor1=raw_input()
    h.len=raw_input('enter lengt \n')
    
    i.wid=raw_input('enter width \n')
    g.cor=float(g.cor)
    g.cor1=float(g.cor1)
    h.len=float(h.len)
    i.wid=float(i.wid)
    f=rect(g,h,i)
    h.lenx=raw_input('enter x extension\n')
    i.widx=raw_input('enter y extension\n')
    h.lenx=float(h.lenx)
    i.widx=float(i.widx)
    movrect(f,g,h,i)
main()
