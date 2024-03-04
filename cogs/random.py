import requests
import json
from secret import randomapi_token
from discord.ext import commands


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """
    @commands.hybrid_command(name='난수',description='지정한 갯수, 크기의 난수를 생성해줍니다.')
    async def random(self, ctx, 갯수: int, 최소크기: int, 최대크기: int):
        token = randomapi_token()
        headers = {
            'Content-Type': 'application/json-rpc',
            'Accept': 'application/json-rpc'
        }
        data = {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": token,
                "n": 갯수,
                "min": 최소크기,
                "max": 최대크기,
                "replacement": True
            },
            "id": 1
        }
        response = requests.post('https://api.random.org/json-rpc/2/invoke', headers=headers, data=json.dumps(data))
        result = response.json()['result']['random']['data']
        print(result)

"""
async def setup(bot):
    await bot.add_cog(Random(bot))

