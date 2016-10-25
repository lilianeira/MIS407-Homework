import os
import time
from slackclient import SlackClient


token = "xoxb-91109580036-FRjGcFWSrRUTJHLJ76sLAO4i"

BOT_NAME = 'starterbot'

slack_client = SlackClient(token)


if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
        print("could not find bot user with the name " + BOT_NAME)
'''
if sc.rtm_connect():
    while True:
        new_evts = sc.rtm_read()
    for evt in new_evts:
      print(evt)
      if "type" in evt:
        if evt["type"] == "message" and "text" in evt:
          message=evt["text"]
else:
    print("Conncetion Failed, invalid token?")
'''


'''
app = Flask(__name__)

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')

@app.route('/slack', methods = ['POST'])
def inbound():
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
    return Response(), 200


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')


if __name__ == "__main__":
    app.run(debug=True)
'''
