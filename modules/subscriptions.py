import discord
from discord.ext import commands
from utils import checks
import asyncio

class Subscriptions():
    def __init__(self, bot):
        self.bot = bot

        # Message delete delay
        self.delay = 10

        # Options for different gams
        # ID first entry
        # Pretty, correctly spelt name as last
        # Various ways of inputting in the middle
        self.csgo = ['195471958534651904','csgo','counter strike','#csgo']
        self.overwatch = ['195471986808455168','ow','overwatch','#overwatch']
        self.lol = ['195472348420243456','lol','league','#lol']
        self.paragon = ['195472489642590208','paragon','#paragon']
        self.pokemon = ['195472571817263105','pkmn','pokemon','#pokemon']
        self.rpg = ['195472607900860416','rpg','#rpg']
        self.smash = ['195472623487025154','smash','#smash']
        self.dank = ['195473816850268160','dank','#dank']
        self.music = ['195473785447514112','music','#music']

        self.allOptions = [self.csgo, self.overwatch, self.lol, self.paragon, self.pokemon, self.rpg, self.smash, self.dank, self.music]

        # Creates a string of availible games to Subscribe to
        listStr = ""
        for x in self.allOptions:
            listStr = listStr + ("\n" + x[-1])

        # Makes that string look pretty
        self.roles = "Channels available to subscribe to: %s " % listStr

    # Joins the user to a role
    @checks.is_server()
    @commands.command(hidden=True,pass_context=True)
    async def join(self, ctx, *, channel: str = None):
        """Adds you to a regions role"""

        # Get's the server and user from message
        server = ctx.message.server
        member = ctx.message.author

        # Sets the region in invalid
        valid = False

        # Defines whether this command is adding or
        # removing role
        self.sub = True

        if channel is None:
            output = await self.bot.say(self.roles)
            await asyncio.sleep(self.delay)
            await self.bot.delete_message(ctx.message)
            await self.bot.delete_message(output)
            return

        # Checks if the region is an available option
        for options in self.allOptions:
            if channel.lower() in options:
                # Gets the role object from Discord
                role = discord.utils.get(server.roles, id=options[0])
                # Adds the role
                await self.bot.add_roles(member, role)
                # Outputs conformation to user
                output = await self.bot.say("%s joined %s" % (member.mention, options[-1]))
                await asyncio.sleep(self.delay)
                await self.bot.delete_message(ctx.message)
                await self.bot.delete_message(output)
                # Outputs to console
                print("%s joined %s" % (member.name, options[-1]))
                #Ensures valid is True
                valid = True
                break

        # If region is not valid, output available roles
        if not valid:
            output = await self.bot.say(self.roles)
            await asyncio.sleep(self.delay)
            await self.bot.delete_message(ctx.message)
            await self.bot.delete_message(output)

    @checks.is_server()
    @commands.command(hidden=True,pass_context=True)
    async def leave(self, ctx, *, channel: str):
        """Removes you from a regions role"""

        # Get's the server and user from message
        server = ctx.message.server
        member = ctx.message.author

        # Sets the region in invalid
        valid = False

        # Defines whether this command is adding or
        # removing role
        self.sub = True

        # Checks if the region is an available option
        for options in self.allOptions:
            if channel.lower() in options:
                # Gets the role object from Discord
                role = discord.utils.get(server.roles, id=options[0])
                # Removes the role
                await self.bot.remove_roles(member, role)
                # Outputs conformation to user
                output = await self.bot.say("%s left %s" % (member.mention, options[-1]))
                await asyncio.sleep(self.delay)
                await self.bot.delete_message(ctx.message)
                await self.bot.delete_message(output)
                # Outputs to console
                print("%s left %s" % (member.name, options[-1]))
                # Ensures valid is True
                valid = True
                break

        # If region is not valid, output available roles
        if not valid:
            output = await self.bot.say(self.roles)
            await asyncio.sleep(self.delay)
            await self.bot.delete_message(ctx.message)
            await self.bot.delete_message(output)

def setup(bot):
    bot.add_cog(Subscriptions(bot))
