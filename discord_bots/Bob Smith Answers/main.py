import discord
import os
import requests
import json
from bs4 import BeautifulSoup
from discord.ext import commands
from keep_alive import keep_alive 

intents2 = discord.Intents.default()
intents2.members = True
intents2.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents2)


def answer(question):
  url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"

  payload = {
    "enable_google_results": "true",
    "enable_memory": False,
    "input_text": f"in less than 100 words {question}"
  }
  headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": os.environ['CHATSONIC']
  }

  response = requests.post(url, json=payload, headers=headers)

  data = json.loads(response.text)
  message_content_html = data['message']

  soup = BeautifulSoup(message_content_html, 'html.parser')

  message_content = soup.get_text()

  return (message_content)





@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def bobans(ctx, *, question):
  async with ctx.typing():
    answer_text = answer(question)
    await ctx.send(answer_text)

    

keep_alive()
bot.run(os.environ['BOTTOKEN'])
