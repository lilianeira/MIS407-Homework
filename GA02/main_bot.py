# There is a couple of thing that you need to do to run this script.
# slackclient needs to be installed by pip install slackclient
import time
import os
from slackclient import SlackClient

token = "xoxb-91109580036-FRjGcFWSrRUTJHLJ76sLAO4i"
sc = SlackClient(token)

def list_channels():
    channels_call = sc.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None
def channels_print():
    channels = list_channels()
    if channels:
        print("Channels: ")
        for c in channels:
            print(c['name'] + " (" + c['id'] + ")")
    else:
        print("Unable to authenticate.")

def channel_info(channel_id):
    channel_info = sc.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None

def send_message(channel_id, message):
    sc.api_call("chat.postMessage", channel = channel_id, text = message, username = "pybot", icon_emoji = 'robot_face')

if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Channels: ")
        for c in channels:
            print(c['name'] + " (" + c['id'] + ")")
            detailed_info = channel_info(c['id'])
            if detailed_info:
                print(detailed_info)
            if c['name'] == 'bots':
                send_message(c['id'],c)
                send_message(c['id'], "Hello " + c['name'] + "! It worked!")
    else:
        print("Unable to authenticate.")
