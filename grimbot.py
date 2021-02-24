#These are our initial library imports, each one should have a description underneath for clarity as to why it is needed
import discord
#of course to use the discord API we must import discord's python library
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.messages = True
#these Intents are what user data the bot is allowed to collect in the course of it's duties
#.members collects data related to members, and in this bot is used to determine what user joins and what user leaves
#.presences is currently only used to detect if a user reacts to a message, but it could be used to detect if a user is
#online or not
#.messages only collects data related to messages, if a chatbot is requested, it will listen to all channels it is allowed
#to talk in, if that function is not enabled, it should only be using this function to SEND messages related to the
#function called for
import discord.utils
#this is another import for a discord library
import os
#this allows the bot to handle local file structures within itself
import logging
#this allows the bot to produce a .log file for review
from discord import *
#this imports all variables from the discord library, generally a bad practice, but i've found
#some functions refuse to work without this wildcard import oddly enough
from discord.ext import commands, tasks
#another discord library import
from itertools import cycle
#this import is what allows the bots status to cycle via a time constraint
killer = os.environ.get('BOT_TOKEN')
#Please PM the bot Developer for more information on this


# all stage 1 events are in this file
#if you are looking for a specific function or command, check the cogs folder first
#when a command is called for, the bot reaches out to the respective 'cog'
#all commands in here are base level, and don't do much




#this is what allows logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)




#this sets the bots command prefix
client = commands.Bot(command_prefix = '>' , intents = intents)
#this is the status list a later command will cycle through in the background
status = cycle(['Dead by Daylight 2' , 'Games'])
#do not touch this at all, this is how the bot knows where it's extensions are
print('Loading extensions.....')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#this is our initial login for the bot
@client.event
async def on_connect():
    print ('Connecting...')
@client.event
async def on_ready():
    print('Setting status....')
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Spooky Tunes'))
    change_status.start()
    print('-------------------------------')
    print('Welcome: GrimBot')
    print('-------------------------------')


#this event is called when a user tries to use a non-existant command
#the error message can be customized
@client.event
async def on_command_error(ctx , error):
        if isinstance(error , commands.CommandNotFound):
            await ctx.send ('Unrecognized Command')

#do not touch these, or call these commands, these allow us to load and unload the bots extensions
#messing with these will break the bot and require a reboot to fix
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


#this just changes the game status of the bot after a set amount of time
#you can replace minutes with seconds or hours
#to change the status, please see the list below the command prefix setting
@tasks.loop(minutes=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#this detects if a member has joined the server and pushes a message to a channel
#to report it
#disabled for now
#@client.event
#async def on_member_join(member):
#    channel = client.get_channel()#Arrival Channel here
#    membersplit = str(member)
#    member_name , member_discriminator = membersplit.split('#')
#    print(f'{member} has joined the server!')
#    await channel.send(f'Welcome to Grim Hollow {member_name} ! Please take a moment to read the rules before asking for a role')


#this detects if a member has left the server and pushes a message to a channel to 
#to report it
#disabled for now

#@client.event
#async def on_member_remove(member):
#    channel = client.get_channel()#channel for notifying of user leaving
#    membersplit = str(member)
#    member_name , member_discriminator = membersplit.split('#')
#    print(f'{member}has left the server!')
#    await channel.send(f'{member_name} has left the server!')



#this function detects if a user reacts to a specific message and adds a role
#it has been disabled for now but may be used in the future
#@client.event
#async def on_raw_reaction_add(payload , * role : discord.Role):
#    if payload.message_id == :#put a rules message id here to see if a user has reacted to it
#        role = (discord.utils.get(payload.member.guild.roles , name = 'Prospect'))
#        await payload.member.add_roles(role)



client.run(killer)
