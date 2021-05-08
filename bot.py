import discord
from discord.ext import commands
import time
import config
import pickle


try:
    data = pickle.load(open(config.way, "rb"))
except FileNotFoundError:
    pickle.dump({}, open(config.way, "wb"))
    data = {}


client = commands.Bot(command_prefix=config.prefix)


# Spam
@client.command(name='spam')
async def answer(ctx, context1, *args):
    global data
    data = pickle.load(open(config.way, "rb"))
    try:
        if not data[ctx.message.channel.id]:
            data[ctx.message.channel.id] = {'flood': False}
    except KeyError:
        data[ctx.message.channel.id] = {'flood': False}
    text = ''
    context = ''
    if not data[ctx.message.channel.id]['flood'] and context1 != 'stop':
        data[ctx.message.channel.id]['flood'] = True
    if ctx.message.attachments and not args:
        context = ctx.message.attachments[0].url
        args = [1]
    else:
        for x in args:
            context += x + ' '
    try:
        if args[0] == '^long':
            context = context[5:len(context)]
            r = 0
            while len(text) < 2000 and r < int(context1):
                text += context + '\n'
                r += 1
            if int(context1) != 0:
                if r < int(context1):
                    for b in range(0, int(int(context1)/r)):
                        await ctx.send(text)
                        time.sleep(0.8)
                    text1 = ''
                    for a in range(0, int(context1)-r*int(int(context1)/r)):
                        text1 += context + '\n'
                    await ctx.send(text1)
                else:
                    await ctx.send(text)
                data[ctx.message.channel.id]['flood'] = False
            if int(context1) == 0:
                while data[ctx.message.channel.id]['flood']:
                    await ctx.send(text)
                    time.sleep(0.8)
        else:
            if int(context1) > 0:
                e = 0
                while e < int(context1) and data[ctx.message.channel.id]['flood']:
                    await ctx.send(context)
                    time.sleep(0.8)
                    e += 1
                data[ctx.message.channel.id]['flood'] = False
            if int(context1) == 0:
                while data[ctx.message.channel.id]['flood']:
                    await ctx.send(context)
                    time.sleep(0.8)
    except IndexError:
        if data[ctx.message.channel.id]['flood']:
            data[ctx.message.channel.id]['flood'] = False
            if context1 == 'stop':
                await ctx.send('stopped')
                while data[ctx.message.channel.id]['flood']:
                    await ctx.send('stopped')
    pickle.dump(data, open(config.way, "wb"))


# Discord Activity
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=config.bot_activity))


client.run(config.TOKEN)
