from discord.ext import commands


class Ping(commands.Cog):

    def __init__(self, template_bot):
        self.template_bot = template_bot

    @commands.command(brief='Check the bot\'s latency.', help='Check the bot\'s latency or whether it\'s responding at all.')
    async def ping(self, ctx):
        await ctx.send(f'Pong! That took me {round(self.template_bot.latency * 1000)}ms!')


def setup(template_bot):
    template_bot.add_cog(Ping(template_bot))