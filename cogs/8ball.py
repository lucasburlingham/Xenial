import discord
import os
import random
from discord.ext import commands
from time import sleep

class Fun(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command(aliases=["8ball"])
    async def _8ball(self,ctx,arg):
        responses = ["It is certain.",

                    "It is decidedly so...",

                    "Without a doubt.",

                    "Yes, definitely.",

                    "You may rely on it.",

                    "As I see it, yes.",

                    "Most likely.",

                    "All good..",

                    "Yes.",

                    "Signs point to yes.",

                    "Reply hazy, try again....",

                    "Ask again later.",

                    "Better not tell you now....",

                    "Cannot predict now....",

                    "Concentrate and ask again!",

                    "Don't count on it.",

                    "My reply is no.",

                    "My sources say no.",

                    "Uh, no.",

                    "Very doubtful."
    ]

        await ctx.send(random.choice(responses))

def setup(client):
    client.add_cog(Fun(client))