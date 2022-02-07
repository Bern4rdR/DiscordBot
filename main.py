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
CLIENT = commands.Bot(command_prefix = '', intents = INTENTS)


if __name__ == '__main__':
    users = []

    @CLIENT.event 
    async def on_ready():
        print('Beep. Boop. . Bot is Ready')

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
        user_exists = False
        for user in users:
            if user.id == str(ctx.author.id):
                for response in user.rps(choice):
                    await ctx.send(response)
                    time.sleep(.3)
                user_exists = True
                break
        # Adds a user if none exist
        if not user_exists:
            print(f'Created new user: {ctx.author.name}')
            users.append(User(ctx.author.name, ctx.author.id))
            for response in users[-1].rps(choice):
                await ctx.send(response)
                time.sleep(.3)
    
    # Key to the bot
    CLIENT.run('<<bot token>>')
