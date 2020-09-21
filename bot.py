import os
import discord
import random
from discord.ext import commands
from time import sleep
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = 'a!')

hello = ["Hello!", "Hallo!", "Bonjour!", "Ciao!", "¡Hola!",
             "Hej!", "Ahoj!", "Aloha!", "Привет!", "Χαίρετε!",
             "你好!", "こんにちは!", "여보세요!", "!مرحبا", "हैलो!", "Salut!"]

vowels = ["a","e","i","o","u","y"]

consonants = ["b","c","d","f","g","h","j","k","l","m", \
                 "n","p","q","r","s","t","v","w","x","z"]

@client.command()
async def docs(ctx,*,arg):
    distros = {
    "ubuntu": "https://docs.ubuntu.com/",
    "arch": "https://wiki.archlinux.org/",
    "gentoo": "https://wiki.gentoo.org/wiki/Main_Page",
    "fedora": "https://docs.fedoraproject.org/en-US/docs/",
    "debian": "https://www.debian.org/doc/",
    "manjaro": "https://wiki.manjaro.org",
    "opensuse": "https://doc.opensuse.org/",
    "kali": "https://www.kali.org/docs/",
    "zorin": "https://zorinos.com/",
    "mint": "https://linuxmint.com/documentation.php",
    "venom": "https://osdn.net/projects/venomlinux/wiki/FrontPage",
    "elementary": "https://elementary.io/docs",
    "clear": "https://docs.clearos.com/en"
    }
    distro = distros[arg]
    if arg in distros:
        await ctx.send(f"Here are the officials docs for {arg}: {distro}")

        # error handling for docs
@docs.error
async def docs_error(ctx,error) :
    if isinstance(error, commands.MissingRequiredArgument):
            author = ctx.message.author
            embed = discord.Embed(
            colour = discord.Colour.orange()
            )
            embed.set_author(name='Available distro docs:')
            embed.add_field(name='Ubuntu',value = "ubuntu",inline=False)
            embed.add_field(name='Debian',value = "debian", inline=False)
            embed.add_field(name='Arch',value = "arch",inline=False)
            embed.add_field(name='Fedora',value = "fedora",inline=False)
            embed.add_field(name='Gentoo',value = "gentoo",inline=False)
            embed.add_field(name='Zorin',value = "zorin",inline=False)
            embed.add_field(name="Manjaro",value="manjaro",inline=False)
            embed.add_field(name="openSUSE",value="opensuse",inline=False)
            embed.add_field(name="Kali",value="kali",inline=False)
            embed.add_field(name="Mint",value="mint",inline=False)
            embed.add_field(name="Venom",value="venom",inline=False)
            embed.add_field(name="ElementaryOS",value="elementary",inline=False)
            embed.add_field(name="ClearOS",value="clear",inline=False)
            await ctx.send(embed=embed)

ignore_command_errors = [ #ignore these commands when there's an error
    ("help", commands.MissingRequiredArgument),
    ("docs", commands.MissingRequiredArgument)
    ]

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
async def compgen(ctx,*,arg):
    if arg == "-c":
        await ctx.send("https://fossbytes.com/a-z-list-linux-command-line-reference/")
        
        
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['DISCORD_TOKEN'])
