#!/usr/bin/python3
def main():
    # Parse through keystone.common.wsgi and return number of failed login attempts.
    loginfail = 0 # Counts the failed login attempts. 

    # Open the file for reading
    keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

    # loop over in the file.

    for line in keystone_file:
        # If this 'fail pattern' appears int he line . . . 
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 #This addes to the counter 'loginfail' at the top of the script. 


    # Print the amount of failed login attempts. 
    print("The number of failed log in attempts is", loginfail)
    keystone_file.close() #closes the open log file. 

main()
