from discord.ext import commands
import discord

# Checks if the message author's id matches the owner
def is_owner_check(message):
    return message.author.id == '95953002774413312'

# Runs the commands module check thing
def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))

# Checks if the message author's roles
def is_admin_check(message, check):
    author = message.author
    role = discord.utils.find(check, author.roles)
    return role is not None

# Checks whether the message author has admin role or is
def is_admin():
    def predicate(ctx):
        if is_owner_check(ctx.message):
            return True
        return is_admin_check(ctx.message, lambda r: r.id == '190031997933060096')
    return commands.check(predicate)

# Returns T/F to whether the server ID is the ESL Dota 2 Server ID
def is_server_check(message):
    return message.server.id == '164175245677297664'

# Checks whether server ID == ESL Dota 2 Server ID
def is_server():
    return commands.check(lambda ctx: is_server_check(ctx.message))

# Checks if the message author's roles
def is_dunce_check(message, check):
    author = message.author
    role = discord.utils.find(check, author.roles)
    return role is not None

# Checks whether the message author has admin role or is
def is_dunce():
    def predicate(ctx):
        return is_dunce_check(ctx.message, lambda r: r.id == '171103388560392193')
    return commands.check(predicate)