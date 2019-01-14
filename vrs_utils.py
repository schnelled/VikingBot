# vrs_utils.py by Chana
#
# Viking Robotics Society - Discord Chatbot
# =====================
# Custom functions for Viking Bot

import os, sys, datetime, logging
import discord
from discord.ext import commands
import vrs_text

dir_path   = os.path.dirname(os.path.realpath(__file__))
log_dir    = dir_path + "/log/"
link_file  = dir_path + "/poll_link.txt" # file with link to availability poll
tinkerfile = dir_path + "/tinker_times.txt" # file with tinkering session times

# Set up console outputs to also save to log file
def setup():
    # Make directory for logs if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Configure the basic logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
        filename=log_path + datetime.datetime.now().strftime("discordlog-%Y%m%d-%H%M.log"),
        filemode='a'
    )

    # Write standard output to the log file
    sl = StreamToLogger(logging.getLogger('STDOUT'), logging.INFO)
    sys.stdout = sl

    # Write standard error to the log file
    sl = StreamToLogger(logging.getLogger('STDERR'), logging.ERROR)
    sys.stderr = sl


# Creates Discord embed with club information
def gen_info():
    embed = discord.Embed(title="__|---     VRS General Information     ---|__", desription=vrs_text.description, color=0x229954)
    embed.set_footer(text=vrs_text.footer)
    embed.add_field(name="What We Do", value=vrs_text.description2, inline=True)
    embed.add_field(name="Contact", value="Email: " + vrs_text.email, inline=True)
    embed.add_field(name="Website", value=vrs_text.website, inline=True)
    
    data = get_poll_link()
    embed.add_field(name="Join Us Formally", value=vrs_text.vrs_join.format(data[0],data[1]), inline=True)
    embed.add_field(name="Other Resources",value=vrs_text.resources+"\n", inline=True)
    return embed

def meet_info():
    embed = discord.Embed(title="__|---     Meetings     ---|__",description=vrs_text.meet_desc, color=0x229954)
    embed.set_footer(text=vrs_text.footer)
    embed.add_field(name="Monthly General Meetings",value="First Friday of every the month starting at 6pm\n-----", inline=True)

    tinkertimes = ""
    for x in sessions.sessions:
        tinkertimes += "{} from {} to {}\n".format(n_to_day(x.weekday), x.starttime, x.endtime)
    tinkertimes += "\n*Last Updated: {}*".format(sessions.lastupdated)
    embed.add_field(name="{} Weekly Tinkering Sessions".format(sessions.name),value=tinkertimes, inline=False)
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
    data = read_data.split("\n")
    return data

# Modify link for Availability poll (stored in local text file)
def update_poll_link(name, new_link):
    with open(link_file, 'w') as f:
        f.write("{}\n{}".format(name, new_link))
    f.close()
    print("Poll link has been updated to {} --> {}".format(name,new_link))

# Convert number to weekday
# 0=Sunday, 1=Monday, ... 6=Saturday
def n_to_day(n):
    if n=='0':
        return "Sunday"
    elif n=='1':
        return "Monday"
    elif n=='2':
        return "Tuesday"
    elif n=='3':
        return "Wednesday"
    elif n=='4':
        return "Thursday"
    elif n=='5':
        return "Friday"
    else:
        return "Saturday"


# Decorate stdout to also print to a log file
class StreamToLogger(object):
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''
 
    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())
 
    def flush(self):
        pass

# Class to organize session times
class Session(object):
    def __init__(self):
        self.weekday = ''
        self.starttime = ''
        self.endtime = ''

# Class to organize event times
class Event(object):
    def __init__(self):
        with open(tinkerfile, 'r') as f:
            read_data = f.read()
        f.close()

        self.sessions = []
        self.name, times, self.lastupdated = read_data.split("\n")
        times = times.split("|")
        for i in range(0,len(times)):
            data = times[i].split(",")
            new_session = Session()
            new_session.weekday = data[0]
            new_session.starttime = data[1]
            new_session.endtime = data[2]
            self.sessions.append(new_session)
    
    def add(self, day, start, end):
        if (day<'0') | (day>'6'):
            return -1 # Day is out of bounds
        elif (start<"00:00") | (start>"23:99"):
            return -2 # Start time is out of bounds
        elif (end<"00:00") | (end>"23:99"):
            return -3 # End time is out of bounds
        
        new_session = Session()
        new_session.weekday = day
        new_session.starttime = start
        new_session.endtime = end

        for i in range(0,len(self.sessions)):
            if new_session.weekday < self.sessions[i].weekday:
                self.sessions.insert(i, new_session)
                break
            elif new_session.weekday == self.sessions[i].weekday:
                if new_session.starttime < self.sessions[i].starttime:
                    self.sessions.insert(i, new_session)
                    break
                elif new_session.starttime == self.sessions[i].starttime:
                    return -4 # Conflicting new time
                else:
                    pass
            else: # Move on to next item
                if(i==(len(self.sessions)-1)):
                    self.sessions.append(new_session)
                    break
                else:
                    pass
        self.update()
        return 0

    def remove(self, index):
        if (index<0) | (index>(len(self.sessions)-1)):
            return -1 # Out of index bounds. 
        
        del self.sessions[index]
        self.update()
        return 0

    def display(self):
        print("Term: {}\n".format(self.name))
        for session in self.sessions:
            print("{} from {} to {}\n".format(session.weekday,session.starttime,session.endtime))
        print("This information was last updated: {}\n".format(self.lastupdated))

    def update(self):
        self.lastupdated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def update_file(self):
        with open(tinkerfile,'w') as f:
            f.write("{}\n".format(self.name))
            
            for i in range(0,len(self.sessions)):
                if i==(len(self.sessions)-1):
                    print("Writing last session time\n")
                    f.write("{},{},{}\n".format(self.sessions[i].weekday,self.sessions[i].starttime,self.sessions[i].endtime))
                else:    
                    f.write("{},{},{}|".format(self.sessions[i].weekday,self.sessions[i].starttime,self.sessions[i].endtime))
            f.write(self.lastupdated)
        f.close()

sessions = Event()
