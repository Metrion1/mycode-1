#!/usr/bin/env python3


def main():
    #Parse throught he keystone.common.wsgi and return the number of failed login attempts
    loginfail = 0 #counter for failed login attempts
    
    # Open the file for reading. 
    with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

        # Loop over the file. 
        for line in kfile:
            #if this "fail pattern" appears in the line...
            if "- - - - -] Authorization failed" in line:
                loginfail += 1 #this adds one count to the loginfail counter at the top. 
    
    #This prints the statement "The numeber of failed log in attempts is" with the number counted at the top. 
    print("The number of failed log in attempts is", loginfail)

main()

