import asyncio
import os
import discord
from secret import dico_token
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=(';'), intents=discord.Intents.all())

token = dico_token()


async def load_cogs():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_ready():
    await bot.tree.sync()
    game = discord.Game(f"prefix = ;")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print('봇 실행 완료')


async def start():
    async with bot:
        await load_cogs()
        await bot.start(token)

asyncio.run(start())