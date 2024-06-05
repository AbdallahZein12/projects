import asyncio
import discord
from discord.ext import commands
from pic2ascii.constants import TOKEN
from pic2ascii.pic2ascii import setup

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/',intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

async def main():
    async with bot:
        await setup(bot)
        await bot.start(TOKEN)

asyncio.run(main())