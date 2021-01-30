import discord
import os
import requests
from bs4 import BeautifulSoup
import praw
import pandas as pd
from PIL import Image
import random

print("started")

client = discord.Client()

reddit = praw.Reddit(client_id="FdRi0pFXO14bTQ",      # your client id
                     client_secret="Zr464LITLlGgTbmxNRTewgCkOTvaCg",  # your client secret
                     user_agent="octobot",  # user agent name
                     )


def cat():
    post = []
    for subm in reddit.subreddit("catsareliquid").top(limit=100):
        post.append(subm)

    x = 0
    curp = post[random.randint(0, len(post))]
    while curp.over_18:
        x = x + 1
        curp = post[random.randint(0, len(post))]
        if x == 25:
            return "nah, little too risky"
    return curp.url


def getSub(sub):
    try:
        post = []
        subns = sub.replace(" ", "")
        # print(sub)
        for subm in reddit.subreddit(subns).top(limit=100):
            post.append(subm)
        x = 0
        curp = post[random.randint(0, len(post))]
        while curp.over_18:
            x = x + 1
            curp = post[random.randint(0, len(post))]
            if x == 25:
                return "nah, little to risky"
        return curp.url
    except ValueError:
        return "oop, don't look like thats a sub bud"


def getSubNs(sub):
    try:
        post = []
        subns = sub.replace(" ", "")
        # print(sub)
        for subm in reddit.subreddit(subns).top(limit=100):
            post.append(subm)
        curp = post[random.randint(0, len(post))]
        return curp.url
    except ValueError:
        return "oop, don't look like thats a sub bud"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$resp'):
        value = msg.split("resp", 1)[1]
        await message.channel.send(value)

    if message.content.startswith('$red'):
        value = msg.split("red", 1)[1]
        await message.channel.send(getSub(value))

    if message.content.startswith('$redd'):
        value = msg.split("red", 1)[1]
        await message.channel.send(getSubNs(value))

    if message.content.startswith('$cat'):
        await message.channel.send(cat())

# os.getenv('TOKEN')
client.run("ODA0NzQ0Njg2MDAxNDU1MTQ0.YBQy5A.v-QcWoSNXrvZmdprG2p375ie21k")
