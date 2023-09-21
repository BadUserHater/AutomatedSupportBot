import voltage
from voltage.ext import commands
import random
import aiohttp
import asyncio

client = commands.CommandsClient("!")

@client.listen("ready")
async def ready():
    print("Bot is Online and Ready")
    await client.set_status(text="DM me for Automated Support")

@client.listen("message")
async def on_message(message):  # Doesn't matter what you call the function.
    msg = message.content
    if message.author.id == client.user.id:
        return
    if isinstance(message.channel, voltage.DMChannel):
        if any(word in msg for word in support1):
            embed = voltage.SendableEmbed(title="Automatic AI Support Assistant", description="You can invite the Meowbahh bot to your server using this Invite link: https://app.revolt.chat/bot/01GQ6RADXPSXPF6NW4CBXXE0VV", color="#FF009F")
            await message.channel.send(embed=embed)
        if any(word in msg for word in support3):
            embed = voltage.SendableEmbed(title="Automatic AI Support Assistant", description="I only have the Automtic AI Support System. If you wish to get in contact with a human Support Team member, please use our Forum channel: <#01GT7K7B95DBN1KK13P2DG7FZH>", color="#FF009F")
            await message.channel.send(embed=embed)
    await client.handle_commands(message)

@client.command(description="Make me say things")
async def say(ctx, *, question):
    await ctx.send(f'{question}')
    await ctx.message.delete()

@client.command(description="Make me say things in a embed")
async def esay(ctx, *, question):
    embed = voltage.SendableEmbed(description=f'{question}', color="#FF009F")
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command(description="Get a link to the original Source Code")
async def source(ctx):
    embed = voltage.SendableEmbed(description="Here is the source code for the Automatic Support Bot here: https://github.com/BadUserHater/AutomatedSupportBot\nSource by Idiot Creature Hater Studios", color="#FF009F")
    await ctx.send(embed=embed)





if "__main__" == __name__:
    with open("support1.txt", "r") as f:
        support1 = f.read().splitlines()

if "__main__" == __name__:
    with open("support3.txt", "r") as f:
        support3 = f.read().splitlines()





client.run("BOTTOKENHERE")
