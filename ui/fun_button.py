import discord
from API.fun_api import hangang_temp

"""-----------------동물코드 버튼---------------------"""
class FunButtonFunction(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    @discord.ui.button(label='한강',style=discord.ButtonStyle.blurple)
    async def button1(self, interaction: discord.Interaction,button: discord.ui.Button):
        temp = hangang_temp()
        print(temp)
        han_embed = discord.Embed(title='🌊',description='현재 한강 수온은...')
        if(temp == '점검중' or temp == '온도 정보를 불러오지 못했습니다.'):
            han_embed.add_field(name='시스템이 점검중이에요...',value='나중에 시도해주세요..')
            print(1)
        else:
            han_embed.add_field(name=f'{temp}도..',value='')
            print(2)
            if(temp<7):
                han_embed.set_footer(text='많이 차갑네요..오늘은 힘들겠어요..')
                print(2.1)
            elif(19 > temp >= 7):
                han_embed.set_footer(text='시원하네요. 수영하기 좋겠어요.')
                print(2.2)
            elif(temp >= 19):
                han_embed.set_footer(text='미지근한데요? 지금이에요!')
                print(2.3)
        await interaction.response.edit_message(embed=han_embed, view=None)
        print(3)

