import asyncio
import os
import discord
from setting import dico_token
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=(';'), intents=discord.Intents.all())

token = dico_token()


async def load_cogs():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command(name='reload', description='cogs 리로드')
async def reload_cogs(ctx):
    await load_cogs()
    ctx.reply(':check_mark: 코드 리로딩 완료')

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


<<<<<<< HEAD

asyncio.run(start())
=======
asyncio.run(start())
>>>>>>> JaeHyeong
