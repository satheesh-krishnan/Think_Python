class Time():
    "multiply time"
def multime(time,number):
    p=(time.h*3600)+(time.m*60)+time.s
    p=float(p)
    pr=p*number
    pr=int(pr)
    time.h=pr/3600%24
    time.m=pr%3600/60
    time.s=pr%3600%60
    print  time.h,':',time.m,':',time.s
   
def dis(time,number):
    number=1/number
    print 'per mile speed is',
    multime(time,number)   
time=Time()
n=raw_input('enter the number\n')
n=float(n)
time.h=1
time.m=12
time.s=20
multime(time,n)
time.h=4
time.m=54
time.s=43
dis(time,n)
