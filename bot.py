import discord
import os
from emotion_analysis import EmotionAnalysisModel

client = discord.Client()
model = EmotionAnalysisModel()
CHANNEL_CATEGORY = 'anti-violence-bot'
CHANNEL_NAME = 'reported-messages'

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


@client.event
async def on_guild_join(guild):
    categories = get_categories(guild)
    channels = get_channels(guild)
    print("Your bot just landed into a new server! We've created the corresponding channels to make it work :D")
    if CHANNEL_CATEGORY not in categories:
        category = await guild.create_category(CHANNEL_CATEGORY)
    if CHANNEL_NAME not in channels:
        await guild.create_text_channel(
            CHANNEL_NAME,
            category=category
        )


def get_categories(guild):
    return get_objects_from_list(guild.categories)


def get_channels(guild):
    return get_objects_from_list(guild.channels)


def get_objects_from_list(list_of_objects):
    objects = set()
    for object_ in list_of_objects:
        objects.add(object_.name)
    return objects


client.run(os.environ['TOKEN'])
