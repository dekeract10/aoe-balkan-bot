#!/bin/env python3 

import discord
import getelo
import re

client = discord.Client()

role_list = []
member_list = []
test_role = []

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    # discord.Intents.all()
    discord.Intents.members = True

    guild_list = await client.fetch_guilds(limit=150).flatten()

    for guild in guild_list:
        role_list = await guild.fetch_roles()

    #print("role list =", role_list)

    # Take only roles that we will need later
        
    for role in role_list:
        #print(role.name)
        if "Test" in role.name:
            test_role.append(role)

    #print(test_role)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "Fixxxer" in message.author.name:
        await message.add_reaction("\U0001F921")

    if message.content.startswith("!check "):
        url = message.content.split(" ")[1]

        steam_id = False

        if (url.startswith("https://steamcommunity.com/")):
            steam_id = True  
        else:
            if (not url.startswith("https://aoe2.net/")):
                await message.channel.send("Error, try again!")
                return

        ID = getelo.get_id(url)
    
        elo = getelo.get_elo(ID, steam_id)
        #print(elo)

        await message.channel.send("Tvoj elo: " + str(elo))
    

    # print(role_list)

    #print(test_role)
    #if message.content == "!addrole":
    #    await message.author.add_roles(test_role[0])


client.run("TOKEN")

#client.run(input("Unesi token:"))
