import discord

"""-----------------테스트용 버튼--------------------"""
class TestButtonFunction(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    @discord.ui.button(label="버튼1", style=discord.ButtonStyle.green)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="버튼1 눌림")


