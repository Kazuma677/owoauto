import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio

import os

#-----SETUP-----#

prefix = "!"

#use the .env feature to hide your token

token = os.getenv("TOKEN")

#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)






@bot.event
async def on_ready():
    activity = discord.Game(name="", type=4)
    await bot.change_presence(status=discord.Status.invisible, activity=activity)
    print(f'''{Fore.RED}
██╗░░██╗███████╗██████╗░██╗
██║░░██║██╔════╝██╔══██╗██║
███████║█████╗░░██████╔╝██║
██╔══██║██╔══╝░░██╔═══╝░██║
██║░░██║███████╗██║░░░░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝{Fore.RED}
▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░ 
    ░     ░ ░  ░  ░▒ ░ ▒░░  
  ░         ░     ░░   ░ ░    
            ░  ░   ░     

{Fore.GREEN}

 ________  ________  ___                                                                                                                                                                                     
|\   __  \|\   __  \|\  \                                                                                                                                                                                    
\ \  \|\  \ \  \|\  \ \  \                                                                                                                                                                                   
 \ \   __  \ \   _  _\ \  \                                                                                                                                                                                  
  \ \  \ \  \ \  \\  \\ \  \ ___                                                                                                                                                                             
   \ \__\ \__\ \__\\ _\\ \__\\__\                                                                                                                                                                            
    \|__|\|__|\|__|\|__|\|__\|__|                                                                                                                                                                            
                                                                                                                                                                                                             
                                                                                                                                                                                                             
                                                                                                                                                                                                             
 ___       ________  ___      ___ _______   ________  ________           ________  ________  _____ ______   _____ ______   ___  ___  ________   ___  _________    ___    ___       _______      ________     
|\  \     |\   __  \|\  \    /  /|\  ___ \ |\   __  \|\   ____\         |\   ____\|\   __  \|\   _ \  _   \|\   _ \  _   \|\  \|\  \|\   ___  \|\  \|\___   ___\ |\  \  /  /|     /  ___  \    |\   __  \    
\ \  \    \ \  \|\  \ \  \  /  / | \   __/|\ \  \|\  \ \  \___|_        \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \  \\\__\ \  \ \  \\\  \ \  \\ \  \ \  \|___ \  \_| \ \  \/  / /    /__/|_/  /|   \ \  \|\  \   
 \ \  \    \ \  \\\  \ \  \/  / / \ \  \_|/_\ \   _  _\ \_____  \        \ \  \    \ \  \\\  \ \  \\|__| \  \ \  \\|__| \  \ \  \\\  \ \  \\ \  \ \  \   \ \  \   \ \    / /     |__|//  / /    \ \  \\\  \  
  \ \  \____\ \  \\\  \ \    / /   \ \  \_|\ \ \  \\  \\|____|\  \        \ \  \____\ \  \\\  \ \  \    \ \  \ \  \    \ \  \ \  \\\  \ \  \\ \  \ \  \   \ \  \   \/  /  /          /  /_/__  __\ \  \\\  \ 
   \ \_______\ \_______\ \__/ /     \ \_______\ \__\\ _\ ____\_\  \        \ \_______\ \_______\ \__\    \ \__\ \__\    \ \__\ \_______\ \__\\ \__\ \__\   \ \__\__/  / /           |\________\\__\ \_______\
    \|_______|\|_______|\|__|/       \|_______|\|__|\|__|\_________\        \|_______|\|_______|\|__|     \|__|\|__|     \|__|\|_______|\|__| \|__|\|__|    \|__|\___/ /             \|_______\|__|\|_______|

selfbot is ready!
''')


















@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="<:bot_tick:870672785322676224>Help AutoOwO<:bot_tick:870672785322676224>",
        color=420699,
        description=
        f":arrow_right: **{prefix}autoOwO**\nowoh, owo sell all, owo flip 500 and owo cash 50 seconds.\n\n**:arrow_right: {prefix}stopautoOwO**\nstops autoOwO.\n\n**:arrow_right: {prefix}Owobanbypass**\nIts prevent you from banning Owo by taking appropriate time\n Example:-`the bot takes breaak 5 min of runnning 1st break= 5min,2nd break=10min 3rd break=15min` \n\n made by Ari.6435"
    )
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/856358420385759293/a_c9bb8d2dd31eae42a2a9d6efc010e1bc.png"
    )
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def autoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('auto OwO  is now **enabled**!')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)


@bot.command()
async def stopautoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('auto OwO Magi is now **disabled**!')
    global dmcs
    dmcs = False


@bot.command(pass_context=True)
async def w(ctx):
    await ctx.message.delete()
    await ctx.send('Wbuy 1')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(2)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully Wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(17)
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(2)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(18)
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(2)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully Wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(19)
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(2)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully Wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(20)
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(2)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully Wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(19)
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(2)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully Wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(24)
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(1)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully Wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(17)
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(2)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully Wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(27)
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(2)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully Wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(15)                    
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(2)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully Wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(16)
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(2)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully Wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(18)
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(2)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully Wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(17)
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(2)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully Wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(20)
            await ctx.send('Owo')
            print(f"{Fore.GREEN}succefully W")
            await asyncio.sleep(2)
            await ctx.send('Owoh')
            print(f"{Fore.GREEN}succefully Wh")
            await ctx.send('Owob')
            print(f"{Fore.GREEN}succefully Wb")
            await asyncio.sleep(3)
            await ctx.send('Owopray')
            print(f"{Fore.GREEN}succefully Owopray")
            await asyncio.sleep(16)    
            
# @bot.command()
# async def stopautoOwO(ctx):
#     await ctx.message.delete()
#     await ctx.send('auto OwO Magi is now **disabled**!')
#     global dmcs
#     dmcs = False






bot.run(token, bot=False)
