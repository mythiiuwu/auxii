import keep_alive
import discord
import os
import time
import discord.ext
import random
import emoji
from discord import Embed
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = "m")
@client.event
async def on_ready():
    print("bot online")

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start    

@client.event
async def on_message(message):
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
        await message.channel.send(maxactualquality)
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

        
    
  
@client.command()
async def ping(ctx):
    await ctx.send("pong!")
    await ctx.send("@everyone") 
@client.command()
async def kick(ctx, member : discord.Member, reason = None):
    try:
        await client.kick(reason=reason)
        await ctx.send("kicked "+member.mention) 
        
    except:
        await ctx.send("bot does not have the kick members permission!")
@client.command()
async def ban(ctx, member : discord.Member, reason = None):
  try:
    if reason is None:
      await client.ban()
      await ctx.send("banned" + member.mention)
    else:
      await client.ban(reason=reason)
      await ctx.send("banned" + member.mention + reason)
  except:
    await ctx.send("no perms!")

@client.command()  
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@client.command()  
async def cf(ctx, headtail: str):
  if(headtail != "head") and headtail != "tail":
    await ctx.send("invalid")
  else:
    
    choices = ["head","tail"]
    a = random.choice(choices)
    
    if a == headtail:
       await ctx.send("the coin landed on " + a + " you were correct")
    else:
      await ctx.send("the coin landed on " + a + " you were wrong")
@client.command()  
async def coinflip(ctx, headtail: str):
  if(headtail != "head") and headtail != "tail":
    await ctx.send("invalid")
  else:
    
    choices = ["head","tail"]
    a = random.choice(choices)
    
    if a == headtail:
       await ctx.send("the coin landed on " + a + " you were correct")
    else:
      await ctx.send("the coin landed on " + a + " you were wrong")

keep_alive.keep_alive()
token = os.environ.get("token")
client.run(token)
