import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


class MiniKuma(commands.Bot):

	def __init__(self):
		super().__init__(command_prefix="mk: ")
		
		@self.command(name='test')
        async def custom_command(ctx):
            print("Hello world !")

	async def on_ready(self): 		# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
		guild_count = 0
		
		for guild in self.guilds: 	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
			print(f"- {guild.id} (name: {guild.name})")
			guild_count = guild_count + 1

		print(f"MiniKuma is in {str(guild_count)} guilds.")
	
	
bot = MiniKuma()
bot.run(os.getenv('DISCORD_BOT_TOKEN'))












# bot = discord.Client()

# # EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
# @bot.event
# async def on_ready():
# 	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
# 	guild_count = 0

# 	for guild in bot.guilds:
# 		print(f"- {guild.id} (name: {guild.name})")
# 		guild_count = guild_count + 1

# 	print("MiniKuma is in " + str(guild_count) + " guilds.")

# # EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
# @bot.event
# async def on_message(message):
# 	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
# 	if message.content[:4] == "mk: ":

# 		await message.channel.send('longueur du message: '+str(len(message.content[4:])))

# 		# if message.content[4:] == "join":
# 		# 	channel = message.author.voice.channel
#     	# 	await channel.connect()
# 		# elif message.content[4:] == "leave":
# 		# 	await message.voice_client.disconnect()

# bot.run(os.getenv('DISCORD_BOT_TOKEN'))


