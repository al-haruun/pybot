import discord
import asyncio
import datetime
import json

client = discord.Client()
prefix = "%"

@client.event
async def on_ready():
    print("Logged in as:", client.user.name)
    print("ID:", client.user.id)
    print("Bot ready")
    await client.change_presence(game=discord.Game(name="Use %help", type=0))

@client.event
async def on_member_join(member):
    embed = discord.Embed(title="Welcome %s to %s" % (member.name, member.server.name) , colour= 0x2ecc71)
    await client.send_message(client.get_channel('323451887061958677'), embed=embed)

@client.event
async def on_member_remove(member):
    embed = discord.Embed(title="%s left %s for a better world..." % (member.name, member.server.name), colour = 0xe74c3c)
    await client.send_message(client.get_channel('323451887061958677'), embed=embed)

@client.event
async def on_message(message):

    if message.content == prefix + "ping":
        await client.send_message(message.channel, ":ping_pong:Pong !")

    elif message.content == prefix + "profile":   
               
        embed = discord.Embed(title = str("_" + message.author.name + "_") + "'s profile", colour= message.author.roles[-1].colour)
        embed.set_author(name="Profile page")
        embed.set_thumbnail(url= message.author.avatar_url)
        embed.add_field(name= "Username", value= str(message.author.display_name), inline=False)
        embed.add_field(name= "ID", value= str(message.author.id), inline=False)
        embed.add_field(name= "Role", value= str(message.author.roles[-1].name), inline=False)
        embed.add_field(name= "Date of creation", value= str(message.author.created_at.strftime("%x")), inline=False)
        embed.add_field(name= "Status", value= str(message.author.status), inline=False)
        embed.add_field(name= "Playing to", value= str(message.author.game), inline=False)
        embed.set_footer(text= str(message.timestamp.strftime("%X")), icon_url= message.channel.server.icon_url )
        await client.send_message(message.channel, embed=embed)

    elif message.content == prefix + "github":
        await client.send_message(message.channel, "https://github.com/Tusquito/pybot")
   
    elif message.content == prefix +"test":
         await client.send_message(message.channel, "Test")
    
    elif message.content ==  prefix + "help":

        embed = discord.Embed(title ="__Commands__", colour= 0xf1c40f)
        embed.set_author(name="Help page")
        embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/323451887061958677/521021725765271572/512px-Circle-icons-settings.png")
        embed.add_field(name= "Profile", value="Syntax : %profile <mentionUser>, show all informations about the user mentioned.", inline=False)
        embed.set_footer(text= str(message.timestamp.strftime("%X")), icon_url= message.channel.server.icon_url )
        await client.send_message(message.channel, embed=embed)   
    
    elif message.content ==  prefix + "profile " + message.mentions[0].mention:

        mentioned = message.mentions[0]
        embed = discord.Embed(title = str("_" + mentioned.name + "_") + "'s profile", colour= mentioned.roles[-1].colour)
                    
        embed.set_author(name="Profile page")
        embed.set_thumbnail(url= mentioned.avatar_url)
        embed.add_field(name= "Username", value= str(mentioned.display_name), inline=False)
        embed.add_field(name= "ID", value= str(mentioned.id), inline=False)
        embed.add_field(name= "Role", value= str(mentioned.roles[-1].name), inline=False)
        embed.add_field(name= "Date of creation", value= str(mentioned.created_at.strftime("%x")), inline=False)
        embed.add_field(name= "Status", value= str(mentioned.status), inline=False)
        embed.add_field(name= "Playing to", value= str(mentioned.game), inline=False)
        embed.set_footer(text= str(message.timestamp.strftime("%X")), icon_url= message.channel.server.icon_url )
        await client.send_message(message.channel, embed=embed)
   

with open('token.json') as json_file:  
    data = json.load(json_file) 


client.run(data['token'])
