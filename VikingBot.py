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
    lobby = bot.get_channel(vrs_ids.ID_TEXT_LOBBY)
    await bot.send_message(lobby, vrs_text.welcome_text.format(member.mention,channel_info.mention))

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
    gen_info = vrs_utils.gen_info()
    meetings = vrs_utils.meet_info()
    await bot.send_message(ctx.message.channel, embed=gen_info)
    await bot.send_message(ctx.message.channel, embed=meetings)

#@bot.command(pass_context=True)
#async def test(ctx, param, *args):
    

#=======================================
# Admin Commands - Only server Admins can use these commands
#=======================================
'''
# Add Tinkering Session Time
@bot.command(pass_context=True)
@commands.has_role('Admin')
async def tinker(ctx, param, *args):
    if(len(args)<=0):
        msg = "{} gave param [ {} ] and no arguments".format(ctx.message.author.mention,param)
    else:
        listarg = ""
        for i in args:
            listarg+="{} ".format(i)
        msg = "{} gave param [ {} ] and {} arguments: {}".format(ctx.message.author.mention,param,len(args),listarg)
        
    await bot.send_message(ctx.message.channel,msg)
'''    

# Update Availability poll link
@bot.command(pass_context=True)
@commands.has_role('Admin')
async def linkupdate(ctx, poll_name, new_link):
    # Update Availability poll link
    vrs_utils.update_poll_link(poll_name, new_link)
    await bot.send_message(ctx.message.author, "You updated the availability poll link to {} --> {}".format(poll_name,new_link))
    
    # Remove old general info and replace with newer one using new poll link
    msgs = []
    channel_info = bot.get_channel(vrs_ids.ID_TEXT_GENERAL_INFO)
    if channel_info == None:
        print("Couldn't find channel with ID {}".format(vrs_ids.ID_TEXT_GENERAL_INFO))
    else:
        async for x in bot.logs_from(channel_info, limit=2):
            msgs.append(x)
        await bot.delete_messages(msgs) 

        gen_info = vrs_utils.gen_info()
        meet_info = vrs_utils.meet_info()
        await bot.send_message(channel_info, embed=gen_info)
        await bot.send_message(channel_info, embed=meet_info)

bot.run(vrs_ids.TOKEN_TESTBOT)
