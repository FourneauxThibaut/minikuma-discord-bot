"""
    function join_channel
    example: #.mk join
"""
@self.command(name='join')                                                                      
async def join_channel(ctx):
    
    if ctx.author.voice is None:    # if author is connected in a voice channel
        await ctx.send("You must be in a voice channel first so I can join it.")
    else:
        channel = ctx.author.voice.channel
        if self.is_connected == False:  # if bot ins't connected in a voice channel
            await channel.connect()
            self.is_connected = True
            self.current_channel = channel
            print(f"connected to {channel} in {ctx.guild}")
        else:
            await ctx.guild.voice_client.disconnect()
            await channel.connect()
            self.current_channel = channel
            print(f"MiniKuma moved to {channel} in {ctx.guild}")
            
"""
    function leave_channel
    example: #.mk leave
"""
@self.command(name='leave')
async def leave_channel(ctx):
    if (ctx.voice_client):  # if bot is connected in a voice channel                           
        await ctx.guild.voice_client.disconnect()
        self.is_connected = False
    else:                 
        await ctx.send("I'm not in a voice channel, use the join command to make me join")
                
"""
    function self_mute
    example: #.mk stfu
"""
@self.command(name='stfu')
async def self_mute(ctx, user = 942054181303369750, reason = None):
    if bot.is_connected is True:
        await mute(ctx, ctx.message.server.get_member(user), reason)
    else:
        await ctx.send("I need to be in a voice channel to be muted")