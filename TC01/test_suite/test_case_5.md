#Test Case: 3

1.
-----------------------------------------
```os.system('python AmesWeather.py P T WS WD SDF')
```
This Test Case detects the error if user types a wrong command

2. Command being tested:
---------------------------------------
``` 'P T WS WD SDF'
```
  * P: pressure
  * T: temperature
  * WS: wind speed
  * WD: wind direction
  * SDF: wrong command

3. Expected output
---------------------------------
We expect the output to print current pressure, temperature, wind speed, wind direction and N\A to detect the error.
4. Observed output:
-----------------------------------
```
$ python test_script.py
1015,86,1.14,153,N/A
```

5. The test is passed
------------------------------------
09/23/2016:15:34
Version: 00.12
```
$ python AmesWeather.py --version
Running AmesWeather v00.12
```
