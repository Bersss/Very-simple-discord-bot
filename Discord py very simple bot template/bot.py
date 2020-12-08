import discord
import os
from discord.ext import commands
intents = discord.Intents().all()
client = commands.Bot(command_prefix = '.', intents = intents)
client.remove_command('help')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


#here you change the bot's status to the thing the will be written in his game activity.
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('WRITE-HERE-WHAT-UR-BOT-IS-PLAYING'))
    print('Your Bot Is Fucking Ready')

#here the bot adds automatically role to someone when he joins, you need to change in change me to name of role.
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name = "CHANGE-ME")
    await member.add_roles(role)

#the help command, you dont need to touch the admin commands, you can change the fun commands where its written change me.
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
    colour = discord.Colour.blue()
    )
    embed.set_author(name='Bot help that u asked for (:')
    embed.set_footer(text='Bot made by Bers#6969')
    embed.add_field(name='Fun Commands:', value='Change-me', inline=False)
    embed.add_field(name='Admin Commands:', value='ban- Use this command then tag user and reason. \n kick- Use this command then tag user and reason. \n clear- Use this command then write number of messages u want to clear.', inline=False)
    embed.add_field(name='Suggestions for our bot:', value='If u have suggestions for the bot write to Bers#6969 about it, it will help', inline=False)
    await author.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#IMPORTANT!! PUT UR TOKEN HERE ON CHANGEME
client.run('CHANGEME')
