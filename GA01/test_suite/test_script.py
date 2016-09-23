# test_script

import time
import unittest
import sys
import os
# use sys to find the location of GA1 folder to import the AmesWeather
# use sys.path to find the location of this file
# however, we need to get rid of test_script to arrive in GA1 folder
i = sys.path
# split the string by '\' and put it in a array
a = i[0].split("\\")
b = ""
# put the words in the array back on with '\' to get the location of GA1
for i in range(len(a)-1):
        b = b + a[i] + '\\' + '\\'

b = b[:-1]
# ask python to find path of the Group Assignment folder

os.chdir(b)
os.system('python AmesWeather.py P T WS WD')
