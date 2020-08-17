from TwitterAPI import TwitterAPI
import json

consumer_key="SLXZNDCBye3xXsGu1D2enmmrn"
consumer_secret="BYgWcm04CCpVYqYapoddImMuJBaCGNoAecxaLOckNZoEIuNAfw"
access_token_key="1290017590123864065-qqkgsGH4LpyT0I3XM2lfkNatwPvHXm"
access_token_secret="mFQyoSh3WTDMJ6PrYRgKQCuy37pYmh9tdw4Fgm7FguUJI"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

class Twitter_API(object):
    def send_direct_messages(self):
        user_id = "sam_birus"
        message_text = "hi"

        event = {
          "event": {
            "type": "message_create",
            "message_create": {
              "target": {
                "recipient_id": user_id
              },
              "message_data": {
                "text": message_text
              }
            }
          }
        }

        r = api.request('direct_messages/events/new', json.dumps(event))
        print('SUCCESS' if r.status_code == 200 else 'PROBLEM: ' + r.text)

    def get_direct_messages(sef):
        r = api.request('direct_messages/events/list')
        if r.status_code == 200:
          return r
        else:
          raise Exception("No data") 

tapi = Twitter_API()
data = tapi.get_direct_messages()
for item in data:
  print(item)