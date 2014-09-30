from datetime import *
def dt(date):
    day=['monday','tuesday','wednesday','thusday','friday','saturday','sunday']
    d=date
    l=date.weekday(d)
    print d

date.year=1990
date.month=6
date.day=4
dt(date)
