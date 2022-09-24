from discord.ext.commands import Bot
from discord import Intents
from os import chdir, listdir, getenv
from os.path import dirname, abspath
from asyncio import run

# entry point of program
async def main():
    client = Bot(command_prefix = '!', intents = Intents.default())

    # loads cogs
    chdir(dirname(abspath(__file__)))
    for filename in listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

    await client.start(getenv('ACMBOT_API_KEY'))

if(__name__ == "__main__"):
    run(main())
    