#test_script



#Test Case: 1
=============
1. Objective
--------------------------
```os.system('python AmesWeather.py -M P T WS WD')
```
This Test Case uses metric system to test the current pressure, temperature, wind speed and wind direction in Ames.

2. Command being tested:
------------------------------
``` -M P T WS WD
```
  * -M: switch the measure system to metric system
  * P: test the pressure
  * T: test the temperature
  * WS: test the wind speed
  * WD: test the wind direction

3. Expected output
--------------------------------
We expect to get 1015 hpa on pressure, 30.0 degree on temperature, 0.5 m/s on wind speed and 174 on wind direction
4. Observed output:
----------------------------
```
$ python test_script.py
1015,29.44,0.51,140
```
The result we had was listed above.

5. The test is passed
------------------------------------
09/23/2016:14:52
Version: 00.12
```
$ python AmesWeather.py --version
Running AmesWeather v00.12
```
