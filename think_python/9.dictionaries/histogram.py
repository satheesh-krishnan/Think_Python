def histogram(s):
    d = dict()
    for c in s:
        f=d.get(c,0)
        d[c]=f+1
    return d

