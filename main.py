import discord
from pathlib import Path
import os

taunt_number = 0

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
                if taunt_number < 1:
                    await text_channel.send('Taunt number exceeds min.')
                break
        if taunt_number != 0:
            taunt_file = find_taunt(taunt_number)
            print('{0} has connected to Discord!'.format(client.user))
            voice_channel = message.author.voice.channel
            vc = await voice_channel.connect()















        if taunt_number == 0:
            await text_channel.send('Please enter a number after "Taunt".')
        taunt_file = find_taunt(taunt_number)

'''
        # only play music if user is in a voice channel
        voice_channel = message.author.voice.channel
        if voice_channel != None:
            await client.connect()
            player = vc.create_ffmpeg_player(taunt_file, after=lambda: print('done'))
            player.start()
            # disconnect after the player has finished
            player.stop()
            await vc.disconnect()
        else:
            await client.channel.send('User is not in a channel.')
'''
client.run('MTAxNTYzMzQ0NjQ4NTM3Mjk0OA.Glya3M.MYwL_repVO26msve0V9OwCbPY_4sjte_BipENk')