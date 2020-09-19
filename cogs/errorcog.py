import discord
import random
import os
from discord.ext import commands
from discord.ext.commands import has_permissions
ignore_command_errors = [
    ("help", commands.MissingRequiredArgument),
    ("docs", commands.MissingRequiredArgument)
    ]
class Error(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self,ctx: commands.Context,error):

        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(description=":x: │ The command you typed does not exist. Run the command **a!help**, which will give you a list of commands.",colour=discord.Colour.purple())
            return await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description=f":x: │ Sorry, {ctx.message.author.mention}, but you do not have the required permissions.",colour=discord.Colour.purple())
            return await ctx.send(embed=embed)
        if not (ctx.command.name, type(error)) in ignore_command_errors:
            if isinstance(error, commands.MissingRequiredArgument):
                embed = discord.Embed(description=f":x: │ What you typed was not complete. Add some arguments?",colour=discord.Colour.purple())
                return await ctx.send(embed=embed)
        if isinstance(error,commands.CommandOnCooldown):
            await ctx.send("Please **wait** before using this command!")

def setup(client):
    client.add_cog(Error(client))
