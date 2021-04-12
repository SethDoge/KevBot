import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from staying_alive import keep_alive
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '>') #put your own prefix here

@client.event
async def on_ready():
    print("Bot Initialized") #will print "bot online" in the console when the bot is online
    
    
@client.command()
async def chirp(ctx):
    await ctx.send("Chirp Chirp") #simple command so that when you type ">Chirp" the bot will respond with "Chirp Chirp"





keep_alive()
client.run(os.getenv("TOKEN"))