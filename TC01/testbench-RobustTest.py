"""Testbench for testing AmesWeather.py

Brief Intro:

This script will need to run from it's current location. It will
import your AmesWeather.py file as a module and then  read 10_test_args.csv to
determine the data that will be requested from your AmesWeather.py script.
Finally, it will store the result from the 10 tests in the file results.csv.

Longer Intro:

This script will read each row found in the 10_test_args.csv file and for each
row in this file call AmesWeather.main(args) with the args parameter set to a
list similar in format to the same list you would have received if your
AmesWeather.py script was called from the command line.

For example:
If in the first row of 10_test_args.csv we find....
06/06/1962:02:00, T-Y, T-W, WS-Y

...then, the following call to your AmesWeather.main() function will be made:

AmesWeather.main(["AmesWeather.py", "06/06/1962:02:00", "T-Y", "T-W", "WS-Y"])

From this call, your AmesWeather.main should return a string in the form
(06/06/1961:02:30, 72.3, 81.2, 10.2)

NOTE1: This is not the actual measurement for this - but rather and example to
illustrate the format.

NOTE2: As we discussed in the last class (the start day of the Bake-off, the
date returned should be the date for which the first data item returned is valid.
That is, in the case of our example, (06/06/1961:02:30, 72.3, 81.2, 10.2), then
06/06/1961:02:30 is the datetime for which the value 72.3 is valid. This date
data is part of all the weather API/Data and should be easily extracted and
included in your response.

If, for whatever reason, you can't respond with any valid data for the requested
items, you should return NA's. So, if you can't return any values you should
return.
(NA, NA, NA, NA)

NOTE: As per the original assignment instructions, valid data is any
data that is within 1.5 hours of the requested date time.

If, you can't find valid data for one of more of the requested items, so for
instance you could not return valid data for all but the WS-Y
request then you would return...
(06/06/1962:02:00, 72.3, 81.2, NA)

If your program is completely confused, and cannot handle the request, or throws
an exeption, you should respond with the following string:
(NA)

"""
import AmesWeather as aw
import sys

from time import time, sleep
import csv

start_time = time()
with open('10_test_args-RobustTest.csv', "r") as cf:
    udataReader = csv.reader(cf)
    responses = []
    for row in udataReader:
        args = ["Amesweather.py"] + row
        print(">>>Calling with args = ", end="")
        print(args)
        try:
            response = aw.main(args)
        except:
            response = "Exception Thrown!"
        print(">>>Response : ", response)
        responses.append(response)

print("\n\n\n~~~~~~ TOTAL TIME = ", time() - start_time)

with open('results-RobustTest.csv', "w") as wf:
    uwriter = csv.writer(wf,  lineterminator='\n')
    for rowstr in responses:
        uwriter.writerow(rowstr.split(","))
