import discord
import os
from dotenv import load_dotenv

load_dotenv(".env")
token = os.environ.get("DISC_TOKEN")


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

# 1 issue -> bot crashes
afk_list = []

def add_afk(user_id):
  afk_list.append(user_id)

def remove_afk(user_id):
  afk_list.remove(user_id)

def print_afk():
  print(afk_list)


def check_afk(user_id):
  if user_id in afk_list:
    return True
  return False


@client.event
async def on_ready():
  print("Logged in!")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  author: discord.Member = message.author
  # GET DISPLAY NAME OR SERVER NICKNAME
  if (author.nick):
    nick = author.nick
  else:
    nick = author.display_name

  # checking to remove AFK
  if (check_afk(author.id)):
    remove_afk(author.id)
    nickname = nick.replace("[AFK] ", "")
    await author.edit(nick=nickname)
    embed = discord.Embed(title="AFK", description="AFK has been removed.", color=0x768bb7)
    await message.channel.send(embed=embed)

  # BASIC TESTING COMMAND
  if message.content.startswith("$hi"):
    embed = discord.Embed(title="Hi", description="I'm Shaan's Bot!", color=0x768bb7)
    await message.channel.send(embed=embed)

  # AFK COMMAND
  if message.content.startswith("$afk"):
    afk_msg = message.content.replace("$afk", "")

    # CHECK IF ALREADY AFK
    if "[AFK]" in nick or check_afk(author.id):
      embed = discord.Embed(title="FAILED ❌", description="You are already AFK!", color=0xFF0000)
      await message.channel.send(embed=embed)
    else:
      # ADD TO AFK_LIST
      add_afk(author.id)
      nickname = "[AFK] " + nick
      await author.edit(nick=nickname)

      if afk_msg != "":
        embed = discord.Embed(title="AFK", description=f"{afk_msg} AFK has been set!", color=0x768bb7)
      else:
        embed = discord.Embed(title="AFK", description="AFK has been set!", color=0x768bb7)

      await message.channel.send(embed=embed)


client.run(token)