class Time(object):
    def intime(self):
        t=(self.h*3600)+(self.m*60)+(self.s)
        print t
time=Time()
time.h=6
time.m=34
time.s=50
time.intime()

