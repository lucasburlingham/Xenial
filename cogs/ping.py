import discord
import os
import random
from discord.ext import commands
from time import sleep

class Examples(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: | **Pong!** Client Side Ping is {round(client.latency * 1000)}ms')


def setup(client):
    client.add_cog(Examples(client))