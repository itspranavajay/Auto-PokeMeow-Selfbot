import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
import os


prefix = os.getenv("PREFIX")
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Help pokemeow", color=255, description=f"**{prefix}start**\npokemon , fish , grazz , quest.\n\n**{prefix}stop**\nstops pokemeow.")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/819971643157118987/845166279266271282/unknown-7.jpg")
  await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def start(ctx):
	await ctx.message.delete()
	await ctx.send('auto pokemeow selfbot is now **enabled**!')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(3)
			await ctx.send(';pokemon')
			print(f"{Fore.GREEN}succefully pokemon")
			await asyncio.sleep(13)
			await ctx.send(';f')
			print(f"{Fore.GREEN}succefully f")
			await asyncio.sleep(13)
			await ctx.send(';grazz')
			print(f"{Fore.GREEN}succefully grazz")
			await asyncio.sleep(13)
			await ctx.send(';quest')
			print(f"{Fore.GREEN}succefully quest")
			await asyncio.sleep(13)


@bot.command()
async def stop(ctx):
	await ctx.message.delete()
	await ctx.send('auto PokeMeow selfbot is now **disabled**!')
	global dmcs
	dmcs = False

@bot.event
async def on_ready():
  activity = discord.Game(name="MoeZilla", type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  print(f'''{Fore.RED}
✨Run Now Auto PokeMeow By MoeZilla
{Fore.GREEN}

✨Run Now Auto PokeMeow Selfbot
''')

bot.run(token, bot=False)
