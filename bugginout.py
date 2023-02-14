#!/usr/bin/python3
#"""Just a lil' warmup!""

def main():
    #Prompt the user with two questions.
    name = input("What is your name?\n>")
    num = int(input("Pick a number between 1 and 3\n>"))-1
    
    #Pick an adjective based on user input.
    adj_list = ["stupendous","splendiferous","magnificent"]
    adj = adj_list[num]
    
    print("Hello " + name + "!" + " Have a " + adj + " Valentine's day!")
main()


# FINAL PART OF CHALLENGE:
# USE THE name AND adj VARIABLES TO PRINT THE FOLLOWING:
# "Hello <name>! Have a <adj> Valentine's Day!
