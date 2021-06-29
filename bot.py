import discord
import os
from emotion_analysis import EmotionAnalysisModel

client = discord.Client()
model = EmotionAnalysisModel()


@client.event
async def on_ready():
    print(f"We have logged {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if model.text_express_anger(message.content):
        await message.channel.send("Your message express anger, you're going to be banned")
    else:
        await message.channel.send("Your message it's okay bruh ;)")

client.run(os.environ['TOKEN'])