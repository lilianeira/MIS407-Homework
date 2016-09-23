# AmesWeather.py
# Command line interface for current and historical weather in Ames


from weather import current, historical
import datetime
import sys
import re

version = "00.10"


def stringToDate(str):
    format = '%m/%d/%Y:%H:%M'
    try:
        newDate = datetime.datetime.strptime(str, format)
        return newDate
    except ValueError as e:
        raise ValueError('Invalid date format. Type --help for help. : {0}'.format(e))


def dateToTimeStamp(dt):
    timestamp = dt.timestamp()
    timestamp = int(timestamp)
    return timestamp


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


def p(raw, type, format, wdate):
    response = 'N/A'
    if raw == 'P':
        if type == 'current':
            response = current.getPressure(format)
        elif type == 'historical':
            now = datetime.datetime.now()
            nowStamp = dateToTimeStamp(now)
            stamp = dateToTimeStamp(wdate)
            if stamp > nowStamp:
                response = 'N/A'
            else:
                response = historical.getPressure(stamp, format)
    else:
        offsetType = raw[-1:]
        now = datetime.datetime.now()
        nowStamp = dateToTimeStamp(now)
        stamp = dateOffset(wdate, offsetType)
        if stamp > nowStamp:
            response = 'N/A'
        else:
            response = historical.getPressure(stamp, format)
    return(response)


def unkown():
    return('N/A')

def t(raw, type, format, wdate):
    response = 'N/A'
    if raw == 'T':
        if type == 'current':
            response = current.getTemp(format)
        elif type == 'historical':
            now = datetime.datetime.now()
            nowStamp = dateToTimeStamp(now)
            stamp = dateToTimeStamp(wdate)
            if stamp > nowStamp:
                response = 'N/A'
            else:
                response = historical.getTemp(stamp, format)
    else:
        offsetType = raw[-1:]
        now = datetime.datetime.now()
        nowStamp = dateToTimeStamp(now)
        stamp = dateOffset(wdate, offsetType)
        if stamp > nowStamp:
            response = 'N/A'
        else:
            response = historical.getTemp(stamp, format)
    return(response)

def ws(raw, type, format, wdate):
    response = 'N/A'
    if raw == 'WS':
        if type == 'current':
            response = current.getWindSpeed(format)
        elif type == 'historical':
            now = datetime.datetime.now()
            nowStamp = dateToTimeStamp(now)
            stamp = dateToTimeStamp(wdate)
            if stamp > nowStamp:
                response = 'N/A'
            else:
                response = historical.getWindSpeed(stamp, format)
    else:
        offsetType = raw[-1:]
        now = datetime.datetime.now()
        nowStamp = dateToTimeStamp(now)
        stamp = dateOffset(wdate, offsetType)
        if stamp > nowStamp:
            response = 'N/A'
        else:
            response = historical.getWindSpeed(stamp, format)
    return(response)

def wd(raw, type, format, wdate):
    response = 'N/A'
    if raw == 'WD':
        if type == 'current':
            response = current.getWindDir(format)
        elif type == 'historical':
            now = datetime.datetime.now()
            nowStamp = dateToTimeStamp(now)
            stamp = dateToTimeStamp(wdate)
            if stamp > nowStamp:
                response = 'N/A'
            else:
                response = historical.getWindDir(stamp, format)
    else:
        offsetType = raw[-1:]
        now = datetime.datetime.now()
        nowStamp = dateToTimeStamp(now)
        stamp = dateOffset(wdate, offsetType)
        if stamp > nowStamp:
            response = 'N/A'
        else:
            response = historical.getWindDir(stamp, format)
    return(response)


switcher = { 'P': p, 'P-Y': p, 'P-M': p, 'P-W': p, 'P-D': p,
            'T': t, 'T-Y': t, 'T-M': t, 'T-W': t, 'T-D': t,
            'WS': ws, 'WS-Y': ws, 'WS-M': ws, 'WS-W': ws, 'WS-D': ws,
            'WD': wd, 'WD-Y': wd, 'WD-M': wd, 'WD-W': wd, 'WD-D': wd}

s = ''
wtype = 'current'
wformat = 'us'
startingPoint = 1
wdate = 0

if len(sys.argv) > 1:
    if sys.argv[1] == '--version':
        print('Running AmesWeather v' + version)
    elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
        print('Someone should eventually put some help here.')
    else:
        # If no help of version command was called,
        # that means it is weather time!

        # TODO: Before we can start looping through comands,
        # we need to figure out which optional
        # arguments are supplied!
        if sys.argv[1] == '-M':
            wformat = 'si'
            startingPoint = 2
        elif sys.argv[1] not in switcher:
            # if the first value here is not in switcher,
            # it is either the date or WRONG
            wtype = 'historical'
            wdate = stringToDate(sys.argv[1])
            if sys.argv[2] == '-M':
                wformat = 'si'
                startingPoint = 3
            else:
                startingPoint = 2
        else:
            wdate = 0

        for i in range(startingPoint, len(sys.argv)):
            fun = switcher.get(sys.argv[i], unkown)
            s = s + str(fun(sys.argv[i], wtype, wformat, wdate)) + ","
            if i == len(sys.argv)-1:
                s = s[:-1]
        print(s)
else:
    print('No arguments provided. Type --help for help.')
