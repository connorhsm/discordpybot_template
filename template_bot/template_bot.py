import os
from discord.ext import commands
import utils.config_manager as config
import discord


print(config.check_config())

intents = discord.Intents.all()

template_bot = commands.Bot(command_prefix=config.read('bot_prefix'), case_insensitive=True, intents=intents)

@template_bot.event
async def on_ready():
    print('The template_bot has risen!')

# Loading of all cog files in the cogs directory
for filename in os.listdir('template_bot/cogs'):
    if filename.endswith('.py'):
        template_bot.load_extension(f'cogs.{filename[:-3]}')


template_bot.run(config.read('bot_token'))