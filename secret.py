import dotenv
import os

dotenv.load_dotenv()


def dico_appid():
    return os.getenv('discord_application_id')


def dico_token():
    return os.getenv('discord_bot_token')


def randomapi_token():
    return os.getenv('random_api_token')
