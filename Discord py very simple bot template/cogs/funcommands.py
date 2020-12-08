import discord
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    #EVENTS
    @commands.Cog.listener()
    async def on_ready(self):
        print('FunCommands are Fucking Ready')

    #COMMANDS
    #this commands are very simple, if you want something more interesting contact me on discord: .Bersss#6969
    #first command it will send something (change changeme1 for the name of command)
    @commands.command()
    async def CHANGEME1(self, ctx):
        await ctx.send('WHAT I WILL SAY WRITE HERE')
    #second command it will send a photo its the same of the first one just with f string, u paste the photo url in: PHOTOURL
    @commands.command()
    async def CHANGEME2(self, ctx):
        await ctx.send(f'PHOTOURL')
    #U can copy and paste these commands here to add more of them.

def setup(client):
    client.add_cog(Fun(client))
