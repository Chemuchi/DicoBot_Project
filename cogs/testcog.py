from discord.ext import commands


class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f'{__name__} cog is ready')

    @commands.hybrid_command(name='핑', description='봇이 대답합니다.')
    async def ping(self, ctx):
        await ctx.reply('퐁!')


async def setup(bot):
    await bot.add_cog(TestCog(bot))
