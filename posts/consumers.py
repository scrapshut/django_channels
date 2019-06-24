from channels.generic.websocket import AsyncJsonWebsocketConsumer
class PostConsumer(AsyncJsonWebsocketConsumer):
	async def connect(self):
		await self.accept()
		await self.channel_layer.group_add("posts", self.channel_name)
		print(f"Add {self.channel_name} channel to post's group")
		print('connected')
	async def receive_json(self, message):
		print("receive",message)
	async def disconnect(self,close_code):
		await self.channel_layer.group_discard("posts", self.channel_name)
		print(f"Remove {self.channel_name} channel from users's group")
	async def post_update(self,event):
		await self.send_json(event)
		print('posts',event)
