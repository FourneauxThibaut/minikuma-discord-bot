import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
class MiniKuma(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=["mk:", "Mk:", "mK:", "MK:", "mk/", "Mk/", "mK/", "MK/"])

        @self.command(name='join')                                                                      # mk:join
        async def join_channel(ctx):
            channel = ctx.author.voice.channel
            if channel is not None:
                voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
                if voice_client == channel:
                    await ctx.send("I am alredy in this voice channel")
                elif voice_client != channel:
                    leave_channel(ctx)
                    await channel.connect()
                else:
                    await channel.connect()
            else:                
                await ctx.send("You must be in a voice channel first so I can join it.")
        
        @self.command(name='leave')                                                                      # mk:leave
        async def leave_channel(ctx):
            if (ctx.voice_client):                              # If the bot is in a voice channel 
                await ctx.guild.voice_client.disconnect()
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