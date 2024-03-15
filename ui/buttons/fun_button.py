import discord
from API.fun_api import hangang_temp


class FunButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
        self.value = None

    @discord.ui.button(label='한강', style=discord.ButtonStyle.blurple)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        temp = hangang_temp()
        han_embed = discord.Embed(title='🌊', description='현재 한강 수온은...')
        if temp == '점검중' or temp == '온도 정보를 불러오지 못했습니다.':
            han_embed.add_field(name='시스템이 점검중이에요...', value='나중에 시도해주세요..')
        else:
            han_embed.add_field(name=f'{temp}도..', value='')
            if temp < 7:
                han_embed.set_footer(text='많이 차갑네요..오늘은 힘들겠어요..')
            elif 19 > temp >= 7:
                han_embed.set_footer(text='시원하네요. 수영하기 좋겠어요.')
            elif temp >= 19:
                han_embed.set_footer(text='미지근한데요? 지금이에요!')
        await interaction.response.edit_message(embed=han_embed, view=None)

    @discord.ui.button(label='ChipiChipi', style=discord.ButtonStyle.secondary)
    async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
        chipi_embed = discord.Embed(title='', description='')
        chipi_embed.set_image(url='https://media1.tenor.com/m/mJ_Og97j5WwAAAAC/chipi-chapa.gif')
        await interaction.response.edit_message(embed=chipi_embed, view=None)
