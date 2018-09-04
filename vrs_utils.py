# vrs_utils.py by Chana
#
# Viking Robotics Society - Discord Chatbot
# =====================
# Custom functions for Viking Bot

import discord
from discord.ext import commands
import vrs_text

# NEVER share this to the public
token = "DISCORD_BOT_TOKEN"

link_file = 'poll_link.txt'

# Creates Discord embed with club information
def info_text():
    embed = discord.Embed(title="Viking Robotics Society", desription=vrs_text.description, color=0x229954)
    embed.set_footer(text=vrs_text.footer)
    embed.add_field(name="What We Do", value=vrs_text.description2, inline=True)
    embed.add_field(name="Contact", value="Email: " + vrs_text.email, inline=True)
    embed.add_field(name="Website", value=vrs_text.website, inline=True)
    embed.add_field(name="Join Us Formally", value=vrs_text.vrs_join.format(get_poll_link()), inline=True)
    embed.add_field(name="Other Resources",value=vrs_text.resources, inline=True)
    return embed

# Creates commands descriptions for Viking Bot
def help(role):
    text = vrs_text.code_mark + vrs_text.commands_header + vrs_text.help_text
    text = text + vrs_text.commands_admin
    text = text + vrs_text.code_mark
    return text

# Information about the bot
def about():
    text = vrs_text.about.format(vrs_text.bot_repo)
    return text

# Get link for Availaibility poll (stored in local text file)
def get_poll_link():
    with open(link_file) as f:
        read_data = f.read()
    f.close()
    return read_data

# Modify link for Availability poll (stored in local text file)
def update_poll_link(new_link):
    with open(link_file, 'w') as f:
        f.write(new_link)
    f.close()
    
