# viking_utils.py by Chana
#
# Viking Robotics Society - Discord Chatbot
# =====================
# Custom functions for Viking Bot

import discord
from discord.ext import commands
import viking_text

# NEVER share this to the public
token = "DISCORD_BOT_TOKEN"

link_file = 'poll_link.txt'

# Creates Discord embed with club information
def info_text():
    embed = discord.Embed(title="Viking Robotics Society", desription=viking_text.description, color=0x229954)
    embed.set_footer(text=viking_text.footer)
    embed.add_field(name="What We Do", value=viking_text.description2, inline=True)
    embed.add_field(name="Contact", value="Email: " + viking_text.email, inline=True)
    embed.add_field(name="Website", value=viking_text.website, inline=True)
    embed.add_field(name="Join Us Formally", value=viking_text.vrs_join.format(get_poll_link()), inline=True)
    embed.add_field(name="Other Resources",value=viking_text.resources, inline=True)
    return embed

# Creates commands descriptions for Viking Bot
def help(role):
    text = viking_text.code_mark + viking_text.commands_header + viking_text.help_text
    text = text + viking_text.commands_admin
    text = text + viking_text.code_mark
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

def read_poll_link():
    with open(link_file) as f:
        read_data = f.read()
    f.close()
    return read_data
