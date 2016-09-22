# test_script

import time
import unittest
import sys
# use sys to find the location of GA1 folder to import the AmesWeather
# use sys.path to find the location of this file
# however, we need to get rid of test_script to arrive in GA1 folder
i = sys.path
# split the string by '\' and put it in a array
a = i[0].split("\\")
b = ""
# put the words in the array back on with '\' to get the location of GA1
for i in range(len(a)-1):
        b = b + a[i] + '\\'

b = b[:-1]
# ask python to find path of the Group Assignment folder
sys.path.insert(0, b)
import AmesWeather as AW

# print out the current time and current date
def timePrinter():
    currentTime = time.strftime("%H:%M:%S")
    currentDate = time.strftime("%d/%m/%Y")
    print
    print(currentTime)
    print(currentDate)

# main test class is created below.
# unittest is used to test the AmesWeather.py
class testHistorical(unittest.TestCase):


    def test_temp_true(self):
        testDate = AW.stringToDate('2/12/2015:17:37')
        testTimeStamp = AW.dateToTimeStamp(testDate)
        print(testTimeStamp)
        timePrinter()
        self.assertTrue(self)



if __name__ == '__main__':
    unittest.main()
