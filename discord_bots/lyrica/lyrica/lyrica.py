import discord 
from discord.ext import commands
import random
from .library import youtube_lookup, youtube_player

greetings = ['Hello!', 'Hi!', 'Hey there!', 'Hola!', "اهلا","你好","Bonjour"]
class Lyrica(commands.Cog):
    def __init__(self,bot):
        self.bot = bot 
        self.admin = None
        self.session_members = set()
        self.queue = dict()
        self.queries = dict()
        
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user}")
        
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        
        if message.content.lower() == 'lyrica':
            await message.channel.send(f'{random.choice(greetings)}')

        if message.content.lower() == '/lyrstart':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_start(ctx)
            except Exception as e:
                print(e)
                
        if message.content.lower() == '/lyrend':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_end(ctx)
            except Exception as e:
                print(e)
            
        if message.content.lower() == '/lyrjoin':
            ctx = await self.bot.get_context(message)
            if await self.check_voice(ctx):
                self.session_members.add(ctx.author.name)
                await self.lyrica_session(ctx)
            else:
                await ctx.channel.send("No active sessions!")
                
        if message.content.lower() == '/lyrleave':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_leave(ctx)
            except Exception as e:
                print(e)
                    
        if message.content.lower() == '/lyrsession':
            ctx = await self.bot.get_context(message)
            await self.lyrica_session(ctx)
            
        if message.content.startswith('/lyrlook'):
            ctx = await self.bot.get_context(message)
            try:
                msg = message.content[len('/lyrlook'):].strip()
                await self.lyrica_look(ctx,msg)
            except Exception as e:
                print(e)
                
        if message.content.startswith('/lyradd'):
            ctx = await self.bot.get_context(message)
            try:
                msg = message.content[len('/lyradd'):].strip()
                await self.lyrica_add(ctx,msg)
            except Exception as e:
                print(e)
                
        if message.content.lower() == '/lyrplay':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_play(ctx)
            except Exception as e:
                print(e)
                
        if message.content.lower() == '/lyrpause':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_pause(ctx)
            except Exception as e:
                print(e)
                
        if message.content.lower() == '/lyrresume':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_resume(ctx)
            except Exception as e:
                print(e)
                
        if message.content.lower() == '/lyrnext':
            ctx = await self.bot.get_context(message)
            try:
                await self.lyrica_next(ctx)
            except Exception as e:
                print(e)
                
                
            
                
    
    async def lyrica_leave(self,ctx):
        if await self.check_voice(ctx):
            if ctx.author.name in self.session_members:
                self.session_members.remove(ctx.author.name)
                if ctx.author.name == self.admin and self.session_members:
                    self.admin = random.choice(list(self.session_members))
                    await ctx.channel.send(f"{self.admin} is now the admin!")
                    await self.lyrica_session(ctx)
                elif ctx.author.name == self.admin and not self.session_members:
                    await self.lyrica_end(ctx)
                else:
                    await ctx.channel.send(f"{ctx.author.name} left the session")
                    await self.lyrica_session(ctx)
                        
            else:
                await ctx.channel.send("You are not in session!")
        else:
            await ctx.channel.send("No active sessions!")
    
    
    
    async def lyrica_start(self,ctx):
        if self.admin and ctx.author.name != self.admin:
            await ctx.channel.send(f"Bot is currently occupied by: {self.admin}")
            return 
        if ctx.author.voice is None:
            await ctx.send("You are not in a voice channel!")
        else:
            voice_channel = ctx.author.voice.channel
            permissions = voice_channel.permissions_for(ctx.guild.me)
            if not permissions.connect or not permissions.speak:
                await ctx.send("I do not have permissions to join and speak in this voice channel!")
                return
            if await self.check_voice(ctx):
                await ctx.voice_client.move_to(voice_channel)
            else:
                await voice_channel.connect()
            await ctx.send(f"Joined the voice channel: {voice_channel.name}")
            self.admin = ctx.author.name if not self.admin else self.admin
            self.session_members.add(self.admin)
            await self.lyrica_session(ctx)
            
    async def lyrica_end(self,ctx):
        if await self.check_voice(ctx):
            if self.admin == ctx.author.name:
                await ctx.voice_client.disconnect()
                await ctx.send("Left the voice channel!")
                self.admin = None
                self.queue = dict()
                self.session_members = set()
                self.queries = dict()
                await self.lyrica_session(ctx)
                return None
            else:
                await ctx.send("You are not the admin!")
        else:
            await ctx.send("I am not in any voice channels!")
            
    async def lyrica_look(self,ctx,msg):
        if await self.check_voice(ctx):
            if ctx.author.name in self.session_members:
                results = youtube_lookup(msg)
                for i in results:
                    await ctx.channel.send(f"{i} - {results[i]['title']}\nBy: {results[i]['author']}\n\n")
                
                self.queries[f"{ctx.author.name}_results"] = results
            else:
                await ctx.channel.send(f"You are not in the session!")
        else:
            await ctx.channel.send(f"No active sessions!")
            
    async def lyrica_add(self,ctx,msg):
        if await self.check_voice(ctx):
            if ctx.author.name in self.session_members:
                try:
                    msg = int(msg)
                    user_name = f"{ctx.author.name}_results"
                    if msg in self.queries[f"{user_name}"]:
                        self.queue[self.queries[f"{user_name}"][msg]['url']] = f"{self.queries[user_name][msg]['title']}"
                        await ctx.channel.send(f"Up Next: {list(self.queue.values())[0]}\n\nQueue: {list(self.queue.values())}")
                    else:
                        await ctx.channel.send(f"{msg} Not in your search query {ctx.author.name}!") 
                except Exception as e:
                    await ctx.channel.send(f"Must be the number of a result of in a query!")
            else:
                await ctx.channel.send(f"You are not in session!")
            
        else:
            await ctx.channel.send(f"No active sessions!")
            
    async def lyrica_play(self,ctx):
        if await self.check_voice(ctx):
            if ctx.author.name in self.session_members:
                if self.queue:
                    url = list(self.queue)[0]
                    now_playing = self.queue.pop(url)
                    await ctx.channel.send(f"Now playing {now_playing}")
                    audio_buffer = youtube_player(url)
                    audio_source = discord.FFmpegPCMAudio(audio_buffer, pipe=True)
                    ctx.voice_client.play(audio_source, after=lambda e: print(f'Error {e}') if e else None)
                    
                else:
                    await ctx.channel.send("No queue found!")
            else:
                await ctx.channel.send("You are not in session!")
        else:
            await ctx.channel.send("No active sessions!")
            
    async def lyrica_pause(self,ctx):
        if await self.check_voice(ctx):
            if ctx.author.name in self.session_members:
                if ctx.voice_client.is_playing():
                    ctx.voice_client.pause()
                    await ctx.channel.send("Audio paused")
                else:
                    await ctx.channel.send("No audio is playing!")
                    
            else:
                await ctx.channel.send("You are not in session!")
        else:
            await ctx.channel.send("No active sessions!")
            
    async def lyrica_resume(self,ctx):
        if await self.check_voice(ctx):
            if ctx.author.name in self.session_members:
                if ctx.voice_client.is_paused():
                    ctx.voice_client.resume()
                    await ctx.channel.send("Audio resumed")
                else:
                    await ctx.channel.send("Audio is not paused!")
            else:
                await ctx.channel.send("You are not in session!")
        else:
            await ctx.channel.send("No active sessions!")
            
    async def lyrica_next(self,ctx):
        if await self.check_voice(ctx):
            if ctx.author.name in self.session_members:
                if self.queue:
                    if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                        ctx.voice_client.stop()
                        
                    await self.lyrica_play(ctx)
                else:
                    if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                        ctx.voice_client.stop()
                    await ctx.channel.send("Queue is empty!")
            else:
                await ctx.channel.send("You are not in session!")
                
        else:
            await ctx.channel.send("No active sessions!")
                
                
                    
                    
            
            
                    
    
            
        
     
    async def lyrica_session(self,ctx):
        await ctx.channel.send(f"\nAdmin: {self.admin}\n\nSessionMembers: {list(self.session_members)}\n\nQueue: {list(self.queue.values()) if self.queue else []}")
                
    async def check_voice(self,ctx):
        if ctx.guild.voice_client is None:
            return False
        else:
            return True      