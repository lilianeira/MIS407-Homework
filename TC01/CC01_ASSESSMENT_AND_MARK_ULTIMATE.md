# TEAM ULTIMATE

I tested your code by running the testbench.py (using 10_test_args.csv data) and testbench-RobustTest.py (using 10_test_args-RobustTest.csv data )

### Output from  testbench.py:
```
>>>Calling with args = ['Amesweather.py', '06/06/1962:02:00', 'T-Y', 'T-W', 'WS-Y']
>>>Response :  N/A,77,68,8
>>>Calling with args = ['Amesweather.py', 'P', 'WS-D', 'WS-W']
>>>Response :  N/A,1018.36,3.21,9
>>>Calling with args = ['Amesweather.py', '05/21/1997:10:00', 'T-Y', 'P', 'P-W', 'WS-D', 'T-D', 'P-Y', 'WD-W', 'WS', 'WD-D', 'WS-Y', 'P-D', 'T-W', 'T']
>>>Response :  N/A,51.67,1026.83,1004.21,3.9,36.82,1011.5,317,6.42,340,6.2,1021.81,46.25,41.08
>>>Calling with args = ['Amesweather.py', 'T', 'WS-W', 'P-D', 'WS-Y', 'P-W', 'WD-D']
>>>Response :  N/A,64.26,9,1025.99,7.67,1017.29,357
>>>Calling with args = ['Amesweather.py', '01/10/2002:17:00', 'P-Y', 'T-D', 'WS-Y', 'T', 'WS-D', 'WD-Y', 'WD-D', 'WD-W', 'P-D', 'WD', 'P-W', 'WS']
>>>Response :  N/A,1018.06,54.23,10.77,37.04,13.16,194,323,209,1008.16,311,1026.74,14.53
>>>Calling with args = ['Amesweather.py', 'WS-W', 'P-W', 'T-D', 'WD-Y', 'P', 'T-W', 'WS-Y', 'WD', 'P-Y', 'WD-W']
>>>Response :  N/A,9,1017.29,49.04,54,1018.36,67.18,7.67,4,1029.8,116
>>>Calling with args = ['Amesweather.py', '07/16/2009:18:00', 'WS', 'WD-W', 'T-W', 'T-Y', 'WD-Y', 'WD', 'T', 'P-W', 'P', 'P-Y', 'T-D', 'WD-D', 'WS-Y', 'P-D']
>>>Response :  N/A,10.3,191,63.38,79.82,194,310,73.12,1018.2,1015.5,1018.2,77.95,296,8.56,1016.3
>>>Calling with args = ['Amesweather.py', 'WD-Y', 'P']
>>>Response :  N/A,54,1018.36
>>>Calling with args = ['Amesweather.py', '03/24/2010:14:00', 'WS-D', 'P', 'T', 'P-Y', 'WS-Y', 'P-W', 'T-W']
>>>Response :  N/A,5.87,1017.8,43.87,1001,14.3,1024.5,37.21
>>>Calling with args = ['Amesweather.py', 'P-Y', 'WS-W', 'WS-Y', 'T-W', 'P-D']
>>>Response :  N/A,1029.8,9,7.67,67.18,1025.99
~~~~~~ TOTAL TIME =  10.637048721313477
```

### Output from testbench-RobustTest.py:

```
$ python testbench-robusttest.py
>>>Calling with args = ['Amesweather.py', '06/1962/02/00', 'T-Y', 'T-W', 'WS-Y']
Date Format Error.
>>>Response :  None
>>>Calling with args = ['Amesweather.py', 'P', 'WS-D', '123', ' WS-W']
>>>Response :  Exception Thrown!
>>>Calling with args = ['Amesweather.py', '', ' T-Y', ' P', ' P -W', 'WS-D', 'T-D', 'P-Y', 'WD-W', 'WS', 'WD-D', 'WS-Y', 'P-D', 'T-W', 'T']
Date Format Error.
>>>Response :  None
>>>Calling with args = ['Amesweather.py', 'asdf', ' asdf - asdf']
Date Format Error.
>>>Response :  None
>>>Calling with args = ['Amesweather.py', '123-123']
Date Format Error.
>>>Response :  None
>>>Calling with args = ['Amesweather.py', '16/16/2009:18:00', 'WS', 'WD-W', 'T-W', 'T-Y', 'WD-Y', 'WD', 'T', 'P-W', 'P', 'P-Y', 'T-D', 'WD-D', 'WS-Y', 'P-D']
Date Format Error.
>>>Response :  None
>>>Calling with args = ['Amesweather.py', 'WD-M', 'P']
>>>Response :  N/A,56,1016.87
~~~~~~ TOTAL TIME =  1.307255506515503
Traceback (most recent call last):
  File "testbench-robusttest.py", line 82, in <module>
    uwriter.writerow(rowstr.split(","))
AttributeError: 'NoneType' object has no attribute 'split'
```

## General Assessment:
### The Good
1. You included NA for the time the measure was made (which is appropriate since the API simply parrots back what you give it for a time).
2. You detailed the data source, and explained the source of the measurements
### The Bad
1. Your choice of data source doesn't include a measurement date, nor anything about station/location where the measurement was made.
2. Your error handling was a bit weak - in that you printed an error to the screen directly, and responded back to the calling function with the None object.

### Timing results:
For timing, I ran through three runs from testbench.py
1) 10.637048721313477
2) 9.95553469657898
3) 9.878197431564331
Average time per 10 transactions is therefore 10.15692695 seconds.

## Rubric Assessment:
Correctness of Results: Rank 2nd
Completeness of Results: Rank 1st
Robustness: Rank 1st
Speed: Rank 2nd 

> __Total score (see Rubric for formula details)__
1+1+2+3*1=7

Your score places you in a very close second relative to the other teams.

__Your mark for CC01 is 95%.__
