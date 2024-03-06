import discord
from discord.ext import commands
from ui.animal_button import AnimalButtonFunction


class AnimalCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f'{__name__} is ready')

    @commands.hybrid_command(name='동물',description='랜덤 이미지')
    async def random_animal(self, ctx):
        await ctx.send('강아지와 고양이중 하나를 선택해보세요!',view=AnimalButtonFunction())


async def setup(bot):
    await bot.add_cog(AnimalCog(bot))
