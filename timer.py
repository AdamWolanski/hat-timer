#!/usr/bin/python

class Time:
    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

def timePrint(t):
    
    '''if self.flag == 1:
        print "+ :"
    else:
        print "- :"'''
    print "{}:{}:{}".format(t.hours, t.minutes, t.seconds)

def timeParse(t):
    return Time(int(t[0:2]),int(t[3:5]),int(t[6:8])) 

def timeAdd(time1, time2): #ex t1 = '12:34:56' 
    hours = 0
    minutes = 0
    seconds = 0
    
    seconds = time1.seconds + time2.seconds
    if seconds >= 60:
        minutes += 1
        seconds -= 60
    minutes = time1.minutes + time2.minutes
    if minutes >= 60:
        hours += 1
        minutes -= 60
    hours = time1.hours + time2.hours
    return Time(hours,minutes,seconds)

def timeSub(time1, time2): #ex t1 = '12:34:56'
    hours = 0
    minutes = 0
    seconds = 0
    seconds = (time1.seconds - time2.seconds)
    if seconds < 0:
        minutes -= 1
        seconds += 60
    minutes = (time1.minutes - time2.minutes)
    if minutes < 0:
        hours -= 1
        minutes += 60
    hours = (time1.hours - time2.hours)
    #hours = abs(hours)
    return Time(hours, minutes, seconds)

def timeCalculate(t1, t2):
    return timeSub(timeParse(t1), timeParse(t2))

def timeCalculate(t1, t2, t3=Time(0,0,0), flag=1): #flag 1 - count weekends, 0 - dont count
    if flag == 1:
        tmp = timeSub(timeParse(t1),timeParse(t2))
        time = timeAdd(tmp, t3)
    else:
        tmp = timeSub(timeParse(t1), timeParse(t2))
        time = timeSub(tmp, t3)
    return time

#example usage:
t = timeCalculate('12:34:56', '32:43:54')
timePrint(t)
