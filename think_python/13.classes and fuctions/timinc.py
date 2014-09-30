class Time(object):
    "time without loop"
def incre(time,seconds):
    time.second+=seconds
    if time.second>=60:
        minute=time.second/60
        time.minute+=minute
    if time.minute>=60:
        hour=time.minute/60
        time.hour=(hour+time.hour)%24
        time.minute=time.minute%60
    time.second=time.second%60
    print time.hour,':',time.minute,':',time.second
time=Time()
print 'enter seconds\n'
seconds=raw_input()
seconds=int(seconds)
time.hour=4
time.minute=24
time.second=34
incre(time,seconds)




























    
