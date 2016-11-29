from tkinter import *
from tkinter.ttk import *
import bus
import sports
import weather as weatherModule

window = Tk()

def weather():
    currentweather = weatherModule.today()
    temp = currentWeather["temp"]
    high = currentWeather["max"]
    low = currentWeather["min"]
    cond = currentWeather["summary"]
    response = "Right now in Ames, it is " + str(temp)
    response += "°F and " + cond + ". Today we'll see a high of "
    response += str(high) + "°F "
    response += "and a low of " + str(low) + "°F."
    if high >= 90:
        response += " " + random.choice(extremeTempComments["hot"])
    elif high <= 15:
        response += " " + random.choice(extremeTempComments["cold"])
    return response
#def sports():

#def bus():


team = Label(window, text="Ultimate")
team.grid(row = 0, column = 0, columnspan = 2)

weatherbtn = Button(window, text="Weather", command = weather)
weatherbtn.grid(row = 1, column = 0)

wthdisp = Listbox(window,height=6, width=35)
wthdisp.grid(column = 0, row = 2, rowspan = 4)

busbtn = Button(window, text="Bus", width=12)
busbtn.grid(row = 1, column = 1)

bus_stop = StringVar()
busentry = Entry(window, textvariable = bus_stop, width = 6)
busentry.grid(row = 1, column = 2)

sportbtn = Button(window, text="Sports", width=12)
sportbtn.grid(row = 8, column = 0)

newsbtn = Button(window, text="News", width=12)
newsbtn.grid(row = 8, column = 1)

window.mainloop()
