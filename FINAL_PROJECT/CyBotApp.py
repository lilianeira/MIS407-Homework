from tkinter import *
import bus as busStop
import weather as weatherModule
import News as newsFeed
import sports as Sports

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

def initModules():
    weather()
    sports()
    bus()

window.wm_title("ULTIMATE DESKTOP APP")

team = Label(window, text="Ultimate")
team.grid(row = 0, column = 0, columnspan = 5)

weatherbtn = Button(window, text="Weather", command = weather)
weatherbtn.grid(row = 1, column = 0, columnspan = 2)

wthdisp = Text(window, width=30, padx=10, pady=10, height=6, background="white")
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
busdisp = Text(window, width=30, padx=10, pady=10, height=6, background="white")
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

sportdisp = Text(window, width=30, padx=10, pady=10, height=6, background="white")
sportdisp.grid(column = 0, row = 4, columnspan = 2)

sscroll = Scrollbar(window)
sscroll.grid(column = 2, row = 4, sticky='ns')

sportdisp.configure(yscrollcommand=sscroll.set)
sscroll.configure(command=sportdisp.yview)

newsbtn = Button(window, text="News", width=12)
newsbtn.grid(row = 3, column = 3, columnspan = 2)
newsdisp = Text(window, width=30, padx=10, pady=10, height=6, background="white")
newsdisp.grid(column = 3, row = 4, columnspan = 2)

nscroll = Scrollbar(window)
nscroll.grid(column = 5, row = 4, sticky='ns')

newsdisp.configure(yscrollcommand=nscroll.set)
nscroll.configure(command=newsdisp.yview)
initModules()

window.mainloop()
