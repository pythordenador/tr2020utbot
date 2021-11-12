from discord.ext import commands
import discord
import os
import toml
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("token")
pluginList = []


bot = commands.Bot(command_prefix="n!")

for i in os.listdir(path='./plugins'):
    with open("./plugins/{}/plugin.toml".format(i),"r") as rile:
        tom = toml.load(rile)
        print("Found {}".format(tom["description"]["name"]))
        try:
            to_append = {
                "name": tom["description"]["name"],
                "id": tom["description"]["id"],
                "author": tom["description"]["author"],
                "description": tom["description"]["description"],
                "version": tom["advanced"]["version"],
                "versionID": tom["advanced"]["versionID"],
                "class": tom["init"]["className"],
                "folder": i,
                "arguments": tom["init"]["args"]
            }
        except KeyError as e:
            print("Parse error in file ./plugins/{}/plugin.toml".format("plugin"))
            to_append = "N"
        if not to_append == "N":
            pluginList.append(to_append)

for i in pluginList:
    exec("import plugins.{}".format(i["folder"]))
    exec("bot.add_cog({}({})".format(i["class"],i["arguments"]))

bot.run(token)
