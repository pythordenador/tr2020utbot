from discord.ext import commands
class example(commands.Cog):
    def __init__(self,bot,pluginList):
        self.bot = bot
        self.plugins = pluginList
        self._last_member = None
    @commands.command()
    async def plugins(self,ctx):
        for i in pluginList:
            await ctx.send("{} - {}".format(i["name"],i["description"]))