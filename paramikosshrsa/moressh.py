#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Learning about Python SSH"""
import json
import paramiko

un= json.loads(open("un.txt").read().strip("\n"))
ip= json.loads(open("ip.txt").read().strip("\n"))


# using with/as for opening files means that all the code involving that file has to be indented underneath it
# since you're opening them at the beginning of the script, I switched them around so
# you can use the un and ip vars later in the script

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
    #credz = un[0,1,2] and ip[0,1,2]
    #print(credz)
    #         {"un": "bender", "ip": "10.10.2.3"}, 
    #        {"un": "zoidberg", "ip": "10.10.2.5"}, 
    #         {"un": "fry", "ip": "10.10.2.4"}
    #        ]

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
    # let me know if you need any help!
    # loop across the collection credz

    counter = 0

    for cred in un:
        ## create a session object
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display our connections
        #print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

        ## make a connection
                                    # grab ip[0] tjem ip[1] etc.
        sshsession.connect(hostname=ip[counter], username=un[counter], pkey=mykey)
                                                            # grab un[0], un[1], etc.

        ## touch the file goodnews.everyone in each user's home directory
        sshsession.exec_command("touch /home/" + un[counter] + "/goodnews.everyone")

        ## list the contents of each home directory
        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + un[counter])

        ## display output
        print(sessout.read().decode('utf-8'))

        ## close/cleanup SSH connection
        sshsession.close()

        counter += 1
    print("Thanks for looping with Alta3!")

main()

