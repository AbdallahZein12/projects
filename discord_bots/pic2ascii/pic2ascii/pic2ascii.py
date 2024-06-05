import discord
from discord.ext import commands
import os
from .p2a_processor import pillow

class Pic2Ascii(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot cog is ready! Logged in as {self.bot.user}")

    @commands.command(name='p2a')
    async def p2a(self, ctx):
        if ctx.message.author == self.bot.user:
            return

        if ctx.message.attachments and ctx.message.attachments[0].content_type.startswith('image/'):
            attachment = ctx.message.attachments[0]
            path = os.path.join('pic2ascii','filehandling', attachment.filename)
            await attachment.save(path)
            await ctx.send(pillow(path))



        else:
            await ctx.send('Please upload an image!')



async def setup(bot):
    await bot.add_cog(Pic2Ascii(bot))



