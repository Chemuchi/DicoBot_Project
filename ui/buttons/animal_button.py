import discord
from API.animal_api import dog, cat

"""-----------------동물코드 버튼---------------------"""
class AnimalButtonFunction(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    @discord.ui.button(label='🐕',style=discord.ButtonStyle.grey)
    async def button1(self, interaction: discord.Interaction,button: discord.ui.Button):
        await interaction.response.edit_message(content=dog(), view=None)

    @discord.ui.button(label='🐈',style=discord.ButtonStyle.blurple)
    async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content=cat(), view=None)