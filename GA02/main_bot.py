#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CyBot Ultimate main module."""

import time
import random
from ExternalDataModules import bus, weather, sports
from fuzzywuzzy import process
from slackclient import SlackClient

token = "xoxb-88140239460-UWfqbhscm4gOevq48BxwLgBY"
botid = "U2L4471DJ"
sc = SlackClient(token)
version = "00.03"


def talk(channel, txt):
    """Talk in slack"""
    sc.api_call("chat.postMessage", channel=channel,
                text=txt, as_user="true")


# Begin Bot Command Response Functions
def unknownResponse(ch, txt, data):
    """What to say when there is nothing to say"""
    responses = ["I don't understand what you're saying. Perhaps your sound module is broken?",
                  "I don't know what that means.",
                  "Hmm?"]
    talk(ch, random.choice(responses))


# Greetings & Help
def responseHello(ch, txt, data):
    """A friendly greeting"""
    responses = ["hi!",
                  "hello there!!",
                  "what's up?"]
    talk(ch, random.choice(responses))


def responseHelp(ch, txt, data):
    """Help response"""
    talk(ch, "I am CYBOT v" + version + ". I was programmed " +
             " to be totally obsessed with bus stops and weather!" +
             " Try saying one of the following things to me:\n" +
             "cybot, what's the weather\ncybot, when is the next basketball game" +
             "\ncybot, what buses are coming to stop 1088")


# Weather talk
extremeTempComments = {
    "cold": [
        "Try not to freeze!",
        "Brrrrrrrrrrrr.",
        "Perfect weather! (if you're a penguin)",
        "Good luck with that...",
        "According to my calculations, if I could feel temperatures, this would be cold."
    ],
    "hot": [
        "I can't go outside, I'd overheat!!!!",
        "Maybe pack some oven mits for your steering wheel...",
        "That's H. O. T.",
        "According to my calculations, if I could feel temperatures, this would be hot."
    ]
}


def responseCurrentWeather(ch, txt, data):
    """Weather related conversation"""
    currentWeather = weather.getSnapshot()
    temp = currentWeather["temp"]
    high = currentWeather["max"]
    low = currentWeather["min"]
    cond = currentWeather["summary"]
    response = "Right now in Ames, it is " + str(temp) + "°F and " + cond + ". Today we'll see a high of " + str(high) + "°F and a low of " + str(low) + "°F."
    if high >= 90:
        response = response + random.choice(extremeTempComments["hot"])
    elif high <= 15:
        response = response + random.choice(extremeTempComments["cold"])
    talk(ch, response)


def responseTomorrowForecast(ch, txt, data):
    """Responses about tomorrow's forecast"""
    forecast = weather.getSnapshot(True)
    high = forecast["max"]
    low = forecast["min"]
    cond = forecast["summary"]
    response = "Tomorrow in Ames, we'll see a high of " + str(high) + "°F and a low of " + str(low) + "°F. " + cond
    if high >= 90:
        response = response + " " + random.choice(extremeTempComments["hot"])
    elif high <= 15:
        response = response + " " + random.choice(extremeTempComments["cold"])
    talk(ch, response)


# Bus Talk
def responseNextBus(ch, txt, data):
    stopnum = txt[-4:]
    busData = bus.getRouteTimes(stopnum)
    if len(busData) == 0:
        talk(ch, "No buses are arriving in the next 15 minutes for stop "
        + stopnum)
    else:
        responsestr = "Arriving at stop " + stopnum + " in the next 15 minutes:\n"
        for i in range(0, len(busData)):
            responsestr = responsestr + "*" + busData[i]["route"] +"* "
            responsestr = responsestr + " (" + busData[i]["descrip"] + "):"
            for e in range(0, len(busData[i]["predictions"])):
                addition = " `bus #" + busData[i]["predictions"][e]["bus"] + "` in " + busData[i]["predictions"][e]["min"] + "min"
                if e != len(busData[i]["predictions"]) - 1:
                    addition = addition + ","
                responsestr = responsestr + addition
            responsestr = responsestr + "\n"
        talk(ch, responsestr)


# Sports Talk
def responseAllSports(ch, txt, data):
    rstr = sports.AllSports()
    talk(ch, rstr)

def responseSportsMB(ch, txt, data):
    rstr = sports.BasketballM()
    talk(ch, rstr)

def responseSportsWB(ch, txt, data):
    rstr = sports.BasketballW()
    talk(ch, rstr)

def responseSportsCC(ch, txt, data):
    rstr = sports.CrossCountry()
    talk(ch, rstr)

def responseSportsMG(ch, txt, data):
    rstr = sports.GolfM()
    talk(ch, rstr)

def responseSportsWG(ch, txt, data):
    rstr = sports.GolfW()
    talk(ch, rstr)

def responseSportsFB(ch, txt, data):
    rstr = sports.Football()
    talk(ch, rstr)

def responseSportsWR(ch, txt, data):
    rstr = sports.Wrestling()
    talk(ch, rstr)

def responseSportsTF(ch, txt, data):
    rstr = sports.TrackField()
    talk(ch, rstr)

def responseSportsSB(ch, txt, data):
    rstr = sports.Softball()
    talk(ch, rstr)

def responseSportsGYM(ch, txt, data):
    rstr = sports.Gymnastics()
    talk(ch, rstr)

def responseSportsSC(ch, txt, data):
    rstr = sports.Soccer()
    talk(ch, rstr)

def responseSportsSW(ch, txt, data):
    rstr = sports.Swimming()
    talk(ch, rstr)

def responseSportsTN(ch, txt, data):
    rstr = sports.Tennis()
    talk(ch, rstr)

def responseSportsVB(ch, txt, data):
    rstr = sports.Volleyball()
    talk(ch, rstr)

# End Bot Command Response Functions


commands = [
    # Greetings
    {
        "trigger": "hello",
        "response": responseHello
    },
    {
        "trigger": "hi there",
        "response": responseHello
    },
    # Help
    {
        "trigger": "who are you",
        "response": responseHelp
    },
    {
        "trigger": "what is your mission",
        "response": responseHelp
    },
    {
        "trigger": "what can you do",
        "response": responseHelp
    },
    {
        "trigger": "help me",
        "response": responseHelp
    },
    # Current Weather
    {
        "trigger": "what's it like outside",
        "response": responseCurrentWeather
    },
    {
        "trigger": "what is the current weather",
        "response": responseCurrentWeather
    },
    {
        "trigger": "what are the current conditions",
        "response": responseCurrentWeather
    },
    {
        "trigger": "what is the weather like",
        "response": responseCurrentWeather
    },
    {
        "trigger": "what is the weather",
        "response": responseCurrentWeather
    },
    {
        "trigger": "tell me the current weather",
        "response": responseCurrentWeather
    },
    {
        "trigger": "what's the weather right now",
        "response": responseCurrentWeather
    },
    # Tomorrow's weather
    {
        "trigger": "what's the weather supposed to be tomorrow",
        "response": responseTomorrowForecast
    },
    {
        "trigger": "what's tomorrow's forecast",
        "response": responseTomorrowForecast
    },
    {
        "trigger": "what'll it be like tomorrow",
        "response": responseTomorrowForecast
    },
    {
        "trigger": "what is tomorrow's weather",
        "response": responseTomorrowForecast
    },
    # Next Bus for a Particular Stop?
    {
        "trigger": "i'm at stop 1212",
        "response": responseNextBus
    },
    {
        "trigger": "i am at bus stop 1212",
        "response": responseNextBus
    },
    {
        "trigger": "what buses are coming to stop 1212",
        "response": responseNextBus
    },
    {
        "trigger": "what buses can i expect at stop 1212",
        "response": responseNextBus
    },
    # Iowa State Sports Events Triggers!
    # All sports
    {
        "trigger": "what iowa state athletics events are coming up",
        "response": responseAllSports
    },
    {
        "trigger": "what games are coming up",
        "response": responseAllSports
    },
    {
        "trigger": "what's going on in isu sports",
        "response": responseAllSports
    },
    {
        "trigger": "what's coming up in sports",
        "response": responseAllSports
    },
    # Men's Basketball
    {
        "trigger": "when are the next mens basketball games",
        "response": responseSportsMB
    },
    {
        "trigger": "when is the next men's basketball game",
        "response": responseSportsMB
    },
    {
        "trigger": "what's coming up in men's basketball",
        "response": responseSportsMB
    },
    # Woman's basketball
    {
        "trigger": "when are the next women's basketball games",
        "response": responseSportsWB
    },
    {
        "trigger": "when is the next women's basketball game",
        "response": responseSportsWB
    },
    {
        "trigger": "what's coming up in women's basketball",
        "response": responseSportsWB
    },
    # Cross Country
    {
        "trigger": "when is the next cross country meet",
        "response": responseSportsCC
    },
    {
        "trigger": "when are the next cross country meets",
        "response": responseSportsCC
    },
    {
        "trigger": "what's coming up in cross country",
        "response": responseSportsCC
    },
    # MEn's Golf
    {
        "trigger": "when is the next men's golf tournament",
        "response": responseSportsMG
    },
    {
        "trigger": "when is the next men's golf competition",
        "response": responseSportsMG
    },
    {
        "trigger": "what's coming up in men's golf?",
        "response": responseSportsMG
    },
    # Woman's Golf
    {
        "trigger": "when is the next women's golf tournament",
        "response": responseSportsWG
    },
    {
        "trigger": "what is the next women's golf competitiont",
        "response": responseSportsWG
    },
    {
        "trigger": "what's coming up in women's golf",
        "response": responseSportsWG
    },
    # Football
    {
        "trigger": "when are the next football games",
        "response": responseSportsFB
    },
    {
        "trigger": "when is the next football game",
        "response": responseSportsFB
    },
    {
        "trigger": "what's coming up in football",
        "response": responseSportsFB
    },
    # Wrestling
    {
        "trigger": "when is the next wrestling meet",
        "response": responseSportsWR
    },
    {
        "trigger": "when are the next wrestling meets",
        "response": responseSportsWR
    },
    {
        "trigger": "what's coming up in wrestling",
        "response": responseSportsWR
    },
    # Track and Field
    {
        "trigger": "when is the next track meet",
        "response": responseSportsTF
    },
    {
        "trigger": "when are the upcoming track meets",
        "response": responseSportsTF
    },
    {
        "trigger": "what's coming up in track and field",
        "response": responseSportsTF
    },
    # Softball
    {
        "trigger": "when is the next softball game",
        "response": responseSportsSB
    },
    {
        "trigger": "when are the next softball games",
        "response": responseSportsSB
    },
    {
        "trigger": "what's coming up in softball",
        "response": responseSportsSB
    },
    # Gymnastics
    {
        "trigger": "what in the next gymnastics meet",
        "response": responseSportsGYM
    },
    {
        "trigger": "when are the next gymnastics meets",
        "response": responseSportsGYM
    },
    {
        "trigger": "what's coming up in gymnastics",
        "response": responseSportsGYM
    },
    # Soccer
    {
        "trigger": "when is the next soccer game",
        "response": responseSportsSC
    },
    {
        "trigger": "when is the next soccer match",
        "response": responseSportsSC
    },
    {
        "trigger": "what's coming up in soccer",
        "response": responseSportsSC
    },
    # Swimming
    {
        "trigger": "when is the next swim meet",
        "response": responseSportsSW
    },
    {
        "trigger": "when is the next swimming competition",
        "response": responseSportsSW
    },
    {
        "trigger": "what's coming up in swimming",
        "response": responseSportsSW
    },
    # Tennis
    {
        "trigger": "when is the next tennis match",
        "response": responseSportsTN
    },
    {
        "trigger": "when is the next tennis game",
        "response": responseSportsTN
    },
    {
        "trigger": "what's coming up in tennis",
        "response": responseSportsTN
    },
    # Volleyball
    {
        "trigger": "when is the next volleyball game",
        "response": responseSportsVB
    },
    {
        "trigger": "what is the next volleyball match",
        "response": responseSportsVB
    },
    {
        "trigger": "what's coming up in volleyball",
        "response": responseSportsVB
    }
]


triggerList = []
for i in range(0, len(commands)):
    triggerList.append(commands[i]["trigger"])


def checkResponse(rsp):
    """Check response from slack realtime chat"""
    for indx in range(0, len(rsp)):
        if rsp[indx]["type"] == "message" and "user" in rsp[indx]:
            botMentioned = False
            str1 = ""
            if rsp[indx]["text"][:5].lower() == "cybot":
                botMentioned = True
                str1 = rsp[indx]["text"][5:]
            elif rsp[indx]["text"][:12] == "<@" + botid + ">":
                botMentioned = True
                str1 = rsp[indx]["text"][12:]
            if rsp[indx]["user"] == botid:
                botMentioned = False
                print("bot taked")
            if botMentioned:
                print(rsp[indx])
                bestMatch = process.extractOne(str1, triggerList)
                matchName = bestMatch[0]
                matchScore = bestMatch[1]
                txt = rsp[indx]["text"]
                ch = rsp[indx]["channel"]
                if matchScore > 55:  # we can probably tweak this.
                    for i in range(0, len(commands)):
                        if commands[i]["trigger"] == matchName:
                            commands[i]["response"](ch, txt, rsp[indx])
                            break
                else:
                    unknownResponse(ch, txt, rsp[indx])
        elif rsp[indx]["type"] == "hello":
            # bot has connected!
            print("Cybot connected to slack.")


if __name__ == "__main__":
    sc = SlackClient(token)
    if sc.rtm_connect():
        while True:
            checkResponse(sc.rtm_read())
            time.sleep(1)
    else:
        print("Connection Failed, bad token?")
