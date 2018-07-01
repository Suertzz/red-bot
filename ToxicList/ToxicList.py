import discord
from discord.ext import commands

class ToxicList:

    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def toxiclist(self):
        await self.bot.say("Salut bb")


def setup(bot):
    bot.add_cog(ToxicList(bot))
