import discord
import asyncio
import datetime

client = discord.Client()
prefix = "%"
@client.event
async def on_ready():
    print("Logged in as:", client.user.name)
    print("ID:", client.user.id)
    print("Bot ready")

@client.event
async def on_member_join(member):
    embed = discord.Embed(colour= g)
    embed.description("Welcome "+ member.mention + " !")

    await client.send_message(server.default_channel, embed=embed)

@client.event
async def on_message(message):

    if message.content == prefix + "ping":
        await client.send_message(message.channel, ":ping_pong:Pong !")

    elif message.content == prefix + "profile":   
        Timestamp = str(message.timestamp.strftime("%X") + message.timestamp.strftime(" %Z"))
       
        embed = discord.Embed(title = str("_" + message.author.name + "_") + "'s profile", colour= message.author.roles[-1].colour)
                    
        embed.set_author(name="Profile page")
        embed.set_thumbnail(url= message.author.avatar_url)
        embed.add_field(name= "Username", value= str(message.author.display_name), inline=False)
        embed.add_field(name= "ID", value= str(message.author.id), inline=False)
        embed.add_field(name= "Role", value= str(message.author.roles[-1].name), inline=False)
        embed.add_field(name= "Date of creation", value= str(message.author.created_at.strftime("%x")), inline=False)
        embed.add_field(name= "Status", value= str(message.author.status), inline=False)
        embed.add_field(name= "Playing to", value= str(message.author.game), inline=False)
        embed.set_footer(text= Timestamp, icon_url= message.channel.server.icon_url )
        await client.send_message(message.channel, embed=embed)     
    elif message.content == prefix + "github":
        await client.send_message(message.channel, "")
        
client.run("")