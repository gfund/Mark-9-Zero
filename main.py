

# Gunnar Funderburk
from webs import keep_alive
import discord
import os



import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import asyncio

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=',',intents=intents)
@bot.event
async def on_guild_join(guild):
   
  
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
          
            await channel.send("https://tenor.com/view/iron-man-mark42-tony-stark-iron-man3-gif-13372101")
            
        break 

@bot.event
async def on_ready():
     
   
     f = open("onrestarts.txt", "r")
     notify=False
     settings=f.readlines()
    

     notify=True if ("notify"==settings[0]) else False
       
     if(notify):

      user=await bot.fetch_user(os.environ.get("userx"))
      await user.send("Booted Systems")
     print("Booted Systems")
    

@bot.event
async def on_member_join(member):
    if member is bot:
      print("BOT")
    
        
keep_alive()

TOKEN=os.environ.get("DISCORD_BOT_SECRET")

bot.run(TOKEN)

