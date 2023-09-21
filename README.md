Automatic Support Bot Source Code
CREATED BY: @idiotcreaturehater on Discord.
IdiotCreatureHater#1983 on Revolt.chat

FOR CODE UPDATES, VISIT US ON GITLAB: https://gitlab.com/idiotcreaturehater

The Automatic Support Bot is a Bot that will allow your members get automated support by letting your members DM your bot with automated responses.

###Set up

Discord Bot Setup:
- Go to https://discord.com/developers/applications and create a discord bot application, create a bot, and copy its discord bot token if you have not already done so
- Enable the Message Content Intent.
- client.run("BOTTOKENHERE") where BOTTOKENHERE is your Discord Bot Token that you got from the Discord developer portal (Located at the bottom of the code)
- In your requirements.txt file, make sure to have discord.py so you can install discord.py to your server

Revolt Bot Setup:
- Go to https://app.revolt.chat/settings/bots and click on "Create a Bot" and give your bot a username, and copy its bot token if you have not already done so
- client.run("BOTTOKENHERE") where BOTTOKENHERE is your Bot Token that you got from the Bots page from the settings (Located at the bottom of the code)
- Run this command in your Console: pip install git+https://github.com/EnokiUN/voltage

###HOW IT WORKS

The txt files is for what partial phrases your members may say to your bot. For example, in support1.txt, it includes "invite the bot", that means if someone
says "How do I invite the bot to my server?", the bot will still activate since the question includes the "invite the bot" phrase in the sentence.
For Discord, its made with discord.py
For Revolt, its made with voltage (a great alternative to revolt.py)
if isinstance(message.channel, discord.DMChannel): will make the bot detect if your question is sent to the bot's DMs. (For revolt, discord.DMChannel is replaced with revolt.DMChannel)
await message.channel.send("") will help the bot be able to DM you back under "if any(word in msg for word in support1):"

At "if any(word in msg for word in support1):", It would be connected with:
if "__main__" == __name__:
    with open("support1.txt", "r") as f:
        support1 = f.read().splitlines()

Here's another example of the system
if "__main__" == __name__:
    with open("support1.txt", "r") as f:
        texthere = f.read().splitlines() <-- texthere needs to be the same as the texthere at "if any(word in msg for word in texthere):"
		
Hope you know what I mean. If you know Python, you will understand what I am saying.
If you have better wording for this, open a pull request.