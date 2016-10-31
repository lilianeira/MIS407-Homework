#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CyBot Ultimate main module."""

import time
import random
from ExternalDataModules import bus, weather
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
             " You should ask me about CyRide... or weather!")


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


def responseNextBus(ch, txt, data):
    stopnum = txt[-4:]
    busData = bus.getRouteTimes(stopnum)
    if len(busData) == 0:
        talk(ch, "I do not know anything about stop:" + stopnum)
    else:
        responsestr = "Arriving at stop " + stopnum + " in the next 15 minutes.\n"
        for i in range(0, len(busData)):
            responsestr = responsestr + busData[i]["route"] +": "
            for e in range(0, len(busData[i]["predictions"])):
                addition = " bus #" + busData[i]["predictions"][e]["bus"] + " in " + busData[i]["predictions"][e]["min"] + "min"
                if e != len(busData[i]["predictions"]) - 1:
                    addition = addition + ","
                responsestr = responsestr + addition
            responsestr = responsestr + "\n"
        talk(ch, responsestr)

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

# sports talk
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
        "trigger": "what busses are coming to stop 1212",
        "response": responseNextBus
    },
    {
        "trigger": "what busses can i expect at stop 1212",
        "response": responseNextBus
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
