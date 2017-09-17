import requests
import json

class SendMessage:

    def __init__(self, result):

        response_msg = {}
        response_msg = {"message" : {
                "text" : result
            }
        }
        #response_msg['message']['text'] = result
        response_msg['recipient'] = {}
        response_msg['recipient']['id'] = '1642333859144198'

        post_message_url = 'https://graph.facebook.com/v2.9/me/messages?access_token=%s' % EAACS4LSlOPkBAPkMXnfAHZBJwS2qu85cf5QZCuRjeZCJxESOh40OVfW771QT5dVTHoQm6hBN4l5E5kr9OYqZBdRIFRFBMEWvp00w3cJG7avrZBoS6ZAhqJgZC2hr0tzvXZAUXIN0yXt4SJZAZBWFbZA3nPPnKAW96e0HqTIFBFdwYb9AX2EbblRu6of
        # response_msg = json.dumps({"recipient": {"id": messenger_id}, "message": self.message_attachment})
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"},
                               data=json.dumps(response_msg))

        print status.json()

        #r = requests.post(SLACK_APP_WEBHOOK, data=json.dumps({"text": status.text}))
