#!/usr/bin/python3

#This script will prompt a user with the question "What is your name?" and "what day of the week is it?" respond with "Hello _____, nice to meet you!"

def main():

    #Pause the program and wait for the user to provide input
    user_input = input("What is your name?")

    #Pause the program and wait for the user to privde input
    user_input2 = input("What day of the week is it today?")

    #Display the input back to the user.
    print("Hello, " + user_input + ", today is " + user_input2 + ". Nice to meet you!")

#this calls main
main()
