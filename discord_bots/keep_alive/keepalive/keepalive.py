import discord
from discord.ext import commands
from .ping import ping_website

class MyCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user}')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.channel.name.lower() != 'announcements':
            return

        if message.content.lower() == 'ping':
            await message.channel.send(f'pong, This message was sent in {message.channel.name}')

        if message.content.startswith('/ping'):
            msg = message.content[len('/ping'):].strip()
            if all(msg.split(' ')):
                msg = msg.split(',',2)
                urls = msg[0]
                keywords = msg[1] if len(msg) > 1 else None
                headers = msg[2] if len(msg) > 2 else None

                urls = urls.split(' ')
                keywords = keywords.strip().split(' ') if keywords is not None else None
                headers = headers.strip().split(' ') if headers is not None else None


                await message.channel.send(ping_website(urls, keywords, headers))




async def setup(bot):
   await bot.add_cog(MyCog(bot))

