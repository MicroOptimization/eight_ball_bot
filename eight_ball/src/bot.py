"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()

key = "" #Insert your key here

client.run(key)