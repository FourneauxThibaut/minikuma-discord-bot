from email import message
import discord
import os
# load our local env so we dont have the token in public
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL

from tinydb import TinyDB, Query, where
db = TinyDB('db.json')
q = Query()

load_dotenv()
class MiniKuma(commands.Bot):
    is_connected = False
    current_channel = ""
    game_list = []

    def __init__(self):
        super().__init__(command_prefix=[".mk ",";mk ",">.mk ", ".Mk ",";Mk ",">.Mk ", ".mK ",";mK ",">.mK ", ".MK ",";MK ",">.MK ",])

        import dlcompare_class
        
        import voice_class
        
        """
            function delete_messages
            example: #.mk delete 5
        """
        @self.command(name='delete')                                                                   
        async def delete_messages(ctx, number_of_messages: int):
            messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

            for each_message in messages:
                await each_message.delete()
            print(f"{number_of_messages} message erased")           
                
    async def on_ready(self):
        # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
        guild_count = 0

        for guild in bot.guilds:
            print(f"- {guild.id} (name: {guild.name})")
            guild_count = guild_count + 1

        print("MiniKuma is in " + str(guild_count) + " guilds.")

bot = MiniKuma()
bot.run(os.getenv('DISCORD_BOT_TOKEN'))