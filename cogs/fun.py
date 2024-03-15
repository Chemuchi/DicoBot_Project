import discord
from discord.ext import commands
from ui.buttons.fun_button import FunButtons


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f'{__name__} is ready')

    @commands.hybrid_command(name='재미',description='재미용버튼')
    async def button_test(self, ctx):
        embed = discord.Embed(title='❓', description='골라 골라 골라')
        embed.set_image(url='https://media1.tenor.com/m/x8v1oNUOmg4AAAAd/rickroll-roll.gif')
        view = FunButtons()
        await ctx.reply(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(FunCog(bot))