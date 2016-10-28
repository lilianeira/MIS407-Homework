"""CyBot Ultimate main module."""

import time
import random
from fuzzywuzzy import process
from slackclient import SlackClient

token = "xoxb-88140239460-UWfqbhscm4gOevq48BxwLgBY"
sc = SlackClient(token)
version = "00.02"


def talk(channel, txt):
    """Talk in slack"""
    sc.api_call("chat.postMessage", channel= channel,
                text= txt, icon_url="https://avatars.slack-edge.com/2016-10-06/88155519905_6902631a78d89f365321_72.png",
                username="Cy Bot")


# Begin Bot Command Response Functions
def unknownResponse(ch, txt, data):
    """What to say when there is nothing to say"""
    responses = [ "I don't understand what you're saying. Perhaps your sound module is broken?",
                  "I don't know what that means.",
                  "Hmm?"]
    talk(ch, random.choice(responses))


def responseHello(ch, txt, data):
    """A friendly greeting"""
    responses = [ "hi!",
                  "hello there!!",
                  "what's up?"]
    talk(ch, random.choice(responses))


def responseHelp(ch, txt, data):
    """Help response"""
    talk(ch, "hi. I am CYBOT v" + version + ". I am here to help!")

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
    }
]


triggerList = []
for i in range(0, len(commands)):
    triggerList.append(commands[i]["trigger"])

def checkResponse(rsp):
    """Check response from slack realtime chat"""
    for indx in range(0, len(rsp)):
        if rsp[indx]["type"] == "message" and "user" in rsp[indx] and rsp[indx]["text"][:5].lower() == "cybot":
            print(rsp[indx])
            str1 = rsp[indx]["text"][5:]
            bestMatch = process.extractOne(str1, triggerList)
            matchName = bestMatch[0]
            matchScore = bestMatch[1]
            txt = rsp[indx]["text"]
            ch = rsp[indx]["channel"]
            if matchScore > 55: # we can probably tweak this.
                for i in range(0, len(commands)):
                    if commands[i]["trigger"] == matchName:
                        commands[i]["response"](ch, txt, rsp[indx])
                        break;
            else:
                unknownResponse(ch, txt, rsp[indx])
        elif rsp[indx]["type"] == "hello":
            # bot has connected!
            print("Cybot connected to slack.");


if __name__ == "__main__":
    sc = SlackClient(token)
    if sc.rtm_connect():
        while True:
            checkResponse(sc.rtm_read())
            time.sleep(1)
    else:
        print("Connection Failed, bad token?")
