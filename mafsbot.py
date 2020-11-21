#mafsbot.py

import os
import random
from calculator.simple import SimpleCalculator

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def calc(rawtxt):
    expression = rawtxt.replace('mafs', '')
    proc = SimpleCalculator()
    proc.run(expression)
    ans = proc.lcd
    return ans



@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('mafs'):
        if message.content.find('help') != -1:
            await message.channel.send('heya mate! this is a very dumb calculator bot. send your expression with spaces between the digits. if you\'re lucky you\'ll get the right answer')
        else:
            x = random.choice(['right', 'wrong'])
            if x=='wrong':
                response = int(calc(message.content))
                p = random.uniform(response-5, response+5)
                await message.channel.send(p)
            else:
                response = calc(message.content)
                await message.channel.send(response)
            
        

client.run(TOKEN)