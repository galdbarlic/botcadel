import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import webserver

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


def cadel_msg(msg):
    msg = msg.lower().replace('joscka', 'aing')
    new_msg = ""
    for i in msg:
        if i == "r":
            new_msg += "l"
        elif i == "R":
            new_msg += "L"
        else:
            new_msg += i
    return new_msg




@bot.event
async def on_ready():
    print(f"Aing {bot.user.name} sia kabeh saha kontol")

@bot.event
async def on_member_join(member):
    await member.send(f"kontol lu {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("!"):
        await bot.process_commands(message)
        return
    msg = cadel_msg(message.content)
    await message.reply(msg)
    await bot.process_commands(message)

@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(cadel_msg(msg))

@bot.command()
async def hello(ctx):
    await ctx.send(f"Naon sia {ctx.author.mention}")

@bot.command()
async def josckakontol(ctx):
    await ctx.send(f"Benar sekali {ctx.author.mention}")


webserver.keep_alive()
bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)