# discordpybot_template
A template for Discord.py bots, with some utils I like for my bots

## Some handy notes
- This template will be setup with [Python Poetry](https://python-poetry.org/) for package management and include helpful settings and launcher for vscode editing.
- Database config values are not required if a DB is not used.
- Ctrl+F and replace all instances of 'template_bot' (including all filenames and file contents) with the name of your bot.
- This is structured to make use of the Discord.py Commands extension and is setup with Cogs, all Cogs are loaded on startup.
- The default Discord.py help command is left untouched.
- All intents are requested on bot startup, ensure both privilidged intents are checked on the Discord dev portal or alter the requested intents.
- On first startup, a config.ini file is generated in the utils directory. Before you start the bot again, enter the bot token where it is specified.

### To do
Complete documentation, sucks to be you.

### Some handy links
- [Discord.py Docs](https://discordpy.readthedocs.io/en/latest/index.html)
- [Python Poetry](https://python-poetry.org/)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Discord Developer Portal](https://discord.com/developers/applications)

### Bots made with this template
- https://github.com/twohoursonelife/dictator
- https://github.com/voteflux/flux-projects