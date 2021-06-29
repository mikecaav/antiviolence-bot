import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!echo"):
        await message.channel.send(message.content)

client.run(os.environ['TOKEN'])