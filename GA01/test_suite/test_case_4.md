#test_script


#Test Case: 4
=============
1.
-----------------------------------------
```os.system('python AmesWeather.py 10/100/2001:12:12 P T WS WD')
```
This Test Case detects the error when user puts the date in a wrong format

2. Command being tested:
---------------------------------------
``` 10/100/2001:12:12 P T WS WD
```
  * 10/100/2001:12:12: wrong date format
  * P: pressure
  * T: temperature
  * WS: wind speed
  * WD: wind direction

3. Expected output
---------------------------------
We expect the output to detect the errors and let user knows.
4. Observed output:
-----------------------------------
```
$ python test_script.py
Invalid format. Type --help for help.
```
### --help
```
$ python AmesWeather.py --help

AMES WEATHER HELP:
-------------------

This program, takes arguments in the following format:
AmesWeather (<date> | "") (-M | "") (measure(-timeoffset | ""))

Measure: { P | T | WS | WD }
P = pressure
T = temperature
WS= wind speed
WD = wind direction

Time-offset: {Y | M | W | D}
Y = year
M = month
W = week
D = day

(Empty "" signifies an optional argument)

Other Commands:
--help
--version
```

5. The test is passed
------------------------------------
09/23/2016:15:31
Version: 00.12
```
$ python AmesWeather.py --version
Running AmesWeather v00.12
```
