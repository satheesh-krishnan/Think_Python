def sumall(*t):
    d=0
    for s in t:
        d=d+s
    return d
t=(3,4,5,6,7)
f=sumall(*t)
print f
