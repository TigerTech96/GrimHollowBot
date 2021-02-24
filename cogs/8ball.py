import discord
from discord import *
from discord.ext import commands
import random
#this import allows the bot to choose from a list randomly

class Games(commands.Cog):


    def __init__(self, client):
        self.client = client
        print('Loaded Games....')

	#this command responds to a question and returns a random answer
    @commands.command()
    async def fortune(self, ctx, * , question):

        responses = [' It is certain.',
                    'It is decidedly so.',
                    'Without a doubt.',
                    'Yes – definitely.',
                    'You may rely on it.',
                    'Signs point to yes',
                    'Yes.',
                    'Outlook good.',
                    'Most likely.',
                    'As I see it, yes.',
                    'Concentrate and ask again.',
                    'Cannot predict now.',
                    'Better not tell you now.',
                    'Ask again later.',
                    'Reply hazy, try again.',
                    'Don\'t count on it.',
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Very doubtful.']
        await ctx.send(f'{random.choice(responses)}')


def setup(client):
    client.add_cog(Games(client))