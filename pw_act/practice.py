#!usr/bin/python3

import getpass

# the getpass function from the getpass module is 
# like a "private" version of input()

passwoid= getpass.getpass()

#Require password to be 8 or more characters
#and start with "P" end with "3" and not include "butts".
if len(passwoid) >= 8 and passwoid.startswith("P") and passwoid.endswith("3") and "butts" not in passwoid:
    print("All requirements met!")

else:
    print("You fail!!!")

print(passwoid)

