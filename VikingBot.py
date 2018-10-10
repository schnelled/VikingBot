# VikingBot.py by Chana
#
# Viking Robotics Society - Discord Chatbot
# =====================
# Discord event-defines for commands

import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

import vrs_utils
import vrs_text
import vrs_ids

vrs_utils.setup() # sets up logging of errors and print statements
bot = commands.Bot(command_prefix='$')
bot.remove_command('help') # remove default help command

print("\n------\n")
print(vrs_text.ASCII_ART)
print("\n------\n")
print("\nDiscord version: {}".format(discord.__version__))
print("\n------\n")

# Bot is ready for Discord
@bot.event
async def on_ready():
    print("Let's build some robots!")
    print("I am running on "+ bot.user.name)
    print("With the ID: "+ bot.user.id)
    print("\n------\n")

# Greet people when they join the server
@bot.event
async def on_member_join(member):
    print("\n{} joined the server!".format(member.name))
    print("First time they joined this server was: {}".format(member.joined_at))

    channel_info = bot.get_channel(vrs_ids.ID_TEXT_GENERAL_INFO)
    await bot.send_message(vrs_ids.ID_TEXT_LOBBY, vrs_text.welcome_text.format(member.mention,channel_info.mention))

#=======================================
# General Commands - anyone can use these commands
#=======================================
# Ping command
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: {} pong! =D".format(ctx.message.author.mention))

# Display commands supported by this bot
@bot.command(pass_context=True)
async def help(ctx):
    await bot.send_message(ctx.message.channel, vrs_utils.help())

# Information about the bot itself
@bot.command(pass_context=True)
async def about(ctx):
    await bot.send_message(ctx.message.channel, vrs_utils.about())

# Provide information about the club
@bot.command(pass_context=True)
async def info(ctx):
    embed = vrs_utils.info_text()
    await bot.send_message(ctx.message.channel, embed=embed)

# Deletes two messages from the channel at a time
#@bot.command(pass_context=True)
#async def clear(ctx):
#    msgs = []
#    async for x in bot.logs_from(ctx.message.channel, limit=2):
#        msgs.append(x)
#    await bot.delete_messages(msgs)


#=======================================
# Admin Commands - Only server Admins can use these commands
#=======================================
# Update Availability poll link
@bot.command(pass_context=True)
async def linkupdate(ctx, poll_name, new_link):
    # Update Availability poll link
    vrs_utils.update_poll_link(poll_name, new_link)
    await bot.send_message(ctx.message.author, "You updated the availability poll link to [{}]({})".format(poll_name,new_link))
    
    # Remove old general info and replace with newer one using new poll link
    msgs = []
    channel_info = bot.get_channel(vrs_ids.ID_TEXT_INFO)
    if channel_info == None:
        print("Couldn't find channel with ID {}".format(vrs_ids.ID_TEXT_INFO))
    else:
        async for x in bot.logs_from(channel_info, limit=2):
            msgs.append(x)
        await bot.delete_messages(msgs) 

        embed = vrs_utils.info_text()
        await bot.send_message(channel_info, "General VRS Info")
        await bot.send_message(channel_info, embed=embed)

bot.run(vrs_ids.TOKEN_TESTBOT)
