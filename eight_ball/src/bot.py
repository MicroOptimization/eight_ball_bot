"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import discord
import key_retriever
import functions

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        
        self.text_channel_names = []
        self.text_channels = []
        
        for i in client.get_all_channels():
            self.text_channel_names.append(str(i))
            self.text_channels.append(i)
            
        await client.change_presence(activity=discord.Game(name="with Fate"))
        
    async def on_message(self, message):    
        print('Message from {0.author} from {0.channel}: {0.content}'.format(message))
        text = message.content
        words = text.split(" ")

        if len(words) >= 2 and words[1].lower() == "help":
            await message.channel.send("To be implemented")
        elif words[0].lower() == "qqox,":
            await message.author.send('Qqox is dead.')
        elif words[0].lower() == "meb," or words[0].lower() == "mge," or (len(words) >= 3 and words[0].lower() == "magic" and words[1].lower() == "eight" and words[2].lower() == "ball,"):
            await message.channel.send("The Magic Eight Ball has Spoken:")
            await message.channel.send("'{}'".format(functions.get_message()))

client = MyClient()

key = key_retriever.get_key() #Insert your key here

client.run(key)
