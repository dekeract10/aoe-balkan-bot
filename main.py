#!/bin/env python3 

import discord

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

    print("role list =", role_list)

    # Take only roles that we will need later
        
    for role in role_list:
        print(role.name)
        if "Test" in role.name:
            test_role.append(role)

    print(test_role)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "Fixxxer" in message.author.name:
        await message.add_reaction("\U0001F921")

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    

    # print(role_list)

    print(test_role)
    if message.content == "!addrole":
        await message.author.add_roles(test_role[0])



client.run(input("Unesi token:"))
