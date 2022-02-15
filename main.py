import discord
import os
# load our local env so we dont have the token in public
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL

load_dotenv()

class MiniKuma(commands.Bot):
    is_connected = False

    def __init__(self):
        super().__init__(command_prefix=[".mk ",";mk ",">.mk ", ".Mk ",";Mk ",">.Mk ", ".mK ",";mK ",">.mK ", ".MK ",";MK ",">.MK ",], help_command=None)

        @self.command(name='help')                                                                      # mk:join
        async def send_help(ctx):
            await ctx.send("to make the bot join the vocal type:  .mk join")
            await ctx.send("to make the bot leave type: .mk leave")

        @self.command(name='join')                                                                      # mk:join
        async def join_channel(ctx):

            if ctx.author.voice is None:
                await ctx.send("You must be in a voice channel first so I can join it.")
            else:
                channel = ctx.author.voice.channel
                if self.is_connected == False:
                    await channel.connect()
                    self.is_connected = True
                    print(f"connected to {channel} in {ctx.guild}")
                else:
                    await ctx.guild.voice_client.disconnect()
                    await channel.connect()
                    print(f"MiniKuma moved to {channel} in {ctx.guild}")
  
        @self.command(name='leave')                                                                      # mk:leave
        async def leave_channel(ctx):
            if (ctx.voice_client):                              # If the bot is in a voice channel 
                await ctx.guild.voice_client.disconnect()
                self.is_connected = False
            else:                                               # But if it isn't
                await ctx.send("I'm not in a voice channel, use the join command to make me join")

    async def on_ready(self):
        # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
        guild_count = 0

        for guild in bot.guilds:
            print(f"- {guild.id} (name: {guild.name})")
            guild_count = guild_count + 1

        print("MiniKuma is in " + str(guild_count) + " guilds.")

bot = MiniKuma()
bot.run(os.getenv('DISCORD_BOT_TOKEN'))