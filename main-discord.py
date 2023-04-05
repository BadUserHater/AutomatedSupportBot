import discord
from discord.ext import commands
import random
import aiohttp
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")

@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        if any(word in msg for word in support1):
            embed = discord.Embed(title="Automatic Support Assistant", description="You can invite the Revolt bot to your server using this Invite link: https://app.revolt.chat/bot/01GQ6RADXPSXPF6NW4CBXXE0VV", color=(16776960))
            await message.author.send(embed=embed)
        if any(word in msg for word in support3):
            embed = discord.Embed(title="Automatic Support Assistant", description="I only have the Automtic AI Support System. If you wish to get in contact with a human Support Team member in our server", color=(16776960))
            await message.author.send(embed=embed)

    await client.process_commands(message)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="DM me for AI Support"))
    print("Bot is Online and Ready")

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Bot Commands", description="Here is my commands for testing purposes", color=(16776960))
    embed.add_field(name="Core Commands", value="!help - This message\n!ping - Checks my Latency\n!say - Make me say stuff\n!esay - Make me say things in a embed\n!source - Get a link to the original Source Code", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'My Latency is: {round(client.latency * 1000)}ms')

@client.command()
async def say(ctx, *, question: commands.clean_content):
    await ctx.send(f'{question}')
    await ctx.message.delete()

@client.command()
async def esay(ctx, *, question):
    embed = discord.Embed(description=f'{question}', color=(16776960))
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command()
async def source(ctx):
    embed = discord.Embed(description="Here is the source code for the Automatic Support Bot here: https://github.com/BadUserHater/AutomatedSupportBot\nSource by Idiot Creature Hater Studios", color=(16776960))
    await ctx.send(embed=embed)





if "__main__" == __name__:
    with open("support1.txt", "r") as f:
        support1 = f.read().splitlines()

if "__main__" == __name__:
    with open("support3.txt", "r") as f:
        support3 = f.read().splitlines()





client.run("BOTTOKENHERE")
