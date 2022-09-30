import discord
import os
import asyncio


intents = discord.Intents.all()
client = discord.Client(command_prefix='#', intents=intents)


@client.event ### Here is the message that will appear in console when the connection is well successful
async def on_ready():
    print(f'{client.user} has entered in your room by the window!')


@client.event ### Here is the def that will answer to user commands
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!circus': #here is the command that user needs to type
        while True: #infinite condition
            await message.channel.send('É O ROBS!')
            await asyncio.sleep(8) #Interval
            await message.channel.send('IRIRIRI')
            await asyncio.sleep(8)
            await message.channel.send('GO LOUD')
            await asyncio.sleep(8) 

client.run(os.getenv('TOKEN'))
