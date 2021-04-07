import keep_alive
import discord
import os
import time
import discord.ext
import random
import emoji
import json
import asyncio
import datetime
from discord import Embed
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import MemberConverter 

from discord.ext.commands import has_permissions,  CheckFailure, check

intents = discord.Intents.all()

with open('owo.txt') as file:
  owos = json.load(file)

with open('cooldown.txt') as filee:
  cooldowns = json.load(filee)
def readData():
  with open('owo.txt') as f:
      owos = json.load(f)
  with open('cooldown.txt') as filee:
    cooldowns = json.load(filee)
def writeData():

  with open("owo.txt", "w") as outfile:
    json.dump(owos, outfile)
  with open('cooldown.txt', 'w') as filee:
    json.dump(cooldowns, filee)


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

owoprefix = ['owo', 'h']
newlist = [owoprefix[0] + s for s in allowocommands]
nextlist = [owoprefix[1] + s for  s in allowocommands]
list3 = [owoprefix[0] + ' ' + s for s in allowocommands]
list4 = [owoprefix[1] + ' ' + s for s in allowocommands]
alllist = newlist + nextlist + list3 + list4
def get_prefix(ctx,message):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
    default = 'm'
  return [prefixes[str(message.guild.id)], default]
  


bot = commands.Bot(intents = intents, command_prefix = get_prefix)
bot.remove_command('help')

@bot.event
async def on_guild_join(guild):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
  prefixes[str(guild.id)] = "m"
  with open("prefixes.json", "w") as f:
    json.dump(prefixes,f, indent=4)


@bot.command()
async def maxqualityreact(message, maxquality):
  if maxquality > 95 and maxquality < 100:
    await message.add_reaction('<a:Legendary:828000283949924352>')
  if maxquality == 100:
    await message.add_reaction('<a:Fabled:828000330117415002>')
  if maxquality > 81 and maxquality < 95:
    await message.add_reaction('<:mythic:828001905409785926>')
  if maxquality > 61 and maxquality < 81:
    await message.add_reaction('<:epic:828000457192243210>')
  if maxquality > 41 and maxquality < 61:
    await message.add_reaction('<:OwO_Rare:828002430431264789>')
  if maxquality > 21 and maxquality < 41:
    await message.add_reaction('<:uncommon:828002604163661865>')
  if maxquality > 0 and maxquality < 21:
    await message.add_reaction('<:OwO_Common:828002747235958805>')

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
 
    prefixes.pop(str(guild.id))
 
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.command(aliases = ['prefix'])
async def setprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
 
    prefixes[str(ctx.guild.id)] = prefix
 
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=  4)
 
    await ctx.send(f'The prefix is now: **``{prefix}``**')



@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "\n") 
    try: 
      readData()
      
    except:
      print("no")


@bot.command(aliases = ['setup'])

async def startall(ctx):
  readData()
  for user in ctx.guild.members:
    id = str(user.id)
    if id in owos:
      pass
    else:
      owos[id] = 0
  for user in ctx.guild.members:
    id = str(user.id)

    cooldowns[id] = 0
  writeData()

  await ctx.send("successfully setup!")

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start
@bot.event
async def on_message(message):
  
  try:
    if 'Great Sword' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        
        
        b = (a[a.find('**Description:** Deals '):a.find(' of your')])
        damage = b[25:-3]
        
        maxquality = ((((250-float(cost))+(float(damage)-35)*5) + 100)/3)
        lowest = ((((250-float(cost))+(float(damage)-35)*5) + 0)/3)

        await message.channel.send("Max Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        await maxqualityreact(message, maxquality)
    if 'Healing Staff' in message.embeds[0].description:
     if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        
        
        b = (a[a.find('**Description:** Heals '):a.find(' of your')])
        damage = b[25:-3]
        
        maxquality = (((200-float(cost))/75*100+2*(float(damage)-100)) + 100)/3
        lowest = (((200-float(cost))/75*100+2*(float(damage)-100)) + 0)/3
        await message.channel.send("Max Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        await maxqualityreact(message, maxquality)
    if 'Bow' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        b = (a[a.find('**Description:** Deals '):a.find(' of your')])
        damage = b[25:-3]
        
        maxquality = ((220-float(cost)) + 2*(float(damage)-110)+100)/3
        lowest = ((220-float(cost)) + 2*(float(damage)-110)+0)/3
        await message.channel.send("Max Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        await maxqualityreact(message, maxquality)
    if 'Aegis' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        
        b = (a[a.find('Reduces incoming damage by '):find_nth(a, "%", 2)])
        
        damage = b[29:-2]
       
        
        maxquality = ((250-float(cost)) + 5*(float(damage)-30)+100)/3
        lowest = ((250-float(cost)) + 5*(float(damage)-30)+0)/3
        await message.channel.send("Max Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        await maxqualityreact(message, maxquality)
    if 'Orb of Potency' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
       await message.channel.send("orb noob")
    if 'Vampiric Staff' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        b = (a[a.find('**Description:** Deal '):a.find(' of your')])
        damage = b[24:-3]
        
        maxquality = ((200-float(cost)) + 5*(float(damage)-25)+100)/3
        lowest = ((200-float(cost)) + 5*(float(damage)-25)+0)/3
        await message.channel.send("Max Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        await maxqualityreact(message, maxquality)
    if 'Energy Staff' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        b = (a[a.find('**Description:** Sends a wave of energy and deals '):a.find(' of your')])
        damage = b[52:-3]
        
        
        maxquality = ((200-float(cost)) + 100/30*(float(damage)-35)+100)/3
        lowest = ((200-float(cost)) + 100/30*(float(damage)-35)+0)/3
        await message.channel.send("Max Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        await maxqualityreact(message, maxquality)
    if 'Arcane Scepter' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        b = (a[a.find('**Description:** Replenish '):a.find(' of your')])
        damage = b[29:-3]
        
        
        maxquality = (4/3*(200-float(cost)) + 100/30*(float(damage)-40)+100)/3
        lowest = (4/3*(200-float(cost)) + 100/30*(float(damage)-40)+0)/3
        await message.channel.send("Max Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        maxqualityreact(maxquality)
    if 'Resurrection Staff' in message.embeds[0].description: 
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        b = (a[a.find('**Description:** Revive a dead ally and heal them for '):a.find(' of your')])
        damage = b[56:-3]
        
        
        maxquality = ((400-float(cost)) + 100/30*(float(damage)-50)+100)/3
        lowest = ((400-float(cost)) + 100/30*(float(damage)-50)+0)/3
        await message.channel.send("Max Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        await maxqualityreact(message, maxquality)
    if 'Glacial Axe' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        
        
        b = (a[a.find('**Description:** Deals '):a.find(' of your')])
        damage = b[25:-3]
        
        maxquality = ((((220-float(cost))+(float(damage)-50)*100/30) + 100)/3)
        lowest = ((((220-float(cost))+(float(damage)-50)*100/30) + 0)/3)
        await message.channel.send("Max Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        await maxqualityreact(message, maxquality)    
    if 'Poison Dagger' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        b = (a[a.find('**Description:** Deals '):a.find(' of your')])
        damage = b[25:-3]
        c = (a[a.find('**Poison** - Deals '): a.find(' MAG as')])
        poison = c[21:-37]
        maxactualquality = ((200-float(cost))+((float(damage)-70)/30*100)+((float(poison)-40)/25*100)+(100))/4
        lowest = ((200-float(cost))+((float(damage)-70)/30*100)+((float(poison)-40)/25*100)+(0))/4
    
        maxquality = (((200-float(cost))+(float(poison)-40)/25*100)+100)/3
        await message.channel.send("Max Quality: "+ str(maxactualquality))
        await message.channel.send("Lowest Quality: "+ str(lowest))
        await message.channel.send("Max Important Quality: " + str(maxquality))
        await maxqualityreact(message, maxquality)
    if 'Wand of Absorption' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        b = (a[a.find('**Description:** Deal '):a.find(' of your')])
        damage = b[24:-3]
        
        c = (a[a.find('equal to '):find_nth(a, "%", 3)])
        replenish = c[11:]
      
        maxquality = ((250-float(cost))+((float(damage)-80)/20*100)+((float(replenish)-20)/20*100)+(100))/4
        lowest = ((250-float(cost))+((float(damage)-80)/20*100)+((float(replenish)-20)/20*100)+(0))/4
        await message.channel.send("Max Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        await maxqualityreact(message, maxquality)
    if 'Spirit Staff' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        
        
        b = (a[a.find('**Description:** Heal all allies for '):a.find(' of your')])
        heal = b[39:-3]

        c = (a[a.find('incoming damage by '):find_nth(a, "%", 3)])
        defup = c[21:]
      
        maxquality = ((225-float(cost))+((float(heal)-30)/20*100)+((float(defup)-20)/10*100)+(100))/4
        lowest = ((225-float(cost))+((float(heal)-30)/20*100)+((float(defup)-20)/10*100)+(0))/4
        await message.channel.send("Max Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        await maxqualityreact(message, maxquality)     
    if 'Culling Scythe' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        
        
        b = (a[a.find('**Description:** Deals '):a.find(' of your')])
        damage = b[25:-3]
       
        c = (a[a.find('animal by '):find_nth(a, "%", 3)])
        mortality = c[12:]
       
        
        maxquality = ((200-float(cost))+((float(mortality)-30)/30*100)+(100))/3
        maxactualquality = ((200-float(cost))+((float(damage)-70)/30*100)+((float(mortality)-30)/30*100)+(100))/4
        lowest = ((200-float(cost))+((float(damage)-70)/30*100)+((float(mortality)-30)/30*100)+(0))/4
        await message.channel.send("Max Actual Quality: " + str(maxactualquality))
        await message.channel.send("Max Important Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        
       
        await maxqualityreact(message, maxquality)  
    if 'Banner' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        
        b = (a[a.find('**Attack Up** - Increases all damage by '): find_nth(a, "%", 2)])
        buff1 = b[42:]
        c = (a[find_nth(a,'Increases all damage by ', 2 ): find_nth(a, "%", 3)])
        buff2 = c[26:]
        d = (a[find_nth(a,'Increases all damage by ', 3 ): find_nth(a, "%", 4)])
        buff3 = d[26:]
        
        
        maxquality = ((300-float(cost))*2 + (float(buff1)-10)*10 + (float(buff2)-20)*10 + (float(buff3)-30)*10+100)/5
        lowest = ((300-float(cost))*2 + (float(buff1)-10)*10 + (float(buff2)-20)*10 + (float(buff3)-30)*10+0)/5
        await message.channel.send("Max Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        await maxqualityreact(message, maxquality)
    if 'Flame Staff' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        
        
        b = (a[a.find('**Description:** Deals '):a.find(' of your')])
        damage = b[25:-3]
        c = (a[find_nth(a, 'Deals', 2):find_nth(a,'of your', 2)])
        flame = c[8:-4]
        d = (a[find_nth(a, 'deal ', 1):find_nth(a,'%', 4)])
        explosion = d[7:]
        

        maxquality = ((200-float(cost))+((float(damage)-60)/20*100)+((float(flame)-20)/20*100)+((float(explosion)-40)/20*100)+(100))/5
        lowest = ((200-float(cost))+((float(damage)-60)/20*100)+((float(flame)-20)/20*100)+((float(explosion)-40)/20*100)+(0))/5

        await message.channel.send("Max Quality: " + str(maxquality))
        await message.channel.send("Lowest Quality: " + str(lowest))
        await maxqualityreact(message, maxquality)
    if 'Rune' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
       await message.add_reaction('<:N104rune:828341609400631298>')

  except:
    
    pass

  await bot.loop.create_task(counter(message))

  await bot.process_commands(message)

owoprefix = ['owo', 'h']




async def counter(message):
  userid = str(message.author.id)
  id = message.id

  ts = id >> 22
  readData()
  print(ts)


  for i in owoprefix:


    if i in message.content and message.author.bot == False:
      if any(word in message.content for word in alllist):

        print('1')
    
      if ts - cooldowns[userid] > 10000:

        if userid not in owos:
          print("please set up the bot with {prefix}setup")

          
        else:
          
          cooldowns[userid] = ts
          owos[userid] += 1
          storedTS = ts

          writeData()



          



 


@bot.command(aliases = ['reset'])
async def clear(ctx, user: discord.Member):
  readData()
  
  userid = str(user.id)
  owos[userid] = 0
  await ctx.send(str(user) + "'s owos has been reset.")
  writeData()


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

  try:
    embed = discord.Embed(title="Leaderboard", color=0x42b7ff)
    with open('owo.txt', 'r') as file:
        data = json.load(file)

    sorted_data = {id: bal for id, bal in sorted(data.items(), reverse=True ,key=lambda item: item[1])}

    for pos, (id, bal) in enumerate(sorted_data.items()):
        member = ctx.guild.get_member(int(id))
        embed.add_field(name=f"{pos+1} - {member.display_name}", 
        value=f"{bal} owos", inline=False)

        if pos+1 > number - 1:
            break 
    await ctx.send(embed=embed)
    
  except:
    await ctx.send("invalid!")

    
spankgifs = ['https://media.tenor.com/images/fa746bf2689ab4c7b1cc1e39ab2219d5/tenor.gif', 'https://media.discordapp.net/attachments/826857266455642122/828395321716768768/Spank.gif', 'https://media.tenor.com/images/7072c796c7e0a29930721c5f457d563c/tenor.gif', 'https://media.tenor.com/images/d75aead0dbf59fff4b996ebfecde0560/tenor.gif','https://media.discordapp.net/attachments/829452143006056560/829452211452641310/Spank_Me_Daddy.png']
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def spank(message, *, member: discord.Member):
  await message.channel.send('You'  + " spank " + member.mention + " !")

  
  embed=discord.Embed(title=member.name + " gets a spank!")
  embed.set_image(url = random.choice(spankgifs))
  embed.set_footer(text=(str(message.author.name)  + " spanks " + member.name+ "!"))
  await message.channel.send(embed=embed) 
  




@bot.command(aliases = ['coinflip'])  
async def cf(ctx, headtail: str):
  try:
    if(headtail != "head") and headtail != "tail":
      headtail = random.choice("head", "tail")
    else:
    
      choices = ["head","tail"]
      a = random.choice(choices)
    
      if a == headtail:
        embed=discord.Embed(title="Coinflip! ", description=("the coin landed on " + a + " you good good!!!"), color=0x00ff08)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://gifimage.net/wp-content/uploads/2017/10/coin-flip-gif-3.gif")
        embed.set_footer(text="coopw is cute")
        await ctx.send(embed=embed)

      else:
        embed=discord.Embed(title="Coinflip! ", description=("the coin landed on " + a + " you bad bad!!!"), color=0xff0000)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://gifimage.net/wp-content/uploads/2017/10/coin-flip-gif-3.gif")
        embed.set_footer(text="coopw is cute")
        await ctx.send(embed=embed)
  except:
    await ctx.send("error!")

@bot.command(aliases = ['owostat'])
async def stat(ctx, user: discord.Member):
  readData()
  id = str(user.id)
  embed=discord.Embed(title= (user.name + "'s owos"), description=(user.name + " has " + str(owos[id]) + " owos"), color=0x00ff59)
  embed.set_footer(text="coolw")
  await ctx.send(embed=embed)
@bot.command()
async def resetall(ctx):


  await ctx.send("resetting!")
  readData()
  for user in ctx.guild.members:
    id = str(user.id)
    owos[id] = 0
  writeData()
  await ctx.send('done!')





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





keep_alive.keep_alive()
token = os.environ.get("token")
bot.run(token)
