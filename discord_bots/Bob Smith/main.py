import discord
import os
import requests
import json
import random
import asyncpraw
from replit import db
import tracemalloc
from keep_alive import keep_alive 
tracemalloc.start()

sad_words = [
  'sad',
  'depressed',
  'depressing',
  'angry',
  'miserable',
]

starter_encouragements = [
  "Hang in there",
  "You are a great person/bot",
  "Don't worry, it'll be okay",
  "Cheer up"
]

if "responding" not in db.keys():
  db["responding"] = True


greetings = [
  'Hi', "Hello", "Greetings", "Bonjour!", "Buenos Dias!", "اهلا", "yo"
]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db['encouragements']
    if encouraging_message in encouragements:
      return
    else:
      encouragements.append(encouraging_message)
      db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db['encouragements']
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements

async def get_meme():
  async with asyncpraw.Reddit(client_id=os.environ['REDDITID'],
                     client_secret=os.environ['REDDITSECRET'],
                     user_agent='YOUR_USER_AGENT') as reddit:
  
    subreddit = await reddit.subreddit('memes')
    posts = []
    async for submission in subreddit.hot(limit=100):
      posts.append(submission)

    post = random.choice(posts)
    return(post.url)
  

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  if msg == ('!bob'):
    await message.channel.send(random.choice(greetings))

  if msg.startswith('!bobinspire'):
    if message.author.name == 'Winger':
      await message.channel.send("no.")
    else:
      quote = get_quote()
      await message.channel.send(quote)

  if msg.startswith('!bobfunny'):
    meme = await get_meme()
    await message.channel.send(meme)
  
  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + list(db["encouragements"])
  
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith('!bobnew'):
    encouraging_message = msg.split("!bobnew ", 1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added!")

  if msg.startswith("!bobdel"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("!bobdel",1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    for index, item in enumerate(encouragements):
        sending = str(index) + "-  " + item
        await message.channel.send(sending)
      

  if msg.startswith("!boblist"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = list(db["encouragements"])
      for index, item in enumerate(encouragements):
        sending = str(index) + "-  " + item
        await message.channel.send(sending)

  if msg.startswith("!bobrespond"):
    value = msg.split("!bobrespond ",1)[1]

    if value.lower() == "true":
      db['responding'] = True
      await message.channel.send("Responding is on!")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off!")
      
keep_alive()
client.run(os.environ['TOKEN'])

