
class example(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None
    @commands.command()
    async def exampleCommand(self,ctx):
        await ctx.send("Hello")