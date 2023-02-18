#!/usr/bin/python3
import time

def start_game():
    print("Welcome to the adventure game!")
    print("You find yourself standing in front of a dark, forbidding cave. Do you dare enter?")
    response = input("> ")
    if response.lower() in ["yes", "y"]:
        enter_cave()
    else:
        print("Okay, maybe another time.")

def enter_cave():
    print("You step inside the cave and immediately feel a chill in the air.")
    print("You can barely see in the darkness, but you notice a small light flickering in the distance. Do you want to investigate?")
    response = input("> ")
    if response.lower() in ["yes", "y"]:
        investigate_light()
    else:
        print("Okay, let's turn back.")

def investigate_light():
    print("You cautiously make your way towards the light, and as you get closer you see that it's coming from a torch mounted on the wall.")
    print("There's also a small wooden chest nearby. Do you want to open it?")
    response = input("> ")
    if response.lower() in ["yes", "y"]:
        open_chest()
    else:
        print("Alright, let's keep moving.")

def open_chest():
    print("Inside the chest, you find a small key and a piece of paper with strange symbols on it.")
    print("Do you want to take them?")
    response = input("> ")
    if response.lower() in ["yes", "y"]:
        print("You now have the key and the paper. What do you want to do next?")
        response = input("> ")
        if response.lower() in ["explore", "explore the cave"]:
            explore_cave()
        else:
            print("Alright, let's keep moving.")
    else:
        print("Okay, let's keep moving.")

def explore_cave():
    print("As you continue deeper into the cave, you come across a large, ornate door.")
    print("There's a keyhole in the door. Do you want to use the key?")
    response = input("> ")
    if response.lower() in ["yes", "y"]:
        print("You unlock the door with the key and step through.")
        print("Congratulations, you have won the game!")
    else:
        print("Alright, let's keep exploring.")

start_game()

