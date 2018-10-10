# vrs_text.py by Chana
#
# Viking Robotics Society - Discord Chatbot
# =====================
# String variables needed for Viking Bot


ASCII_ART = " __      ___ _    _                      \n\
 \ \    / (_) |  (_)                      \n\
  \ \  / / _| | ___ _ __   __ _           \n\
   \ \/ / | | |/ / | '_ \ / _` |          \n\
    \  /  | |   <| | | | | (_| |          \n\
     \/   |_|_|\_\_|_| |_|\__, |          \n\
                           __/ |          \n\
  _____       _           |___/           \n\
 |  __ \     | |         | | (_)          \n\
 | |__) |___ | |__   ___ | |_ _  ___ ___  \n\
 |  _  // _ \| '_ \ / _ \| __| |/ __/ __| \n\
 | | \ \ (_) | |_) | (_) | |_| | (__\__ \ \n\
 |_|__\_\___/|_.__/ \___/ \__|_|\___|___/ \n\
  / ____|          (_)    | |             \n\
 | (___   ___   ___ _  ___| |_ _   _      \n\
  \___ \ / _ \ / __| |/ _ \ __| | | |     \n\
  ____) | (_) | (__| |  __/ |_| |_| |     \n\
 |_____/ \___/ \___|_|\___|\__|\__, |     \n\
                                __/ |     \n\
                               |___/      "

#=======================================
# Other text
#=======================================
bot_version = "2018-10-09"

# First bracket should be a mention for the joining user. Second bracket should be text channel mention.
welcome_text = "Welcome {} to the Discord Server for Viking Robotics Society at Portland State University\n\
Our group welcomes people of the community and students of any major to join us in learning robotics.\n\
\n\
Please change your nickname to your real name so we can identify people on the server.\n\
If we haven't seen you at our meetings yet, be sure to stop by so we know who you are.\
See our {} channel for more information, or ask for help in this channel and we'll get back to you."

about = "(Version {}) --- I was made by Chana for the Viking Robotics Society at Portland State University. You can find my source code at https://github.com/pdx-robotics/VikingBot"

#=======================================
# Discord Embed Text - About the Society
#=======================================
title = "Viking Robotics Society"
footer = "Viking Robotics Society - Portland State University"
description = "We are the Robotics Club at Portland State, open for the community to join us"
description2 = "Teach robotics and engineering industry skills through projects"
email = "*robotics@pdx.edu*"
website = "http://robotics.ece.pdx.edu"
vrs_join = "Here's how you can join us formally:\n\
            (1) Let us know more about you by filling out the [New Membership Form](https://goo.gl/forms/AUXMLsyf38IpIoJW2)\n\
            (2) Join us on [Orgsync](https://orgsync.com/85238/chapter)\n\
            (3) Participate in our [Weekly Availability Poll for {}]({}) so we can schedule meetings around everyone's schedule.\n"

vrs_location = "Portland State University - Intelligent Robotics Lab (FAB70-09)"

resources = "Viking Robotics [Github](https://github.com/pdx-robotics)\n\
            Website for our [3D Printer](http://roboprint.cecs.pdx.edu/)"


#=======================================
# Help Command Text
#=======================================
commands_header = "========__Viking Bot Commands__========\n"

code_mark = "```"

help_text = "$help  ==> Shows this message\n\
$about ==> Get information about Viking Bot\n\
$info  ==> Get information about Viking Robotics Society\n"

commands_admin = "\n========__Admin Commands__========\n\
$linkupdate \"link name\" <new_link> \n==> Update Availability Poll link stored by Viking Bot. Link must start with http://\n"
