# AmesWeather.py
# Command line interface for current and historical weather in Ames


from weather import current, historical
import datetime
import sys


for i in range(0, len(sys.argv)):
    print(sys.argv[i])
    # TODO: command line stuff goes here probably


def stringToDate(str):
    format = '%m/%d/%Y:%H:%M'
    newDate = datetime.datetime.strptime(str, format)
    return newDate


def dateToTimeStamp(dt):
    timestamp = dt.timestamp()
    timestamp = int(timestamp)
    return timestamp


def currentDate():
    dateNow = datetime.datetime.now()
    return dateNow


def dateOffset(dt, type):
    response = -1
    if type == 'W' or type == 'D':
        # 1 week and 1 day will always be the same amount of time
        # so we can just subtract the seconds from the timestamp
        timeStampTemp = dateToTimeStamp(dt)
        if type == 'W':
            response = timeStampTemp - 604800
        elif type == 'D':
            response = timeStampTemp - 86400
    elif type == 'Y' or type == 'M':
        # month and year could differ, so we can't just subtract seconds
        format1 = '%m||%d||%Y||%H||%M'
        dateString = dt.strftime(format1)
        dateInfo = dateString.split('||')
        month = dateInfo[0]
        day = dateInfo[1]
        year = dateInfo[2]
        hour = dateInfo[3]
        minutes = dateInfo[4]
        # FIXME? leap year? currently uses last year's 28th.
        if int(month) == 2 and int(day) == 29:
            day = '28'
        if type == 'Y':
            year = str(int(year) - 1)
        elif type == 'M':
            tempM = int(month)
            if tempM == 1:
                month = '12'
                year = str(int(year) - 1)
            else:
                month = str(int(month) - 1)
        dateString2 = month+'/'+day+'/'+year+':'+hour+':'+minutes
        dateobj = stringToDate(dateString2)
        response = dateToTimeStamp(dateobj)
    return response


# HERE'S AN EXAMPLE OF HOW THESE DATE FUNCTIONS WORK.
# We can delete this later

# turns the string into python's datetime format
testDate = stringToDate('2/12/2015:17:37')
print(testDate)

# turns the datetime object into a UNIX timestamp
testTimeStamp = dateToTimeStamp(testDate)
print(testTimeStamp)

# turns the datetime object into a UNIX timestamp for 1 day before
print(dateOffset(testDate, 'D'))
# turns the datetime object into a UNIX timestamp for 1 month before
print(dateOffset(testDate, 'M'))

# gets temp from timestamp
print(historical.getTemp(str(testTimeStamp)))

# END EXAMPLES
