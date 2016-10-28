"""CyBot Ultimate main module."""

import time
import random
from fuzzywuzzy import process
from slackclient import SlackClient

token = "xoxb-88140239460-UWfqbhscm4gOevq48BxwLgBY"
sc = SlackClient(token)


def talk(channel, txt):
    """Talk in slack"""
    sc.api_call("chat.postMessage", channel= channel, text= txt)


def unknownResponse(data):
    """What to say when there is nothing to say"""
    txt = data["text"]
    ch = data["channel"]
    responses = [ "I don't understand what you're saying. Perhaps your sound module is broken?",
                  "I don't know what that means.",
                  "Hmm?"]
    talk(ch, random.choice(responses))


def responseHello(data):
    """A friendly greeting"""
    txt = data["text"]
    ch = data["channel"]
    responses = [ "hi!",
                  "hello there!!",
                  "what's up?"]
    talk(ch, random.choice(responses))


def responseHelp(data):
    """Help response"""
    talk(ch, "hi. I am CYBOT. I am here to help!")


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
    }
]


triggerList = []
for i in range(0, len(commands)):
    triggerList.append(commands[i]["trigger"])

def checkResponse(rsp):
    """Check response from slack realtime chat"""
    if rsp != []:
        if rsp[0]["type"] == "message" and "user" in rsp[0] and rsp[0]["text"][:5].lower() == "cybot":
            print(rsp[0])
            str1 = rsp[0]["text"][5:]
            bestMatch = process.extractOne(str1, triggerList)
            matchName = bestMatch[0]
            matchScore = bestMatch[1]
            if matchScore > 55:
                for i in range(0, len(commands)):
                    if commands[i]["trigger"] == matchName:
                        commands[i]["response"](rsp[0])
                        break;
            else:
                unknownResponse(rsp[0])


if __name__ == "__main__":
    sc = SlackClient(token)
    if sc.rtm_connect():
        while True:
            checkResponse(sc.rtm_read())
            time.sleep(1)
    else:
        print("Connection Failed, bad token?")
