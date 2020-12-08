import discord
from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    #EVENTS
    @commands.Cog.listener()
    async def on_ready(self):
        print('AdminCommands are Fucking Ready')

    #COMMANDS
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=0):
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f'I cleared {amount} messages.')
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("WHAT ARE YOU TRYING TO DO?!?!?! you don't have premissions.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason="no reason"):
            await member.kick(reason=reason)
            await ctx.send(f'I kicked: {member.mention} because: {reason}')
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("WHAT ARE YOU TRYING TO DO?!?!?! you don't have premissions.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member : discord.Member, *, reason="no reason"):
            await member.ban(reason=reason)
            await ctx.send(f'I banned: {member.mention} because: {reason}')
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("WHAT ARE YOU TRYING TO DO?!?!?! you don't have premissions.")




def setup(client):
    client.add_cog(Admin(client))
