import os
import discord
import random
from discord.ext import commands
from time import sleep
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = 'a!')

hello = ["Hello!", "Hallo!", "Bonjour!", "Ciao!", "¡Hola!",
             "Hej!", "Ahoj!", "Aloha!", "Привет!", "Χαίρετε!",
             "你好!", "こんにちは!", "여보세요!", "!مرحبا", "हैलो!"]

vowels = ["a","e","i","o","u","y"]

consonants = ["b","c","d","f","g","h","j","k","l","m", \
                 "n","p","q","r","s","t","v","w","x","z"]

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
    activity=discord.Game(f"Type \'a!help\' for commands | On {len(client.guilds)} guilds"))
    print('Xenial Bot is online!')
           
@client.command()
async def rubbish(ctx):
    sentence = ""
    for i in range(random.randrange(3,7)):
        word = str()
        for j in range(random.randrange(1,5)):
            word = word + random.choice(consonants) + random.choice(vowels)
        sentence = sentence + word + " "
    await ctx.send(sentence.capitalize().rstrip() + random.choice(["!","?","."]))
    
@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: | **Pong!** Client Side Ping Latency took {round(client.latency * 1000)}ms!')

@client.command()
async def hello(ctx):
    await ctx.send(random.choice(hello))
              
@client.command()
async def code(ctx):
    await ctx.send(f'Xenial\'s source code is avalaible at GitHub: https://github.com/tuxedlinux/Xenial/')

@client.command()
async def invite(ctx):
    await ctx.send(f'If you want to invite Xenial to your server, use this link: https://discord.com/api/oauth2/authorize?client_id=756471287442047056&permissions=8&scope=bot')
    
@client.command()
async def about(ctx):
    await ctx.send(f'Xenial is a Discord bot by tuxed, written in Python3. Licensed under MIT, meaning that it\'s open-source and you are free to distribute your own modifications of the bot.')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['DISCORD_TOKEN'])
