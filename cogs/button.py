import discord
from discord.ext import commands


class ButtonFunction(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f'{__name__} is ready')
    #메세지 수정은 edit_message(content='')
    @discord.ui.button(label="버튼1", style=discord.ButtonStyle.green)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="버튼1 눌림")

class ButtonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(name='테스트버튼',description='테스트용 버튼')
    async def test_button(self, ctx):
        await ctx.send("버튼 테스트용", view=ButtonFunction())





async def setup(bot):
    await bot.add_cog(ButtonCog(bot))