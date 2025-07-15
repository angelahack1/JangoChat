# myapp/consumers.py
import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import ChatMessage
# This will allow us to run synchronous database operations in an async context
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("--- WebSocket connect initiated.")
        try:
            self.room_name = 'llm_chat'
            self.room_group_name = f'chat_{self.room_name}'
            print(f"--- Joining room: {self.room_group_name}")

            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
            print("--- WebSocket connection accepted and successful.")

        except Exception as e:
            print(f"!!! CONNECTION FAILED: {e}")
            await self.close()

    async def disconnect(self, close_code):
        print("--- WebSocket disconnected.")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print(f"--- Received message from client: {text_data}")
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            user = self.scope['user']

            if not user.is_authenticated:
                print("!!! User not authenticated. Message rejected.")
                return

            print(f"--- Message parsed: '{message}' from user '{user.username}'")
            await self.save_message(user, message)
            print("--- User message saved to DB.")

            await self.channel_layer.group_send(
                self.room_group_name,
                {'type': 'chat_message', 'message': message, 'username': user.username}
            )
            print("--- User message broadcast to room.")

            # Simulate LLM response
            await asyncio.sleep(1)
            llm_response = f"This is a simulated response to: '{message}'"
            bot_user, _ = await self.get_or_create_bot_user()
            await self.save_message(bot_user, llm_response)
            print("--- Bot message saved to DB.")

            await self.channel_layer.group_send(
                self.room_group_name,
                {'type': 'chat_message', 'message': llm_response, 'username': 'LLM_Bot'}
            )
            print("--- Bot message broadcast to room.")

        except Exception as e:
            print(f"!!! ERROR in receive method: {e}")

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        print(f"--- Sending message to WebSocket: '{message}' from '{username}'")
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    # Synchronous database operations wrapped for async context
    @database_sync_to_async
    def save_message(self, user, message):
        ChatMessage.objects.create(user=user, message=message)

    @database_sync_to_async
    def get_or_create_bot_user(self):
        return User.objects.get_or_create(username='LLM_Bot')

class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("--- ✅ TEST CONSUMER CONNECTED SUCCESSFULLY ✅ ---")
        await self.accept()
