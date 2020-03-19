import discord
from discord.ext import commands

import asyncio
from itertools import cycle
import os
import dotenv

bot = commands.Bot(command_prefix="*:")


@bot.event
async def on_ready():
    print("-" * 30)
    print(f'Logged in as: {bot.user}')
    print(f'With ID: {bot.user.id}')
    print("-" * 30)


@bot.command()
async def ping(ctx):
    await ctx.send(f'pong, that was {bot.latency}')


@bot.command()
async def ping(ctx, ):
    print(ctx.author)


dotenv.load_dotenv()
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)

#You can invite the bot here
#https://discordapp.com/api/oauth2/authorize?client_id=690265979166523418&permissions=8&scope=bot
