import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class WSConsumer(WebsocketConsumer):
  def connect(self):
    # to access user
    # self.user = self.scope["user"]
    self.room_group_name = self.scope['url_route']['kwargs']['room_name']
    print('ws connection established ...')

    async_to_sync(self.channel_layer.group_add)(
      self.room_group_name,
      self.channel_name,
    )
    
    self.accept()
    self.send(text_data=json.dumps({
      'message': 'connection established'
    }))

  def disconnect(self, close_code):
    pass

  def notify(self, event):
    message = event['message']
    self.send(text_data=json.dumps({
      'message': message
    }))
