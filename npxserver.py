import discord
from discord.ext import commands
import npxsearch
from cred import collection, Token

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send('hi, i guess i am ready')
    await bot.process_commands(message)


@bot.command()
async def google(ctx, *text):
    search_query = ' '.join(text)
    g = npxsearch.NpxSearch(search_query)
    res = g.nsearch()
    search_result = {
        "query": search_query
    }
    collection.insert_one(search_result)
    for i in res:
        await ctx.send(i)


@bot.command()
async def recent(ctx, text: str):
    query = {
        "query": {
            "$regex": text
        }
    }
    res = collection.find(query)
    for i in res.distinct('query'):
        await ctx.send(i)

bot.run(Token)
