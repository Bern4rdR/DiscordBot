from asyncio import events
from user import *
import interact
import discord
from discord import channel
from discord.client import Client
from discord.ext import commands
import time


INTENTS = discord.Intents(messages = True, guilds = True, reactions = True,
                          members = True, presences = True)
# Bot account
CLIENT = commands.Bot(command_prefix = '', intents = INTENTS)


if __name__ == '__main__':
    users = []

    @CLIENT.event 
    async def on_ready():
        print('Beep. Boop. . Bot is Ready')

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

        if not user_exists:
            print(f'Created new user: {ctx.author.name}')
            users.append(User(ctx.author.name, ctx.author.id))
            for response in user.rps(choice):
                await ctx.send(response)
                time.sleep(.3)
    
    # key to the bot
    CLIENT.run('<<bot token>>')
