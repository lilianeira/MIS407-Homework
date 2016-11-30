from tkinter import *
import bus as busStop
import sports as sportAll
import weather as weatherModule
import News as newsFeed

window = Tk()

def weather():
    currentWeather = weatherModule.today()
    temp = currentWeather["temp"]
    high = currentWeather["max"]
    low = currentWeather["min"]
    cond = currentWeather["summary"]
    response = "Right now in Ames: \n" + str(temp)
    response += "°F and " + cond + ".\n\nToday:\nHigh: "
    response += str(high) + "°F\nLow:"
    response += " " + str(low) + "°F."
    weatherTxt.set(response)

def sports():
    sportinfo = sportAll.AllSports()
    sportTxt.set(sportinfo)

def bus(bus_stop):
    busStopInfo = busStop.getRouteTimes(bus_stop)
    busTxt.set(busStopInfo)

def initModules():
    weather()
    sports()
    bus()

window.wm_title("ULTIMATE DESKTOP APP")

team = Label(window, text="Ultimate")
team.grid(row = 0, column = 0, columnspan = 2)

weatherbtn = Button(window, text="Weather", command = weather)
weatherbtn.grid(row = 1, column = 0)
weatherTxt = StringVar()
weatherTxt.set("Hit button to load weather data.")
wthdisp = Message(window, width=150, padx=10, pady=10, textvariable=weatherTxt, background="white")
wthdisp.grid(column = 0, row = 2, rowspan = 4, columnspan = 32)

busbtn = Button(window, text="Bus Stop (#):", width=12)
busbtn.grid(row = 1, column = 33)
bus_stop = StringVar()
busentry = Entry(window, textvariable = bus_stop, width = 6)
busTxt = StringVar()
busTxt.set("Click Bus to see buses coming in the next 15 minutes.")
busentry.grid(row = 1, column = 34)
busInfo = StringVar()
busdisp = Message(window, width=150, padx=10, pady=10, textvariable=busTxt, background="white")
busdisp.grid(column = 33, row = 2, rowspan = 4, columnspan = 32)

sportTxt = StringVar()
sportTxt.set("Click on Sports to view upcoming sport schedules")
sportbtn = Button(window, text="Sports", width=12, command = sports)
sportbtn.grid(row = 8, column = 0)
sportdisp = Message(window, width=150, padx=10, pady=10, textvariable=sportTxt, background="white")
sportdisp.grid(column = 0, row = 9, rowspan = 12, columnspan = 32)

newsbtn = Button(window, text="News", width=12)
newsbtn.grid(row = 8, column = 33)

window.mainloop()

initModules()
