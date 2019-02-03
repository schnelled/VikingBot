# Title: vrs_classes.py
# Author: Aaron Chan (Chana030102) & Dustin Schnelle (schnelled)
# Date: 1/24/2019
#
# Classes for the Viking Robotics Society discord bot
# ==============================================================================
# Classes:
#           -> Session(object): Session objects represent individual meeting
#                               times during the current term. It stores the
#                               individual sessions meeting day, start time,
#                               and end times.
#           -> Event(object):   The Event object is a method of managing all of
#                               the sessions during the current term.

import datetime, os

#-------------------------------------------------------------------------------
# Class:        Session
# Methods:
#               -> __init__ (initialize)
# Variables:
#               -> weekday: Day of the week which the session is occuring
#               -> starttime: Start time of the session
#               -> endtime: End time of the session
# Description:  Class to organize session times.
#-------------------------------------------------------------------------------
class Session(object):
    #---------------------------------------------------------------------------
    # Function:     initialize
    # Input:        none
    # Output:       none
    # Definition:   Initialize the Session class object.
    #---------------------------------------------------------------------------
    def __init__(self):
        # Initialize the day of the week, start time, and end time
        self.weekday = ''
        self.starttime = ''
        self.endtime = ''

#-------------------------------------------------------------------------------
# Class:        Event
# Methods:
#               -> __init__ (initialize)
#               -> add
#               -> remove
#               -> display
#               -> update
# Variables:
#               -> file:
#               -> sessions:
#               -> term:
#               -> lastupdated:
# Description:  Class to add, remove, and modify events during a current term.
#               The event class is an array of independent session classes.
#-------------------------------------------------------------------------------
class Event(object):
    #---------------------------------------------------------------------------
    # Function:     initialize
    # Input:        -> tinkerfile - file where the tinker time information is
    #                   stored.
    # Output:       none
    # Description:  Read the tinkering times from the tinker_times.txt file.
    #               Initialize the sessions array for storing session information.
    #               Initialize the information (weekday, starttime, & endtime)
    #               for the sessions.
    #---------------------------------------------------------------------------
    def __init__(self, tinkerfile):
        # Initialize the tinkering session file
        self.file = tinkerfile

        # Open the file (read only) with tinker time information
        with open(self.file, 'r') as f:
            # Read the tinker time information
            read_data = f.read()
        # Close the file with tinker time information
        f.close()

        # Initialize an empty sessions array to store Session objects
        self.sessions = []
        # Use the read tinker time information to initialize the term, time, and
        # last updated date of the session
        self.term, times, self.lastupdated, unused = read_data.split('\n')
        # Spilt the times information for each session during the term
        times = times.split("|")

        # Loop for the number of sessions (tinker times)
        for i in range(0,len(times)):
            # Spilt the information for the session time
            data = times[i].split(",")
            # Create new instance of a Session object
            new_session = Session()
            # Initialize the weekday, starttime and endtime for the session
            new_session.weekday = data[0]
            new_session.starttime = data[1]
            new_session.endtime = data[2]
            # Append the current session into the sessions array
            self.sessions.append(new_session)

    #---------------------------------------------------------------------------
    # Function:     add
    # Input:        day - String representing the day of the week
    #               start - Starting time of the tinkering session
    #               end - Ending time of the tinkering session
    # Output:       none
    # Description:  Add the new tinkering session into the event class.
    #---------------------------------------------------------------------------
    def add(self, day, start, end):
        # Open the file (read only) with tinker time information
        with open(self.file, 'r') as f:
            # Read the tinker time information
            read_data = f.read()
        # Close the tinker time text file
        f.close()

        # Information to be added to the file
        add = '|' + day + ',' + start + ',' + end
        # Use the read tinker time information to initialize the term, time, and
        # last updated date of the session
        self.term, times, self.lastupdated, unused = read_data.split('\n')
        # Spilt the times information for each session during the term
        times = times.split("|")

        # Loop for the number of sessions (tinker times)
        for i in range(0,len(times)):
            # Spilt the information for the session time
            data = times[i].split(",")
            # Check if the new date is less than the current date in the times array
            if(int(data[0]) <= int(day)):
                print("Less than")
                # Check if new date is equal to current date in times array
                if(int(data[0]) == int(day)):
                    print("Equal")
            #Otherwise the new date is greater then the current date in the time array
            else:
                print("Greater than")

        # Update the last modification date and time
        self.lastupdated = self.update()

        # Create new instance of a Session object
        new_session = Session()
        # Initialize the weekday, starttime and endtime for the session
        new_session.weekday = day
        new_session.starttime = start
        new_session.endtime = end
        # Append the current session into the sessions array
        self.sessions.append(new_session)

        # Open the tinker time text file for writing
        with open(self.file, 'w+') as f:
            # Write to the tinker time text file
            f.write("{}\n{}\n{}\n".format(self.term, times, self.lastupdated))
        # Close the tinker time text file
        f.close()

    #---------------------------------------------------------------------------
    # Function:     remove
    # Input:        day - The day of the session to be removed
    #               start - The start time of the session to be removed
    #               end - The end time of the session to be removed
    # Output:       none
    # Description:  Removes a current tinkering session from the event class.
    #---------------------------------------------------------------------------
    def remove(self, day, start, end):
        # Session time to be removed
        toRemove = day + ',' + start + ',' + end

        # Open the file (read only) with tinker time information
        with open(self.file, 'r') as f:
            # Read the tinker time information
            read_data = f.read()
        # Close the tinker time text file
        f.close()

        # Use the read tinker time information to initialize the term, time, and
        # last updated date of the session
        self.term, times, self.lastupdated, unused = read_data.split('\n')
        # Spilt the times information for each session during the term
        times = times.split("|")

        # Initialize the index
        i = 0
        # Loop for the number of sessions (tinker times) in the list of strings
        while i < len(times):
            # Check for the matching session string to be removed
            if times[i] == toRemove:
                # Display information about the deleted section
                print("Deleting {},{},{} from tinker_time.txt".format(day, start, end))
                # Remove the specified session from the list of session strings
                del times[i]
            else:
                # Increment the index
                i += 1

        # Loop for the number of sessions (tinker times) in the list of session objects
        for i, o in enumerate(self.sessions):
            # Check for matching session object to be removed
            if o.weekday == day and o.starttime == start and o.endtime == end:
                # Remove the specified session from the list of session objects
                del self.sessions[i]
                break

        # Transform the list of times into a times string
        times = '|'.join(times)

        # Open the tinker time text file for writing
        with open(self.file, 'w+') as f:
            # Write to the tinker time text file
            f.write("{}\n{}\n{}\n".format(self.term, times, self.lastupdated))
        # Close the tinker time text file
        f.close()

    #---------------------------------------------------------------------------
    # Function:     display
    # Input:
    # Output:
    # Description:
    #---------------------------------------------------------------------------
    def display(self):
        print("Not implemented yet!!!")

    #---------------------------------------------------------------------------
    # Function:     update_file
    # Input:        none
    # Output:       String with current date and time
    # Description:  Produce an updated date and time string to be written to the
    #               file.
    #---------------------------------------------------------------------------
    def update(self):
        # Update the last modification date and time
        year = datetime.datetime.today().year
        month = datetime.datetime.today().month
        date = datetime.datetime.today().day
        hour = datetime.datetime.now().hour
        min = datetime.datetime.now().minute
        return str(year) + '-' + str(month) + '-' + str(date) + ' ' + str(hour) + ':' + str(min)

#-------------------------------------------------------------------------------
# Function:     testClasses
# Input:        none
# Output:       none
# Description:  Test the functionality of the classes, so new methods can be
#               fully tested before being added to the VRS Discord server.
#-------------------------------------------------------------------------------
def testClasses():
    # Obtain current working directory
    testDir = os.getcwd()
    # Modify the directory
    testDir = testDir.replace("Include", "Test/tinker_times.txt")

    # Initialize instance for testings events
    testEvent = Event(testDir)

    # Exaustive test of the add/remove feature without time conflicts
    # Remove Sunday(0) session
    testEvent.remove('0','12:00','16:00')
    # Add Sunday(0) session
    # Remove Monday(1) session
    testEvent.remove('1','12:00','16:00')
    # Add Monday(1) session
    # Remove Tuesday(2) session
    testEvent.remove('2','12:00','16:00')
    # Add Tuesday(2) session
    # Remove Wednesday(3) session
    testEvent.remove('3','12:00','16:00')
    # Add Wednesday(3) session
    # Remove Thursday(4) session
    testEvent.remove('4','12:00','16:00')
    # Add Thursday(4) session
    # Remove Friday(5) session
    testEvent.remove('5','12:00','16:00')
    # Add Friday(5) session
    # Remove Saturday(6) session
    testEvent.remove('6','12:00','16:00')
    # Add Saturday(6) session

# If classes is run as a script then run the test case
if __name__ == '__main__':
    testClasses()
