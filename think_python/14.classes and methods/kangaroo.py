class kangaroo(object):
    def __init__(self):
        self.pouchcontents=[]
   
    def putinpouch(self,x):
        if isinstance(x,kangaroo):
            for i in x.pouchcontents:
                self.pouchcontents.append(i)
        else:
            self.pouchcontents.append(x)
        
            
    def __str__(self):
        l=[self]
        for i in self.pouchcontents:
            l.append(i)
        return str(l)
kanga=kangaroo()
roo=kangaroo()
kanga.putinpouch('64')
roo.putinpouch('okj')
roo.putinpouch('45')
kanga.putinpouch(roo)
print kanga
