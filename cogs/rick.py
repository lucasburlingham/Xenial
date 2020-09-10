import discord
import os
import random
from discord.ext import commands
from time import sleep

class Fun(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    async def rick(self, ctx):
        await ctx.send(f'https://tenor.com/view/rick-ashtley-never-gonna-give-up-rick-roll-gif-4819894')


def setup(client):
    client.add_cog(Fun(client))