import asyncio
import discord
from discord.ext import commands
from lyrica import setup, TOKEN

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="/",intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! logged in as {bot.user}")
    
async def main():
    async with bot:
        await setup(bot)
        await bot.start(TOKEN)
        
asyncio.run(main())