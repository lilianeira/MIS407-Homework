#Test Case: 3

1.
-----------------------------------------
```os.system('python AmesWeather.py 01/01/2001:12:12 P T WS WD')
```
This Test Case tests the historical data in 01/01/2001 12:12.

2. Command being tested:
---------------------------------------
``` '01/01/2001:12:12 P T WS WD'
```
  * 01/01/2001:12:12: the specific date and time, we want to test on
  * P: pressure
  * T: temperature
  * WS: wind speed
  * WD: wind direction

3. Expected output
---------------------------------
We expect the output to be the pressure, temperature, wind speed and wind direction in 01/01/2001:12:12 without any errors
4. Observed output:
-----------------------------------
```
$ python test_script.py
1032.77,13.31,13.68,214
```

5. The test is passed
------------------------------------
09/23/2016:15:16
Version: 00.12
```
$ python AmesWeather.py --version
Running AmesWeather v00.12
```
