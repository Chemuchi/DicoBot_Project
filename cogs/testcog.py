import discord
from discord.ext import commands

from ui.buttons.test_button import TestButtonFunction
from setting import embed_color


class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f'{__name__} is ready')

    @commands.hybrid_command(name='핑', description='커맨드 기초')
    async def ping(self, ctx):
        await ctx.reply('퐁!')

    @commands.hybrid_command(name='대답', description='커맨드 입력값 기초')
    async def repeat(self, ctx, *, content: str):
        await ctx.reply(content)

    @commands.hybrid_command(name='아웃라인임베드', description='임베드 기초')
    async def outline_embed(self, ctx):
        embed = discord.Embed(title='임베드 제목', description='임베드 설명', color=embed_color())
        embed.add_field(name='필드 이름 1', value='필드 값 1', inline=False)
        embed.add_field(name='필드 이름 2', value='필드 값 2', inline=False)
        embed.add_field(name='필드 이름 3', value='필드 값 3', inline=False)
        embed.add_field(name='필드 이름 4', value='필드 값 4', inline=False)
        embed.set_footer(text='바닥글 내용')
        await ctx.reply(embed=embed)

    @commands.hybrid_command(name='인라인임베드', description='임베드 기초')
    async def inline_embed(self, ctx):
        embed = discord.Embed(title='임베드 제목', description='임베드 설명', color=embed_color())
        embed.add_field(name='필드 이름 1', value='필드 값 1', inline=True)
        embed.add_field(name='필드 이름 2', value='필드 값 2', inline=True)
        embed.add_field(name='필드 이름 3', value='필드 값 3', inline=True)
        embed.add_field(name='필드 이름 4', value='필드 값 4', inline=True)
        embed.set_footer(text='바닥글 내용')
        await ctx.reply(embed=embed)

    @commands.hybrid_command(name='강제종료')
    async def force_off(self, ctx):
        await self.bot.close()



    @commands.hybrid_command(name='버튼테스트',description='버튼을 테스트')
    async def button_test(self, ctx):
        await ctx.send('버튼을 눌러보세요.', view=TestButtonFunction())
async def setup(bot):
    await bot.add_cog(TestCog(bot))
