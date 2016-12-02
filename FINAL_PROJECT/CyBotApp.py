from tkinter import *
import bus as busStop
import weather as weatherModule
import News as newsFeed
import webbrowser
import datetime
import sports as Sports

version = "00.06"

window = Tk()


def dateToString(date):
    """turns date obj into a string"""
    format = '%m/%d/%Y'
    newDate = date.strftime(format)
    return newDate


def stampToDate(str):
    return datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=str)


def weather():
    wtype = weathervariable.get()
    if wtype == "today":
        currentWeather = weatherModule.today()
        temp = currentWeather["temp"]
        high = currentWeather["max"]
        low = currentWeather["min"]
        later = currentWeather["cond"]
        cond = currentWeather["summary"]
        response = "Right now in Ames, it is " + str(temp)
        response += "°F and " + cond + ".\n\nToday we'll see a high of "
        response += str(high) + "°F "
        response += "and a low of " + str(low) + "°F."
        response += "\n\n" +later
    else:
        forecast = weatherModule.sevanDay()
        response = ""
        for i in range(0, len(forecast)):
            dateObj = stampToDate(forecast[i]['date'])
            dateString = dateToString(dateObj)
            high = forecast[i]["max"]
            low = forecast[i]["min"]
            cond = forecast[i]["summary"]
            response = response + dateString + "\n"
            response = response + "High of "
            response += str(high) + "°F and a low of "
            response += str(low) + "°F.\n" + cond + "\n\n-----\n\n"
        print(forecast)
    wthdisp.delete(1.0, END)
    wthdisp.insert(END, response)

def sports():
    sportChosen = sportvariable.get()
    response = Sports.getSports(sportChosen)
    sportdisp.delete(1.0, END)
    sportdisp.insert(END, response)

def bus():
    stopNum = bus_stop.get()
    busData = busStop.getRouteTimes(stopNum)
    if len(busData) == 0:
        responsestr = "No buses are arriving in the next 15 minutes for stop " + stopNum;
    else:
        responsestr = "Stop " + stopNum
        responsestr += " in next 15 minutes:\n\n"
        for i in range(0, len(busData)):
            responsestr = responsestr + "" + busData[i]["route"] + " "
            responsestr = responsestr + " (" + busData[i]["descrip"] + "):\n"
            for e in range(0, len(busData[i]["predictions"])):
                addition = " bus #" + busData[i]["predictions"][e]["bus"]
                addition += " in " + busData[i]["predictions"][e]["min"] + "min"
                if e != len(busData[i]["predictions"]) - 1:
                    addition = addition + ","
                responsestr = responsestr + addition
            responsestr = responsestr + "\n\n"
    busdisp.delete(1.0, END)
    busdisp.insert(END, responsestr)


def news():
    theNews = newsFeed.newsPlease()
    newsdisp.delete(1.0, END)
    if len(theNews):
        for i in range(0, len(theNews)):
            newsdisp.insert(END, theNews[i]["title"] + "\n")
            newsdisp.insert(END, theNews[i]["link"], "hlink")
            newsdisp.insert(END, "\n\n")



def initModules():
    weather()
    sports()
    bus()
    news()


def openHLink(event):
    start, end = newsdisp.tag_prevrange("hlink", newsdisp.index("@%s,%s" % (event.x, event.y)))
    webbrowser.open(newsdisp.get(start, end))


window.wm_title("ULTIMATE DESKTOP APP")

team = Label(window, pady=25, text="Ultimate v"+version, font=("Helvetica", 16))
team.grid(row = 0, column = 0, columnspan = 5)

weatherbtn = Button(window, text="Weather", command = weather)
weatherbtn.grid(row = 1, column = 0)

weathervariable = StringVar(window)
weathervariable.set("today")

weatherPick = OptionMenu(window, weathervariable,
                       "today", "7 day")
weatherPick.grid(column = 1, row =1)

wthdisp = Text(window, width=40, padx=10, wrap=WORD, pady=10, height=8, background="white")
wthdisp.grid(column = 0, row = 2, columnspan = 2)
wscroll = Scrollbar(window)
wscroll.grid(column = 2, row = 2, sticky='ns')

wthdisp.configure(yscrollcommand=wscroll.set)
wscroll.configure(command=wthdisp.yview)

busbtn = Button(window, text="Bus Stop (#):", width=12, command = bus)
busbtn.grid(row = 1, column = 3)
bus_stop = StringVar()
bus_stop.set("1088")
busentry = Entry(window, textvariable = bus_stop, width = 6)

busentry.grid(row = 1, column = 4)
busdisp = Text(window, width=40, padx=10, wrap=WORD, pady=10, height=8, background="white")
busdisp.grid(column = 3, row = 2, columnspan = 2)

bscroll = Scrollbar(window)
bscroll.grid(column = 5, row = 2, sticky='ns')

busdisp.configure(yscrollcommand=bscroll.set)
bscroll.configure(command=busdisp.yview)

sportbtn = Button(window, text="Sports", width=12, command = sports)
sportbtn.grid(row = 3, column = 0)


sportvariable = StringVar(window)
sportvariable.set("all")

sportPick = OptionMenu(window, sportvariable,
                       "all", "Men's Basketball", "Woman's Basketball", "Cross Country",
                       "Men's Golf", "Woman's Golf", "Football",
                       "Wrestling", "Track and Field", "Softball",
                       "Gymnastics", "Soccer", "Swimming",
                       "Tennis", "Volleyball")
sportPick.grid(column = 1, row =3)

sportdisp = Text(window, width=40, padx=10, pady=10, wrap=WORD, height=8, background="white")
sportdisp.grid(column = 0, row = 4, columnspan = 2)

sscroll = Scrollbar(window)
sscroll.grid(column = 2, row = 4, sticky='ns')

sportdisp.configure(yscrollcommand=sscroll.set)
sscroll.configure(command=sportdisp.yview)

newsbtn = Button(window, text="News", width=12)
newsbtn.grid(row = 3, column = 3, columnspan = 2)
newsdisp = Text(window, width=40, padx=10, pady=10, wrap=WORD, height=8, background="white")
newsdisp.grid(column = 3, row = 4, columnspan = 2)

nscroll = Scrollbar(window)
nscroll.grid(column = 5, row = 4, sticky='ns')

newsdisp.configure(yscrollcommand=nscroll.set)
nscroll.configure(command=newsdisp.yview)

newsdisp.tag_configure("hlink", foreground='blue', underline=1)
newsdisp.tag_bind("hlink", "<Button-1>", openHLink)


initModules()

window.mainloop()
