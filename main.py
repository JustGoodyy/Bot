import discord
from scraper import cek_pengumuman_baru
from discord.ext import commands
from discord.ext import tasks
from scraper import cek_pengumuman_baru
import logging
from dotenv import load_dotenv
import os
import webserver

load_dotenv()
ROLE_ID = int(os.getenv('ROLE_ID'))
token = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = 1424712642492235817  # Ganti dengan ID channel yang diinginkan

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot Active, {bot.user.name}")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"<@&{ROLE_ID}>Bot Active!")
    cek_pengumuman.start()

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server, {member.name}!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "fuck" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, sok asik lu!")

    await bot.process_commands(message)

@tasks.loop(minutes=10)
async def cek_pengumuman():
    channel = bot.get_channel(CHANNEL_ID)
    baru = cek_pengumuman_baru()
    if baru:
        await channel.send(f"<@&{ROLE_ID}>📢 Penugasan baru:\n{baru}")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
webserver.keep_alive()