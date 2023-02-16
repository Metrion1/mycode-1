#!/usr/bin/env python3

# Parse through the keystone.common.wsgi and return the number of failed login attempts.
def main():
    loginfail = 0 # This will act as the counter for failed attempts

    # Open the file for reading. 
    keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

    #turn the file into a list of lines in the system memory. 

    keystone_file_lines=keystone_file.readlines()

    # Loop over the list of lines. 
    for line in keystone_file_lines:
        # If this 'fail pattern' appears int he line...
        if"- - - - -] Authorization failed" in line:
            loginfail += 1 #This is the same as loginfail = loginfail + 1

    print("The number of failed log in attempts is", loginfail)
    keystone_file.close() # This closes the open file. 

main()
