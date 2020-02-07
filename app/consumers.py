from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class BasicConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        async_to_sync(
            self.channel_layer.group_add)('global', self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(
            self.channel_layer.group_discard)('global', self.channel_name)

    def receive(self, text_data):
        print(text_data)

    def global_receive(self, event):
        message = event.get('message')
        if message:
            self.send(message)
