from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import weather as weatherModule
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
    sportTxt.set("Sport goes here")



window.title('ULTIMATE DESKTOP APP')
window.configure(background = '#e1d8b9')
window.style = ttk.Style()
window.style.configure('TFrame', background = '#e1d8b9')
window.style.configure('TButton', background ='#e1d8b9', font = ('Arial', 12))
window.style.configure('TLabel', background ='#e1d8b9')
window.style.configure('TLabel', background ='#e1d8b9', font=('Arial', 12))
window.style.configure('Header.TLabel', font = ('Arial',18,'bold'))
window.frame_header = ttk.Frame(window)
window.frame_header.pack()
window.logo = PhotoImage(file = 'iowalogo.gif')
window.logo = window.logo.subsample(5,5)
ttk.Label(window.frame_header, image = window.logo).grid(row = 0, column = 0)
title = ttk.Label(window.frame_header, text = "Welcome to ULTIMATE Desktop App", style = 'Header.TLabel')
title.grid(row = 0, column =1)


window.frame_content = ttk.Frame(window)
window.frame_content.pack()
weatherbtn = ttk.Button(window.frame_content, text = 'Weather',command = weather)
weatherbtn.grid(row = 0, column =1, padx =5, sticky ='sw')
weatherTxt = StringVar()
weatherTxt.set("Hit button to load weather data.")
weatherentry = Message(window.frame_content, width = 50,font = ('Arial', 10),textvariable=weatherTxt)
weatherentry.grid(row = 1, column = 0, columnspan=3,padx =5)



sportbtn = ttk.Button(window.frame_content, text = 'Specific Sport Schedule',command = sports)
sportbtn.grid(row = 6, column =1, padx =5)
sporttree = ttk.Treeview(window.frame_content)
sporttree.grid(row = 7, column = 0, rowspan=3)
sporttree.insert('','0','item1',text='Basketball')
sporttree.insert('','1','item2',text='Football')
sporttree.insert('','2','item3',text='Baseball')
sporttree.insert('','end','item4',text='Soccer')
sportTxt = StringVar()
sportTxt.set("Click on Sports to view upcoming sport schedules")
sportmes = Message(window.frame_content,width = 50, font = ('Arial', 10),textvariable=sportTxt)
sportmes.grid(row = 7, column = 1, rowspan = 3, columnspan = 2, padx=5)



busbtn = ttk.Button(window.frame_content, text = "Bus Stop (#):", width =12)
busbtn.grid(row=0, column =4, padx =5)
bus_stop = StringVar()
busentry = ttk.Entry(window.frame_content, textvariable = bus_stop, width = 12)
busTxt = StringVar()
busTxt.set("Click Bus to see buses coming in the next 15 minutes.")
busentry.grid(row = 0, column = 5,padx =5)
busInfo = StringVar()
busmes = Message(window.frame_content, width = 150, padx =10,pady=10, textvariable=busTxt)
busmes.grid(column = 4, row = 1, columnspan=3, padx=5)

newsbtn = ttk.Button(window.frame_content, text = "News", width =12)
newsbtn.grid(row = 6, column = 5, padx=5)
newsInfo = StringVar()
newsInfo.set("News Goes Here")
newsmes = Message(window.frame_content, width = 150, padx =10, pady=10, textvariable=newsInfo)
newsmes.grid(row = 7, column =4, rowspan = 3, columnspan = 2, padx=5)
