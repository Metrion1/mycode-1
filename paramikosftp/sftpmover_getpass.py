#!/usr/bin/python3
## Try a real world test with getpass

## import Paramiko so we can talk SSH
import paramiko # allows Python to ssh
import os # low level operating system commands
import getpass # we need this to accept passwords
## iterate across the files within directory

def movethemfiles(sftp, loc):
    try:
        for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
            if not os.path.isdir("/home/student/filestocopy/"+x):# filter everything that is NOT a directory
                sftp.put(f"/home/student/filestocopy/{x}", f"{loc}/{x}") # move file to target location
                                                             #asdffasdfasdfasdffile1.txt
                                                             #asdfasdfasdfasdfafile2.txt
    except Exception as err:
        print("Error! That path does not exist:", err)

def main():
    path= input("Where on the remote host do you want these files placed?\n>?")
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender
    
    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass
    
    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    
    movethemfiles(sftp, path)
    
    ## close the connection
    sftp.close() # close the connection
if __name__ == "__main__":
    main()

