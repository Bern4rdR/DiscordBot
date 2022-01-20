import requests

API_ENDPOINT = 'https://discord.com/api/v8'
CLIENT_ID = '<<client id>>'
CLIENT_SECRET = '<<client secret>>'
REDIRECT_URI = "https://google.com"

class User:
    """Every users personal connection to the bot, storing information about the user"""
    def __init__(self, username, id):
        self.username = username
        self.id = id


def exchange_code(code):
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
        }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
    r = requests.post(API_ENDPOINT + '/oauth2/token', data=data, headers=headers)
    r.raise_for_status()
    return r.json()

def add_to_guild(access_token, userID):
    url = API_ENDPOINT + "/guilds/<<guild id>>/members/" + userID
    botToken = '<<token>>'

    data = {'access_token': access_token}
    headers = {
        'Authorization': 'Bot ' + botToken,
        'Content-Type': 'application/json'
        }
    response = requests.put(url = url, headers=headers, json=data)
    print(response.text)


if __name__ == '__main__':
    code = exchange_code('<<code querry>>')['access_token']
    add_to_guild(code, '<<user id>>')