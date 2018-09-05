# vrs_utils.py by Chana
#
# Viking Robotics Society - Discord Chatbot
# =====================
# Custom functions for Viking Bot

import os, sys, datetime
import discord
from discord.ext import commands
import vrs_text

dir_path  = os.path.dirname(os.path.realpath(__file__))
log_dir  = dir_path + "/log/"
link_file = dir_path + "/poll_link.txt"

# Set up console outputs to also save to log file
def setup():
    # Make directory for logs if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    sys.stdout = Logger()


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
def help():
    text = vrs_text.code_mark + vrs_text.commands_header + vrs_text.help_text
    text = text + vrs_text.commands_admin
    text = text + vrs_text.code_mark
    return text

# Information about the bot
def about():
    text = vrs_text.about.format(vrs_text.bot_version)
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

# Decorate stdout to also print to a log file
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open(log_dir + datetime.datetime.now().strftime("discordlog-%Y%m%d-%H%M.txt"), "a")
 
    def write(self, message):
        self.terminal.write(message)
        self.log.write(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M   ")+ message)
 
    def flush(self):
        pass

