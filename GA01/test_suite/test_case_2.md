#test_script

#Test Case: 2
=============
1. ```os.system('python AmesWeather.py P-D P-W P-M P-Y')
```
This Test Case tests the pressure yesterday, last weed, last month, last year.

2.
``` P-D P-W P-M P-Y
```
  * P-D: pressure yesterday
  * P-W: pressure last week
  * P-M: pressure last month
  * P-Y: pressure last year
3. We expect the output to be somewhere around 1000.
4. Observed Output. 
```
$ python test_script.py
1012.63,1011.85,1014.08,1020.18
```

5. The test is passed
------------------------------------
09/23/2016:15:08
Version: 00.12
```
$ python AmesWeather.py --version
Running AmesWeather v00.12
```
