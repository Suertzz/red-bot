import discord
from discord.ext import commands

class ToxicList:

    def __init__(self, bot):
        self.bot = bot

    def is_command(self, msg):
        if callable(self.bot.command_prefix):
            prefixes = self.bot.command_prefix(self.bot, msg)
        else:
            prefixes = self.bot.command_prefix
        for p in prefixes:
            if msg.content.startswith(p):
                return True
        return False

    async def msg_listener(self, message):
        printf("test2")
        if message.author == self.bot.user:
            print("test")
            return
        else:
            await self.bot.add_reaction(message, "\U0001f602")
def setup(bot):
    bot.add_cog(ToxicList(bot))
