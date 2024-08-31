import random
from .youtube import youtube_lookup, youtube_player
import discord
import asyncio

async def lyrica_leave(self,ctx):
    if await self.check_voice(self,ctx):
        if ctx.author.name in self.session_members:
            self.session_members.remove(ctx.author.name)
            if ctx.author.name == self.admin and self.session_members:
                self.admin = random.choice(list(self.session_members))
                await ctx.channel.send(f"{self.admin} is now the admin!")
                await self.lyrica_session(self,ctx)
            elif ctx.author.name == self.admin and not self.session_members:
                await self.lyrica_end(self,ctx)
            else:
                await ctx.channel.send(f"{ctx.author.name} left the session")
                await self.lyrica_session(self,ctx)
                    
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
        if await self.check_voice(self,ctx):
            await ctx.voice_client.move_to(voice_channel)
        else:
            await voice_channel.connect()
        await ctx.send(f"Joined the voice channel: {voice_channel.name}")
        self.admin = ctx.author.name if not self.admin else self.admin
        self.session_members.add(self.admin)
        await self.lyrica_session(self,ctx)
        
async def lyrica_end(self,ctx):
    if await self.check_voice(self,ctx):
        if self.admin == ctx.author.name:
            await ctx.voice_client.disconnect()
            await ctx.send("Left the voice channel!")
            self.admin = None
            self.queue = dict()
            self.session_members = set()
            self.queries = dict()
            await self.lyrica_session(self,ctx)
            return None
        else:
            await ctx.send("You are not the admin!")
    else:
        await ctx.send("I am not in any voice channels!")
        
async def lyrica_look(self,ctx,msg):
    if await self.check_voice(self,ctx):
        if ctx.author.name in self.session_members:
            results = youtube_lookup(msg)
            for i in results:
                await ctx.channel.send(f"{i} - {results[i]['title']}\nBy: {results[i]['author']}\nLength: {results[i]['length']}\n\n")
            
            self.queries[f"{ctx.author.name}_results"] = results
        else:
            await ctx.channel.send(f"You are not in the session!")
    else:
        await ctx.channel.send(f"No active sessions!")
        
async def lyrica_add(self,ctx,msg):
    if await self.check_voice(self,ctx):
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
    if await self.check_voice(self,ctx):
        if ctx.author.name in self.session_members:
            if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                await self.lyrica_resume(self,ctx)
            else:
                if self.queue:
                    for url in list(self.queue.keys()):
                        now_playing = self.queue.pop(url)
                        await ctx.channel.send(f"Now playing {now_playing}")
                        audio_buffer = youtube_player(url)
                        audio_source = discord.FFmpegPCMAudio(audio_buffer, pipe=True)
                        done_playing = asyncio.Event()
                
                        def after_playing(error):
                            if error:
                                print(error)
                            
                            done_playing.set()
                            
                        ctx.voice_client.play(audio_source, after=after_playing)
                        await done_playing.wait()
    
                else:
                    await ctx.channel.send("No queue found!")
        else:
            await ctx.channel.send("You are not in session!")
    else:
        await ctx.channel.send("No active sessions!")
        
async def lyrica_pause(self,ctx):
    if await self.check_voice(self,ctx):
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
    if await self.check_voice(self,ctx):
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
    if await self.check_voice(self,ctx):
        if ctx.author.name in self.session_members:
            if self.queue:
                if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                    ctx.voice_client.stop()
                    
                await self.lyrica_play(self,ctx)
            else:
                if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                    ctx.voice_client.stop()
                await ctx.channel.send("Queue is empty!")
        else:
            await ctx.channel.send("You are not in session!")
            
    else:
        await ctx.channel.send("No active sessions!")

async def lyrica_clear(self,ctx):
    if await self.check_voice(self,ctx):
        if ctx.author.name == self.admin:
            self.queue = dict()
            await self.lyrica_session(self,ctx)
        else:
            await ctx.channel.send("You are not the admin!")
    else:
        await ctx.channel.send("No active sessions!")
        
    
async def lyrica_session(self,ctx):
    await ctx.channel.send(f"\nAdmin: {self.admin}\n\nSessionMembers: {list(self.session_members)}\n\nQueue: {list(self.queue.values()) if self.queue else []}")
            
async def check_voice(self,ctx):
    if ctx.guild.voice_client is None:
        return False
    else:
        return True     