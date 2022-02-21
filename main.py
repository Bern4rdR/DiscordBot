from asyncio import events
from user import *
import interact
import discord
from discord import channel
from discord.client import Client
from discord.ext import commands
import time
import random
import requests


INTENTS = discord.Intents(messages = True, guilds = True, reactions = True,
                          members = True, presences = True)
# Bot account
CLIENT = commands.Bot(command_prefix = '?', intents = INTENTS)

# Message Log
URL = 'https://discord.com/api/v9/channels/<<channel id>>/messages'
HEADER = {
    'authorization': '<<user token>>'
    }

COMMANDS = ['dice + sides (optional) --> roll a die',
            '8ball + question --> ask the magic 8ball a question',
            'rps + choice --> play rock-paper-sissors against the bot',
            'log --> log the last 50 messages in chat',
            'hist + ammount --> show your fist messages']

users = []

def find_user(username, user_id):
    user_exists = False
    for user in users:
        if str(user_id) == user.id:
            user_exists = True
            return users.index(user)
            break
    if not user_exists:
        print(f'Created new user {username}')
        users.append(User(username, user_id))
        return -1


if __name__ == '__main__':
    @CLIENT.event 
    async def on_ready():
        print('Beep. Boop. . Bot is Ready')

    @CLIENT.command(aliases=['help', 'commands', 'command'])
    async def commands(ctx):
        for com in COMMANDS:
            await ctx.send(com)

    @CLIENT.command(aliases=['dice', 'd6'])
    async def _dice(ctx, *, size=6):
        await ctx.send(random.randint(1, int(size)))

    @CLIENT.command(aliases=['8ball'])
    async def _8ball(ctx, *, question):
        r = requests.get('https://8ball.delegator.com/magic/JSON/' + question.replace(' ', '%20'))
        answer = r.json()
        await ctx.send(answer['magic']['answer'])
        
    @CLIENT.command(aliases=['rps'])
    async def rock_paper_sissors(ctx, *, choice):
        user_indx = find_user(ctx.author.name, ctx.author.id)
        for response in users[user_indx].rps(choice):
            await ctx.send(response)
            time.sleep(.3)
    
    @CLIENT.command(aliases=['log', 'save'])
    async def log_mesages(ctx):
        r = requests.get(URL, headers=HEADER).json()
        for message in r:
            user_indx = find_user(message['author']['username'], message['author']['id'])
            users[user_indx].log_msg(message['content'])
        await ctx.send('This channel was logged')

    @CLIENT.command(aliases=['history', 'hist'])
    async def get_msg_hist(ctx, *, ammount):
        await ctx.send(f'Your first {ammount} messages were:')
        user_indx = find_user(ctx.author.name, ctx.author.id)
        for message in users[user_indx].ret_msg_hist(int(ammount)):
            await ctx.send(message)
    
    # Key to the bot
    CLIENT.run('<<bot token>>')
