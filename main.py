import keep_alive
import discord
import os
import time
import discord.ext
import random
import emoji
import json
import asyncio
import dns
import datetime
import pymongo
from bson.objectid import ObjectId
from pymongo import MongoClient
from discord import Embed
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import MemberConverter 

from discord.ext.commands import has_permissions,  CheckFailure, check

intents = discord.Intents.all()


#add counting hunts




allowocommands = ["ab", "acceptbattle","battle", "b", "fight", "battlesetting", "bs", "battlesettings","crate", "weaponcrate", "wc","db", "declinebattle","pets", "pet","rename","team", "squad",
"teams", "setteam", "squads", "useteams","weapon", "w", "weapons", "wep","weaponshard", "ws", "weaponshards", "dismantle","claim", "reward", "compensation","cowoncy", "money", "currency", "cash", "credit", "balance","daily","give", "send","quest","gif", "pic",
"blush", "cry", "dance", "lewd", "pout", "shrug", "sleepy", "smile", "smug", "thumbsup", "wag", "thinking","triggered", "teehee", "deredere", "thonking", "scoff", "happy", "thumbs", "grin","cuddle", "hug", "kiss", "lick", "nom", "pat", "poke", "slap", "stare", "highfive", "bite", "greet", "punch","handholding", "tickle", "kill", "hold", "pats", "wave", "boop", "snuggle", "fuck", "sex",
"blackjack", "bj", "21","coinflip", "cf", "coin", "flip",
"drop", "pickup","lottery", "bet", "lotto","slots", "slot", "s",
"communism", "communismcat","distractedbf", "distracted","drake","eject", "amongus","emergency", "emergencymeeting","headpat",
"isthisa","slapcar", "slaproof","spongebobchicken", "schicken",
"bully", "pika", "pikapika","alastor", "army", "gauntlet", "piku",
"bunny", "cake", "java", "crown", "cpc", "dish", "donut", "icecream", "lollipop", "meshi", "milk","pizza", "poutine", "rose", "bouquet", "rum", "sharingan", "slime", "teddy", "yy","coffee", "cupachicake", "yinyang","tarot","bell", "strengthtest","roll", "d20","choose", "pick", "decide","my", "me", "guild","top", "rank", "ranking","buy","describe", "desc","equip", "use","inventory", "inv","shop", "market","acceptmarriage", "am","cookie", "rep",
"declinemarriage", "dm","define","divorce","eightball", "8b", "ask", "8ball","emoji", "enlarge", "jumbo","level", "lvl", "levels", "xp","propose", "marry", "marriage", "wife", "husband","owo", "owoify", "ify","pray", "curse","profile","ship", "combine","translate", "listlang","wallpaper", "wp", "wallpapers", "background", "backgrounds","announce", "changelog", "announcement", "announcements","avatar", "user","censor","checklist", "task", "tasks", "cl","color", "randcolor", "colour", "randcolour","covid", "cv", "covid19", "coronavirus","disable","enable","feedback", "question", "report", "suggest","guildlink","help","invite", "link",
"math", "calc", "calculate","merch","patreon", "donate","ping", "pong","prefix","rule", "rules","shards", "shard","stats", "stat", "info","uncensor","vote","autohunt", "huntbot", "hb","hunt", "h", "catch","lootbox", "lb","owodex", "od", "dex", "d","sacrifice", "essence", "butcher", "sac", "sc","sell","upgrade", "upg","zoo",]
allcommands = []
owoprefix = ['owo', 'h']
for i in owoprefix:
  for x in allowocommands:
    allcommands.append(i+x)
    allcommands.append(i + ' ' + x)



bot = commands.Bot(intents = intents, command_prefix = "m")
bot.remove_command('help')

dbclient = pymongo.MongoClient("mongodb+srv://mythii:auxii@cluster0.xonkd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")




owos = dbclient['mythii']['owos']
alltime = dbclient['mythii']['alltime']
yesterday = dbclient['mythii']['yesterday']
@bot.event 
async def on_member_join(member):
  
  id = str(member.id)
  yesterday.update_one(
      {"id": member.id},
      {"$set":{"owos":0}},
      upsert = True
    )
  owos.update_one(
      {"id": member.id},
      {"$set":{"owos":0}},
      {"$set": {"cooldowns":0}},
      upsert = True
    )
  alltime.update_one(
      {"id": member.id},
      {"$set":{"owos":0}},
      upsert = True
    )




@bot.event
async def on_guild_join(guild):
  for user in guild.members:
    
    id = str(user.id)

    yesterday.update_one(
        {"id": user.id},
        {"$set":{"owos":0}},
        upsert = True
      )
    owos.update_one(
        {"id": user.id},
        {"$set":{"owos":0}},
        {"$set": {"cooldowns":0}},
        upsert = True
      )
    alltime.update_one(
        {"id": user.id},
        {"$set":{"owos":0}},
        upsert = True
      )


      



@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "\n") 



@bot.command()

async def setupmythiionly(ctx):  

  for user in ctx.guild.members:
    id = str(user.id)
    print(id)
    test = owos.find_one({"id": user.id})
    if test is None:
      yesterday.update_one(
          {"id": user.id},
          {"$set":{"owos":0}},
          upsert = True
        )
      owos.update_one(
          {"id": user.id},
          {"$set":{"owos":0}},
          upsert = True
        )
      owos.update_one(
          {"id": user.id},  
          {"$set":{"cooldowns":0}},
          upsert = True
        )
      alltime.update_one(
          {"id": user.id},
          {"$set":{"owos":0}},
          upsert = True
        )
  

  await ctx.send("successfully setup!")

owoprefix = ['owo', 'h']


@bot.event
async def on_message(message):
  try: 
    userid = str(message.author.id)
    id = message.id

    ts = id >> 22
    userstats = owos.find_one({"id" : message.author.id})

  
    for i in owoprefix:
      if i in message.content and message.author.bot == False:
        if  any(message.content.lower().startswith(x) for x in allcommands):
          break
        elif ts - userstats["cooldowns"] > 15000:
          if userstats is None:
            print("please set up the bot with {prefix}setup")
          else:

            owos.update_one(
                {"id":message.author.id },
                {"$inc":{"owos":1}} 
              )
            alltime.update_one(
                {"id":message.author.id },
                {"$inc":{"owos":1}} 
              )

            owos.update_one({"id":message.author.id}, {"$set":{"cooldowns": ts}})
  except:
    print(message.author.id)
    print(message.content)
 
  await bot.process_commands(message)






        

@bot.command(aliases = ['reset'])
async def clear(ctx, user: discord.Member):
  
  try:
    resetuser = {"id" : user.id, "owos" : 0}
    owos.update_one(resetuser)

    await ctx.send(str(user) + "'s owos has been reset.")
  except:
    ctx.send("invalid!!!")


  


@bot.command()
async def info(ctx):
  embed=discord.Embed(title="Haiiiiii!", description="Made by mythii#9555!\ncoopw#1111 helped mythii not be an idiot", color=0x70ffee)
  embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
  embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/719721942742990889/6999b9abe3d5c863a26c61695c75c240.png?size=256")
  embed.set_footer(text="coop is cute")
  await ctx.send(embed=embed)
  


@bot.command(aliases = ["howto"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(message):
  embed=discord.Embed(title="OwObot Helper", color=0x70ffee)
  embed.add_field(name="Ping", value="Gets bot latency", inline=False)
  embed.add_field(name="Info", value="Shows bot info", inline=False)
  embed.add_field(name="Choose", value="{prefix}choose {a} {b}, chooses random choice", inline=False)
  embed.add_field(name="cf/coinflip", value="{prefix}cf {head or tail}, will generate a coinflip", inline=False)
  embed.add_field(name="prefix", value="sets a new prefix for the server", inline=False)
  embed.set_footer(text="coop is cute")
  await message.channel.send(embed=embed)


@bot.command()
async def ping(ctx):
    ms = bot.latency * 1000
    await ctx.send('Pong! ' + str(ms) + ' ms')

@bot.command()  
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command(aliases = ['top', 'lb'])
async def leaderboard(ctx, number: int):


  embed = discord.Embed(title="Leaderboard", color=0x42b7ff)
  i = 1
  data = owos.find().sort("owos",-1)
  for x in data:
    try:
      temp = ctx.guild.get_member(x["id"])
      tempowo = x["owos"]
      embed.add_field(name = f"{i}: {temp.name}", value =f"Top OwOs Today: {tempowo} ", inline=False)
      i += 1
    except:
      pass
    if i == number + 1:
      break
  await ctx.send(embed=embed)


    
spankgifs = ['https://media.tenor.com/images/fa746bf2689ab4c7b1cc1e39ab2219d5/tenor.gif', 'https://media.discordapp.net/attachments/826857266455642122/828395321716768768/Spank.gif', 'https://media.tenor.com/images/7072c796c7e0a29930721c5f457d563c/tenor.gif', 'https://media.tenor.com/images/d75aead0dbf59fff4b996ebfecde0560/tenor.gif','https://media.discordapp.net/attachments/829452143006056560/829452211452641310/Spank_Me_Daddy.png']
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def spank(message, *, member: discord.Member):
  await message.channel.send('You'  + " spank " + member.mention + " !")

  
  embed=discord.Embed(title=member.name + " gets a spank!")
  embed.set_image(url = random.choice(spankgifs))
  embed.set_footer(text=(str(message.author.name)  + " spanks " + member.name+ "!"))
  await message.channel.send(embed=embed) 
  






@bot.command(aliases = ['owostat'])
async def stat(ctx,member: discord.Member = None):

  if(member is None):
    user = ctx.message.author
  else:
    user = member
  userstats = owos.find_one({"id" : user.id})
  yesterdaystats = yesterday.find_one({"id" : user.id})
  alltimestats = alltime.find_one({"id" : user.id})
  owonum = userstats["owos"]
  yesterdaynum = yesterdaystats["owos"]
  alltimenum = alltimestats["owos"]
  
  embed=discord.Embed(title= (user.name + "'s owos"), color=0x00ff59)
  embed.add_field(name = "today: ", value = str(owonum))
  embed.add_field(name="yesterday: " , value=str(yesterdaynum), inline=True)
  embed.add_field(name = "all time: ", value = str(alltimenum))

  
  
  await ctx.send(embed=embed)






@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def suggest(message,*, suggestion: str):
  channel = bot.get_channel(828819989422145567)
  try:
    embed=discord.Embed(title = (message.author.name +  "'s suggestion"), description= suggestion)
    
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)

    embed.set_footer(text="coop is cute")


    sent = await channel.send(embed=embed)
    await sent.add_reaction('<:hy_check:828831373514768405>')
    await sent.add_reaction(('<:hyx:828831379861143553>'))
    await greenred(embed)
  except:
    message.channel.send("you are still on cooldown!")
  await bot.process_commands(message)

def seconds_until(hours, minutes):
    given_time = datetime.time(hours, minutes)
    now = datetime.datetime.now()
    future_exec = datetime.datetime.combine(now, given_time)
    if (future_exec - now).days < 0:  
      future_exec = datetime.datetime.combine(now + datetime.timedelta(days=1), given_time) 

    return (future_exec - now).total_seconds()

print(seconds_until(6,59))
@tasks.loop(hours = 24)
async def dailyreset():
  await asyncio.sleep(seconds_until(6,59))

  for guild in bot.guilds:

    for user in guild.members:
      try:
        id = str(user.id)
        userstats = owos.find_one({"id" : user.id})
        yesterdaynum = userstats["owos"] 
        yesterday.update_one(
        {"id": user.id},
        {"$set":{"owos":yesterdaynum}}
        )
      except:
        pass
    for user in guild.members:
      try:
        id = str()
        owos.update_one(
        {"id": user.id},
        {"$set":{"owos":0}},
        )
      except:
        pass


dailyreset.start()



keep_alive.keep_alive()
token = os.environ.get("token")
bot.run(token)
