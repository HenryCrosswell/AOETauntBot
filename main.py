from multiprocessing.connection import wait
import discord
from pathlib import Path
import os
from discord import FFmpegPCMAudio
import asyncio


list_of_taunts = os.listdir(Path('./taunt_files'))
def find_taunt(taunt_number):
    taunt = list_of_taunts[taunt_number-1]
    return taunt

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    taunt_number = None

    #finds taunt number from the message
    if message.content.startswith('Taunt'):
        text_channel = message.channel
        for word in message.content.split():
            if len(message.content.split()) == 1:
                await text_channel.send('Please enter a number after "Taunt".')
                break
            if word.isnumeric():
                taunt_number = int(word)               
                if taunt_number > 32:
                    await text_channel.send('Taunt number exceeds max.')
                    return
                if taunt_number < 1:
                    await text_channel.send('Taunt number exceeds min.')
                    return
                break

        #checks if taunt number has been changed and finds the file
        if taunt_number != None:
            taunt_file = find_taunt(taunt_number)
            print(taunt_file)
 
            #checks if message sender is in the voice channel
            try:
                voice_channel = message.author.voice.channel
            except:
                await text_channel.send('User is not in a channel.')
                return
            if voice_channel != None:
                try:
                    vc = await voice_channel.connect()
                    source = FFmpegPCMAudio('taunt_files/'+ taunt_file)
                    print('taunt_files/'+ taunt_file)
                    player = vc.play(source)
                    # disconnect after the player has finished
                    # disconnect after the player has finished
                    while vc.is_playing() != True: #Checks if voice is playing
                        asyncio.sleep(15) #While it's playing it sleeps for 1 second
                        await vc.disconnect() #if not it disconnects
                except discord.ClientException:
                    vc = discord.utils.get(client.voice_clients)
                    source = FFmpegPCMAudio('taunt_files/'+ taunt_file)
                    print('taunt_files/'+ taunt_file)
                    player = vc.play(source)
                    # disconnect after the player has finished
                    while vc.is_playing() != True: #Checks if voice is playing
                        print(vc.is_playing())
                        asyncio.sleep(15) #While it's playing it sleeps for 1 second
                        print(vc.is_playing())
                        await vc.disconnect() #if not it disconnects

client.run('MTAxNTYzMzQ0NjQ4NTM3Mjk0OA.Glya3M.MYwL_repVO26msve0V9OwCbPY_4sjte_BipENk')