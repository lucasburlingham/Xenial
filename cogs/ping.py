import os
import discord
from discord.ext import commands
import random

class Examples(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f':ping_pong: | Pong! Client Side Latency is**{round(self.client.latency * 1000)}ms**')

def setup(client):
    client.add_cog(Examples(client))
