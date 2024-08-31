import discord 
from discord.ext import commands
import random
from .library import lyrica_start,lyrica_look,lyrica_play,lyrica_pause,lyrica_add,lyrica_clear,lyrica_end,lyrica_leave,lyrica_next,lyrica_resume,lyrica_session,check_voice
import asyncio


class Lyrica(commands.Cog):
    def __init__(self,bot):
        self.bot = bot 
        self.admin = None
        self.session_members = set()
        self.queue = dict()
        self.queries = dict()
        self.greetings = ['Hello!', 'Hi!', 'Hey there!', 'Hola!', "اهلا","你好","Bonjour"]
        
        self.lyrica_start = lyrica_start
        self.check_voice = check_voice
        self.lyrica_look = lyrica_look
        self.lyrica_play = lyrica_play
        self.lyrica_pause = lyrica_pause
        self.lyrica_add = lyrica_add
        self.lyrica_clear = lyrica_clear
        self.lyrica_end = lyrica_end
        self.lyrica_leave = lyrica_leave
        self.lyrica_next = lyrica_next
        self.lyrica_resume = lyrica_resume
        self.lyrica_session = lyrica_session
        
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user}")
        
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        
        if message.content.lower() == 'lyrica':
            await message.channel.send(f'{random.choice(self.greetings)}')

        if message.content.lower() == '/lyrstart':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_start(self,ctx)
            except Exception as e:
                print(e)
                
        if message.content.lower() == '/lyrend':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_end(self,ctx)
            except Exception as e:
                print(e)
            
        if message.content.lower() == '/lyrjoin':
            ctx = await self.bot.get_context(message)
            if await self.check_voice(self,ctx):
                self.session_members.add(ctx.author.name)
                await self.lyrica_session(self,ctx)
            else:
                await ctx.channel.send("No active sessions!")
                
        if message.content.lower() == '/lyrleave':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_leave(self,ctx)
            except Exception as e:
                print(e)
                    
        if message.content.lower() == '/lyrsession':
            ctx = await self.bot.get_context(message)
            await self.lyrica_session(self,ctx)
            
        if message.content.startswith('/lyrlook'):
            ctx = await self.bot.get_context(message)
            try:
                msg = message.content[len('/lyrlook'):].strip()
                await self.lyrica_look(self,ctx,msg)
            except Exception as e:
                print(e)
                
        if message.content.startswith('/lyradd'):
            ctx = await self.bot.get_context(message)
            try:
                msg = message.content[len('/lyradd'):].strip()
                await self.lyrica_add(self,ctx,msg)
            except Exception as e:
                print(e)
                
        if message.content.lower() == '/lyrplay':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_play(self,ctx)
            except Exception as e:
                print(e)
                
        if message.content.lower() == '/lyrpause':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_pause(self,ctx)
            except Exception as e:
                print(e)
                
        if message.content.lower() == '/lyrresume':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_resume(self,ctx)
            except Exception as e:
                print(e)
                
        if message.content.lower() == '/lyrnext':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_next(self,ctx)
            except Exception as e:
                print(e)
        if message.content.lower() == '/lyrclear':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_clear(self,ctx)
            except Exception as e:
                print(e)
                
                
            
                
    
     
    