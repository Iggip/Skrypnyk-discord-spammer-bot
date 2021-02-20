import discord
from discord.ext import commands
import time
import config

flood = False
flood_photo = False
client = commands.Bot(command_prefix=config.prefix)


# Spam
@client.command(name='spam')
async def answer(ctx, context1, context2):
    global flood
    context = ''
    text = ''
    text1 = ''
    if not flood:
        flood = True
    else:
        flood = False
    for x in range(0, len(context2)):
        if context2[x] == '/':
            context = context + ' '
        else:
            context = context + context2[x]
    for v in range(0, int(1000/len(context))):
        text = text + context + '\n'
    if int(context1) > 0:
        if int(context1) > int(1000 / (len(context))):
            for e in range(0, int(int(context1)/(int(1000 / (len(context)))))):
                await ctx.send(text)
                time.sleep(0.8)
        else:
            for v in range(0, int(context1)):
                text1 = text1 + context + '\n'
            await ctx.send(text1)
    if int(context1) == 0:
        while flood:
            await ctx.send(text)
            time.sleep(0.8)


# Spam_Photo
@client.command(name='spam_photo')
async def answer(ctx, context1, context2):
    global flood_photo
    if not flood_photo:
        flood_photo = True
    else:
        flood_photo = False
    if int(context1) > 0:
        for x in range(0, int(context1)):
            await ctx.send(context2)
            time.sleep(0.8)
    elif int(context1) == 0:
        while flood_photo:
            await ctx.send(context2)
            time.sleep(0.8)


# Discord Activity
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=config.bot_activity))


client.run(config.TOKEN)
