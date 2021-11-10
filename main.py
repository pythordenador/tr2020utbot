from discord.ext import commands
import discord
import toml
pluginList = []


bot = commands.bot(command_prefix="n!")

for i in os.listdir(path='./plugins'):
    with open("./plugins/{}/plugin.toml".format(i),"r") as rile:
        tom = toml.load(rile)
        