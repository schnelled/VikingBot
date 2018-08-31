# VikingBot.py by Chana
#
# Viking Robotics Society - Discord Chatbot
# =====================
# Supported Commands
# - $help --- DM list commands for VikingBot
# - $info --- DM information about the Society

import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

import viking_utils
import viking_text

# NEVER share this with the public. This is access to your Discord App/bot
token = viking_utils.token

bot = commands.Bot(command_prefix='$')
bot.remove_command('help') # remove default help command

print("\nDiscord version: {}".format(discord.__version__))
print("\n------\n")

# Bot is ready for Discord
@bot.event
async def on_ready():
    print("Let's bulid some robots!")
    print("I am running on "+ bot.user.name)
    print("With the ID: "+ bot.user.id)
    print("\n------\n")

# When someone joins the server
@bot.event
async def on_member_join(member):
    print("\n{} joined the server".format(member.name))
    print("First time the joined this server is: {}".format(member.joined_at))

    # Future implementation: message upon joining server
    await bot.send_message(member, viking_text.welcome_text)

#=======================================
# General Commands - anyone can use these commands
#=======================================
# Ping command
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong! =D")

# Help command
#@bot.command(pass_context=True)
#async def help(ctx):
    #await bot.send_message(ctx.message.channel, viking_text.commands_text)

# Help command
@bot.command(pass_context=True)
async def help(ctx):
    await bot.send_message(ctx.message.author, viking_utils.help(ctx.message.author.top_role))

# Provide information about the club
@bot.command(pass_context=True)
async def about(ctx):
    embed = viking_utils.info_text()
    await bot.send_message(ctx.message.author, embed=embed)

#=======================================
# Admin Commands - Only server Admins can use these commands
#=======================================
# Update Availability poll link
@bot.command(pass_context=True)
@commands.has_role('Admin')
async def linkupdate(ctx, new_link):
    viking_utils.update_poll_link(new_link)
    await bot.send_message(ctx.message.author, "You updated the availability poll link to {}".format(viking_utils.read_poll_link()))

bot.run(token)
