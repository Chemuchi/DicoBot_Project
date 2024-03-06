import requests, json


"""-------------한강----------------"""
def hangang_temp():
    response = requests.get('https://api.hangang.life')
    data = json.loads(response.text)
    temp = data['DATAs']['DATA']['HANGANG']['노량진']['TEMP']
    return temp