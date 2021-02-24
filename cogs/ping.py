import discord
from discord import *
from discord.ext import commands

class Diagnostics(commands.Cog):

	
	def __init__(self, client):
		self.client = client
	#this command simply sends back the bots latency in ms
	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'{round(self.client.latency * 1000)}ms')

def setup(client):
	client.add_cog(Diagnostics(client))

