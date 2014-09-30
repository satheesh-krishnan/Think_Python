class Card(object):
    
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
    def __cmp__(self,other):
        n=(self.h*3600)+(self.m*60)+self.s
        m=(other.h*3600)+(other.m*60)+other.s
        return cmp(n,m)
a=Card(10,18,34)
b=Card(5,45,23)
print a.__cmp__(b)    
