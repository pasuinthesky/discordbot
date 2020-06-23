# bot.py
import os
import re
import json

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})\n'
          f'guild members:\n'
          f'{guild.members}')
    for u in guild.members:
        print(u.status)
        print(str(u.status) != 'offline')
        for a in u.activities:
            print(a)
            print(json.dumps(json.load(a.timestamps), indent=4))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    s = message.content.lower()
    if not s.startswith('bot,'):
        return

    if 'happy birthday' in s:
        await message.channel.send('Happy Birthday! 🎈🎉')

    if 'say hi to ' in s:
        sub = 'say hi to '
        p = re.sub(r'\W+', '',
                   s[(len(s) - s.find(sub) - len(sub)) * -1:].split()[0])
        await message.channel.send(f'Hi, {p}. How are you? 🎈🎉')

    if 'good night to everyone' in s:
        guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
        for u in guild.members:
            #
            if u != client.user and str(u.status) != 'offline':
                await message.channel.send(
                    f'Good night, {u.name if u.nick is None else u.nick}. :sleeping:\n'
                )


client.run(TOKEN)