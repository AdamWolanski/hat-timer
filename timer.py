#!/usr/bin/python

import sys

class Time:
    def __init__(self, argv):
        self.args = argv
        self.time = 0
        self.hours = 0
        self.minutes = 0
        self.flag = 1
        self.timeSet()
        self.timePrint()
    def timePrint(self):
        if self.flag == 1:
            print "Masz w zapasie: "
        else:
            print "Brakuje ci: "
        print "{}:{}".format(self.hours, self.minutes)
    def timeSet(self):
        for t in self.args:
            self.time += float(t)
        self.time *= (60*8)
        if self.time < 0:
            self.flag = 0
        else:
            self.flag = 1
        self.hours = int(self.time/60)
        self.minutes = int(self.hours * 60 - self.time)
        self.hours = abs(self.hours)
        self.minutes = abs(self.minutes)

def main(argv):
    t = Time(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
