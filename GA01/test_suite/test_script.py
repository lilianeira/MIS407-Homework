#test_script

import time
import unittest
import sys
sys.path.insert(0, 'D:\\2016 Fall\\MIS 407\\Git Bash\\TEAM-ULTIMATE\\GA01')
import AmesWeather as AW

def timePrinter():
    currentTime = time.strftime("%H:%M:%S")
    currentDate = time.strftime("%d/%m/%Y")
    print
    print(currentTime)
    print(currentDate)
# turns the string into python's datetime format
testDate = AW.stringToDate('2/12/2015:17:37')
print(testDate)

# turns the datetime object into a UNIX timestamp
testTimeStamp = AW.dateToTimeStamp(testDate)
print(testTimeStamp)

# turns the datetime object into a UNIX timestamp for 1 day before
print(AW.dateOffset(testDate, 'D'))
# turns the datetime object into a UNIX timestamp for 1 month before
print(AW.dateOffset(testDate, 'M'))

# gets temp from timestamp
print(AW.historical.getTemp(str(testTimeStamp)))

print(timePrinter())
