"""AmesWeather.py main module. This module takes in a user command from
the command line and outputs historical weather measurements and if no date
is specified, it outputs the currenct weather measurements"""


from weather import current, historical
import datetime
import sys

version = "00.13"


def dateToString(date):
    """convert a date string to a datetime obj"""
    format = '%m/%d/%Y:%H:%M'
    newDate = date.strftime(format)
    return newDate



def stringToDate(str):
    """convert a date string to a datetime obj"""
    format = '%m/%d/%Y:%H:%M'
    try:
        newDate = datetime.datetime.strptime(str, format)
        return newDate
    except ValueError as e:
         return -1


def dateToTimeStamp(dt):
    """convert a datetime obj to UNIX timestamp"""
    timestamp = dt.timestamp()
    timestamp = int(timestamp)
    return timestamp


def dateOffset(dt, type):
    """offset a date. returns a UNIX timestamp"""
    response = -1
    timeStampTemp = dateToTimeStamp(dt)
    if type == 'W':
        response = timeStampTemp - 604800
    elif type == 'D':
        response = timeStampTemp - 86400
    elif type == 'M':
        # ueses 30 days as a 'month'
        response = timeStampTemp - 2592000
    elif type == 'Y':
        # ueses 365 days as a 'year'
        response = timeStampTemp - 31536000
    return response


def p(raw, type, format, wdate, isFirst):
    """get pressure"""
    response = 'N/A'
    if raw == 'P':
        if type == 'current':
            response = current.getPressure(format)
        elif type == 'historical':
            now = datetime.datetime.now()
            nowStamp = dateToTimeStamp(now)
            stamp = dateToTimeStamp(wdate)
            wdate = datetime.datetime.fromtimestamp(stamp)
            if stamp > nowStamp:
                response = 'N/A'
            else:
                response = historical.getPressure(str(stamp), format)
    else:
        offsetType = raw[-1:]
        now = datetime.datetime.now()
        nowStamp = dateToTimeStamp(now)
        stamp = dateOffset(wdate, offsetType)
        wdate = datetime.datetime.fromtimestamp(stamp)

        if stamp > nowStamp:
            response = 'N/A'
        else:
            response = historical.getPressure(str(stamp), format)
    if isFirst == 1:
        dateString = dateToString(wdate)
        return(dateString+","+str(response))
    else:
        return(response)


def unkown(raw, type, format, wdate):
    """handle unknown arguments"""
    return('N/A')


def t(raw, type, format, wdate, isFirst):
    """get temperature"""
    response = 'N/A'
    if raw == 'T':
        if type == 'current':
            response = current.getTemp(format)
        elif type == 'historical':
            now = datetime.datetime.now()
            nowStamp = dateToTimeStamp(now)
            stamp = dateToTimeStamp(wdate)
            wdate = datetime.datetime.fromtimestamp(stamp)
            if stamp > nowStamp:
                response = 'N/A'
            else:
                response = historical.getTemp(str(stamp), format)
    else:
        offsetType = raw[-1:]
        now = datetime.datetime.now()
        nowStamp = dateToTimeStamp(now)
        stamp = dateOffset(wdate, offsetType)
        wdate = datetime.datetime.fromtimestamp(stamp)

        if stamp > nowStamp:
            response = 'N/A'
        else:
            response = historical.getTemp(str(stamp), format)
    if isFirst == 1:
        dateString = dateToString(wdate)
        return(dateString+","+str(response))
    else:
        return(response)


def printHelp():
    """print help information"""
    print("\nAMES WEATHER HELP:\n-------------------\n")
    print("This program, takes arguments in the following format:")
    print("AmesWeather (<date> | \"\") (-M | \"\") (measure(-timeoffset | \"\"))\n")
    print("Date format: MM/DD/YYYY:HH:MM (HH:MM is 24 hr time)\n")
    print("Measure: { P | T | WS | WD }\nP = pressure\nT = temperature\nWS= wind speed\nWD = wind direction")
    print("\nTime-offset: {Y | M | W | D}\nY = year\nM = month\nW = week\nD = day")
    print("\n(Empty \"\" signifies an optional argument)\n")
    print("Other Commands:\n--help\n--version")


def ws(raw, type, format, wdate, isFirst):
    """get wind speed"""
    response = 'N/A'
    if raw == 'WS':
        if type == 'current':
            response = current.getWindSpeed(format)
        elif type == 'historical':
            now = datetime.datetime.now()
            nowStamp = dateToTimeStamp(now)
            stamp = dateToTimeStamp(wdate)
            wdate = datetime.datetime.fromtimestamp(stamp)
            if stamp > nowStamp:
                response = 'N/A'
            else:
                response = historical.getWindSpeed(str(stamp), format)
    else:
        offsetType = raw[-1:]
        now = datetime.datetime.now()
        nowStamp = dateToTimeStamp(now)
        stamp = dateOffset(wdate, offsetType)
        wdate = datetime.datetime.fromtimestamp(stamp)
        if stamp > nowStamp:
            response = 'N/A'
        else:
            response = historical.getWindSpeed(str(stamp), format)
    if isFirst == 1:
        dateString = dateToString(wdate)
        return(dateString+","+str(response))
    else:
        return(response)


def wd(raw, type, format, wdate, isFirst):
    """get wind direction"""
    response = 'N/A'
    if raw == 'WD':
        if type == 'current':
            response = current.getWindDir(format)
        elif type == 'historical':
            now = datetime.datetime.now()
            nowStamp = dateToTimeStamp(now)
            stamp = dateToTimeStamp(wdate)
            wdate = datetime.datetime.fromtimestamp(stamp)
            if stamp > nowStamp:
                response = 'N/A'
            else:
                response = historical.getWindDir(str(stamp), format)
    else:
        offsetType = raw[-1:]
        now = datetime.datetime.now()
        nowStamp = dateToTimeStamp(now)
        stamp = dateOffset(wdate, offsetType)
        wdate = datetime.datetime.fromtimestamp(stamp)
        if stamp > nowStamp:
            response = 'N/A'
        else:
            response = historical.getWindDir(str(stamp), format)
    if isFirst == 1:
        dateString = dateToString(wdate)
        return(dateString+","+str(response))
    else:
        return(response)


def main(txt):
    switcher = {'P': p, 'P-Y': p, 'P-M': p, 'P-W': p, 'P-D': p,
        'T': t, 'T-Y': t, 'T-M': t, 'T-W': t, 'T-D': t,
        'WS': ws, 'WS-Y': ws, 'WS-M': ws, 'WS-W': ws, 'WS-D': ws,
        'WD': wd, 'WD-Y': wd, 'WD-M': wd, 'WD-W': wd, 'WD-D': wd}
    s = ''
    wtype = 'current'
    wformat = 'us'
    startingPoint = 1
    wdate = datetime.datetime.now()
    args = txt.split()
    rdate = datetime.datetime.now()
    isFirst = 0
    if len(args) > 1:
        if args[1] == '--version':
            print('Running AmesWeather v' + version)
        elif args[1] == '--help' or args[1] == '-h':
            printHelp()
        else:
            # If no help of version command was called,
            # that means it is weather time!

            # TODO: Before we can start looping through comands,
            # we need to figure out which optional
            # arguments are supplied!
            if args[1] == '-M':
                wformat = 'si'
                startingPoint = 2
            elif args[1] not in switcher:
                # if the first value here is not in switcher,
                # it is either the date or WRONG
                wtype = 'historical'
                wdate = stringToDate(args[1])
                if wdate == -1:
                    print('Date Format Error.')
                    return
                rdate = wdate
                if args[2] == '-M':
                    wformat = 'si'
                    startingPoint = 3
                else:
                    startingPoint = 2
            else:
                wdate = datetime.datetime.now()

            for i in range(startingPoint, len(args)):
                fun = switcher.get(args[i], unkown)
                if i == startingPoint:
                    isFirst = 1
                else:
                    isFirst = 0
                s = s + str(fun(args[i], wtype, wformat, wdate, isFirst)) + ","
                if i == len(args)-1:
                    s = s[:-1]
            print(s)
    else:
        print('No arguments provided. Type --help for help.')
