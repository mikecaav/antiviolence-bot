import discord
import os
from emotion_analysis import EmotionAnalysisModel

client = discord.Client()
model = EmotionAnalysisModel()
CHANNEL_CATEGORY = 'anti-violence-bot'
CHANNEL_NAME = 'reported-messages'
MODERATOR_ROLE = 'moderator message reviewer'

@client.event
async def on_ready():
    print(f"We have logged {client.user}")


@client.event
async def on_message(message):
    report_message_channel = get_report_message_channel(message.guild)
    if message.author == client.user:
        return
    if model.text_express_anger(message.content):
        await report_message_channel.send(f"{message.author.mention}: {message.content}")


def get_report_message_channel(guild):
    for channel in guild.channels:
        if channel.name == CHANNEL_NAME:
            return channel


@client.event
async def on_guild_join(guild):
    categories = get_categories(guild)
    channels = get_channels(guild)
    roles = get_roles(guild)

    print(f"Your bot just landed into {guild.name}! We've created the corresponding channels, roles and categories to make it work :D")
    if CHANNEL_CATEGORY not in categories:
        category = await guild.create_category(CHANNEL_CATEGORY)

    if MODERATOR_ROLE not in roles:
        permissions = discord.Permissions(
            ban_members=True,
            kick_members=True,
            deafen_members=True,
            mute_members=True,
            read_messages=True
        )
        moderator_role = await guild.create_role(
            name=MODERATOR_ROLE,
            permissions=permissions,
            mentionable=True
        )

    if CHANNEL_NAME not in channels:
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            moderator_role: discord.PermissionOverwrite(read_messages=True)
        }
        await guild.create_text_channel(
            CHANNEL_NAME,
            category=category,
            topic="This text channel was created as a special place to review the messages that are detected as hostile to decide what to do with the hostile users",
            overwrites=overwrites
        )


def get_categories(guild):
    return get_objects_from_list(guild.categories)


def get_channels(guild):
    return get_objects_from_list(guild.channels)

def get_roles(guild):
    return get_objects_from_list(guild.roles)

def get_objects_from_list(list_of_objects):
    objects = set()
    for object_ in list_of_objects:
        objects.add(object_.name)
    return objects


client.run(os.environ['TOKEN'])
