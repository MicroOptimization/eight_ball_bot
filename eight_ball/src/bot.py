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
            
        await client.change_presence(activity=discord.Game(name='with Fate'))
        
        """
        channel = client.get_channel(701760072560148519)
        await channel.send("test")
        """
        
    async def on_message(self, message):    
        print('Message from {0.author} from {0.channel}: {0.content}'.format(message))
        text = message.content
        words = text.split(" ")
        if words[1] == "help":
            await message.channel.send("To talk to me, begin with 'qqox, <message>'")
        elif words[0] == "qqox,":
            await message.channel.send("Hello, I am qqox")
        elif words[2] is not None and words[0].lower() == "magic" and words[1].lower() == "eight" and words[2].lower() == "ball,":
            await message.channel.send("The Magic Eight Ball has Spoken~~~")
            await message.channel.send(functions.get_message())
        #await message.author.send('If only my programmer would allow me to give an answer other than this.')
        #await message.author.send("Spaghetti")
        
client = MyClient()

key = key_retriever.get_key() #Insert your key retrieval method here

client.run(key)