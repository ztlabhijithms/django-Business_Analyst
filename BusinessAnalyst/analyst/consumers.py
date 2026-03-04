import json
from channels.generic.websocket import AsyncWebsocketConsumer

class BusinessConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)

        idea = data["idea"]

        response = f"Analyzing business idea: {idea}"

        await self.send(text_data=json.dumps({
            "message": response
        }))