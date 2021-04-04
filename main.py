import keep_alive
import discord
import os
import time
import discord.ext
import random
import emoji
import json
from discord import Embed
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^



def get_prefix(client, message):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]
  

client = commands.Bot(command_prefix = get_prefix)
@client.event
async def on_guild_join(guild):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
  prefixes[str(guild.id)] = "m"
  with open("prefixes.json", "w") as f:
    json.dump(prefixes,f, indent=4)





@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
 
    prefixes.pop(str(guild.id))
 
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def setprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
 
    prefixes[str(ctx.guild.id)] = prefix
 
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=  4)
 
    await ctx.send(f'The prefix is now: **``{prefix}``**')



@client.event
async def on_ready():
    print("Logged in as: " + client.user.name + "\n") #screw u

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start    

@client.event
async def on_message(message):
  await client.process_commands(message)
  try:

    if 'Great Sword' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        
        
        b = (a[a.find('**Description:** Deals '):a.find(' of your')])
        damage = b[25:-3]
        
        maxquality = ((((250-float(cost))+(float(damage)-35)*5) + 100)/3)
        await message.channel.send("Max Quality: " + str(maxquality))
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')
    if 'Healing Staff' in message.embeds[0].description:
     if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        
        
        b = (a[a.find('**Description:** Heals '):a.find(' of your')])
        damage = b[25:-3]
        
        maxquality = (((200-float(cost))/75*100+2*(float(damage)-100)) + 100)/3
        await message.channel.send("Max Quality: " + str(maxquality))
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')
    if 'Bow' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        b = (a[a.find('**Description:** Deals '):a.find(' of your')])
        damage = b[25:-3]
        
        maxquality = ((220-float(cost)) + 2*(float(damage)-110)+100)/3
        await message.channel.send("Max Quality: " + str(maxquality))
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')
    if 'Aegis' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        
        b = (a[a.find('Reduces incoming damage by '):find_nth(a, "%", 2)])
        
        damage = b[29:-2]
       
        
        maxquality = ((250-float(cost)) + 5*(float(damage)-30)+100)/3
        await message.channel.send("Max Quality: " + str(maxquality))
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')
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
        await message.channel.send("Max Quality: " + str(maxquality))
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')
    if 'Energy Staff' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        b = (a[a.find('**Description:** Sends a wave of energy and deals '):a.find(' of your')])
        damage = b[52:-3]
        
        
        maxquality = ((200-float(cost)) + 100/30*(float(damage)-35)+100)/3
        await message.channel.send("Max Quality: " + str(maxquality))
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')
    if 'Arcane Scepter' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        b = (a[a.find('**Description:** Replenish '):a.find(' of your')])
        damage = b[29:-3]
        
        
        maxquality = (4/3*(200-float(cost)) + 100/30*(float(damage)-40)+100)/3
        await message.channel.send("Max Quality: " + str(maxquality))
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')
    if 'Resurrection Staff' in message.embeds[0].description: 
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        b = (a[a.find('**Description:** Revive a dead ally and heal them for '):a.find(' of your')])
        damage = b[56:-3]
        
        
        maxquality = ((400-float(cost)) + 100/30*(float(damage)-50)+100)/3
        await message.channel.send("Max Quality: " + str(maxquality))
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')
    if 'Glacial Axe' in message.embeds[0].description:
      if message.author.id == 408785106942164992 and message.embeds[0].description.__contains__('**Owner:**'):
        a = message.embeds[0].description
        costdesc = (a[a.find('**WP Cost:** '):a.find('\n**Description')-25])
        cost = costdesc[13:]
        
        
        b = (a[a.find('**Description:** Deals '):a.find(' of your')])
        damage = b[25:-3]
        
        maxquality = ((((220-float(cost))+(float(damage)-50)*100/30) + 100)/3)
        await message.channel.send("Max Quality: " + str(maxquality))
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')       
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
    
        maxquality = (((200-float(cost))+(float(poison)-40)/25*100)+100)/3
        await message.channel.send("Max Quality: "+ str(maxactualquality))
        await message.channel.send("Max Important Quality: " + str(maxquality))
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')
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
        await message.channel.send("Max Quality: " + str(maxquality))
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')
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
        await message.channel.send("Max Quality: " + str(maxquality))
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')      
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
        await message.channel.send("Max Actual Quality: " + str(maxactualquality))
        await message.channel.send("Max Important Quality: " + str(maxquality))

        
       
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')  
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
        

        

        await message.channel.send("Max Quality: " + str(maxquality))
        if maxquality > 95 and maxquality < 100:
          await message.add_reaction('<a:Legendary:828000283949924352>')
        if maxquality == 100:
          await message.add_reaction('<a:Fabled:828000330117415002>')
        if maxquality > 80 and maxquality < 95:
          await message.add_reaction('<:mythic:828001905409785926>')
        if maxquality > 60 and maxquality < 80:
          await message.add_reaction('<:epic:828000457192243210>')
        if maxquality > 40 and maxquality < 60:
          await message.add_reaction('<:OwO_Rare:828002430431264789>')
        if maxquality > 20 and maxquality < 40:
          await message.add_reaction('<:uncommon:828002604163661865>')
        if maxquality > 0 and maxquality < 20:
          await message.add_reaction('<:OwO_Common:828002747235958805>')


  except:
    
    pass
    
    
@client.command()
async def info(ctx):
  embed=discord.Embed(title="Haiiiiii!", description="Made by mythii#9555!\ncoopw#1111 helped mythii not be an idiot", color=0x70ffee)
  embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
  embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/719721942742990889/6999b9abe3d5c863a26c61695c75c240.png?size=256")
  embed.set_footer(text="coop is cute")
  await ctx.send(embed=embed)
client.remove_command('help')
@client.command()
async def help(ctx):
  embed=discord.Embed(title="OwObot Helper", color=0x70ffee)
  embed.add_field(name="Ping", value="Gets client latency", inline=False)
  embed.add_field(name="Info", value="Shows client info", inline=False)
  embed.add_field(name="Choose", value="{prefix}choose {a} {b}, chooses random choice", inline=False)
  embed.add_field(name="cf/coinflip", value="{prefix}cf {head or tail}, will generate a coinflip", inline=False)
  embed.set_footer(text="coop is cute")
  await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    ms = client.latency * 1000
    await ctx.send('Pong! ' + str(ms) + ' ms')

@client.command()  
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@client.command(aliases = ['coinflip'])  
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













keep_alive.keep_alive()
token = os.environ.get("token")
client.run(token)
