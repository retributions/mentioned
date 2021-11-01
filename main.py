import discord
from discord.ext import commands, tasks
import colorama
from colorama import Fore as F
import os
from os import system
import json
import threading
import requests
import asyncio
import time
import random


system("title " + "Configuration")
#token = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Token: ')
#prefix = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Prefix: ')
os.system('cls')
token = input(f'''{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Token:''')
#token = 'ODA2ODYxOTExNjU1NTc5NjQ4.YImU6w.ju-P0WoTxm8HcYXNp6bVbq_eWVg'#hey dont log me ;)
intents = discord.Intents.all()

intents.members = True


client = discord.Client()  

client = commands.Bot(command_prefix = 'd!', self_bot=True, intents=intents)

client.remove_command('help')

headers = {'Authorization' : f'{token}'}

spam = True

white = discord.Color.from_rgb(255,182,193)

@client.event
async def on_connect():
  print('''
  \033[97m_______   ______   ______    ______   ______  _______   __        ________   ______\033[0m  
\033[97m/       \ /      | /      \  /      \ /      |/       \ /  |      /        | /      \ \033[0m 
\033[32m$$$$$$$  |$$$$$$/ /$$$$$$  |/$$$$$$  |$$$$$$/ $$$$$$$  |$$ |      $$$$$$$$/ /$$$$$$  |\033[0m
\033[32m$$ |  $$ |  $$ |  $$ \__$$/ $$ |  $$/   $$ |  $$ |__$$ |$$ |      $$ |__    $$ \__$$/\033[0m 
\033[32m$$ |  $$ |  $$ |  $$      \ $$ |        $$ |  $$    $$/ $$ |      $$    |   $$      \ \033[0m 
\033[32m$$ |  $$ |  $$ |   $$$$$$  |$$ |   __   $$ |  $$$$$$$/  $$ |      $$$$$/     $$$$$$  |\033[0m
\033[32m$$ |__$$ | _$$ |_ /  \__$$ |$$ \__/  | _$$ |_ $$ |      $$ |_____ $$ |_____ /  \__$$ |\033[0m
\033[32m$$    $$/ / $$   |$$    $$/ $$    $$/ / $$   |$$ |      $$       |$$       |$$    $$/\033[0m 
\033[32m$$$$$$$/  $$$$$$/  $$$$$$/   $$$$$$/  $$$$$$/ $$/       $$$$$$$$/ $$$$$$$$/  $$$$$$/\033[0m  
  ''')

#ifmentionedcommand



@client.listen('on_message')
async def ifmentioned(message):
  if message.author == client.user:
    return
  if str(client.user.id) in message.content:
    print("══════════════════════════════════════════════════")
    print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Mentioned -", f"Mentioned By{F.WHITE}: {message.author}.")
    print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Mentioned -", f"Server{F.WHITE}: {message.guild}")
    print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Mentioned -", f"Channel{F.WHITE}: {message.channel}")
    print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Mentioned -", f"Message Content: {message.content}".replace(f"<@{client.user.id}>" or f"<@!{client.user.id}>", ""))
    print("══════════════════════════════════════════════════")

client.run(token, bot=False)
