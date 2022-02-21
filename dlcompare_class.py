"""
    function add_game
    example: #.mk add_game "binding of isaac" 5
"""
@self.command(name='add_game')
async def add_game(ctx, name, price):
    if db.contains(q.author == ctx.author.name):
        game = db.get((q.game == name) & (q.price != price))
        if game != None:
            if q.price != price:
                db.update({'price': price}, q.game == name)
                await ctx.send(f"{name} price is updated !")
        else:
                await ctx.send(f"{name} is already in your list")
    else:
        db.insert({ "author" : ctx.author.name, "game" : name, "price" : price })
        print(f"{ctx.author.name} {name} {price} created")
        
"""
    function get_game_list
    example: #.mk get_game_list
"""
@self.command(name='get_game_list')
async def get_game_list(ctx):
    user_list = db.search(q.author == ctx.author.name)
    print(user_list)
    
    
    # for game in self.game_list:
    #     if ctx.author.name == game['author']:
    #         user_game.append(game)
    # if len(user_game) > 0:
    #     await ctx.send(f"{ctx.author.name} have {len(user_game)} in the list:")
    #     for message in user_game:
    #         await ctx.send( message["game"] + " : " + message["price"] + "€")
    # else:
    #     await ctx.send("you need to add a game first in the list using the add_game command")