import discord
from discord import *
from discord.ext import commands

class ChannelControls(commands.Cog):


	def __init__(self, client):
		self.client = client
		print('Loaded Channel Controls....')
#This command essentially looks like >clear 123 and it clears that many messages from the
#channel it is called in, it does count the command message as 1 message
#so to clear 5 messages you would type >clear 6
	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount : int):
		await ctx.message.delete()
		await ctx.channel.purge(limit=amount)
	@clear.error
	async def clear_error(self , ctx , error):
		if isinstance(error , commands.MissingRequiredArgument):
			await ctx.send ('Please specify how many messages you would like to clear')
		if isinstance(error , commands.MissingPermissions):
			await ctx.send ('You do not have permission to do that')

		


def setup(client):
	client.add_cog(ChannelControls(client))