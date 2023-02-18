import time

def start_game():
    print("Welcome to the adventure game!")
    current_room = rooms["outside"]
    print(current_room["description"])
    response = input("> ")
    if response.lower() in ["yes", "y"]:
        enter_cave(current_room)
    else:
        print("Okay, maybe another time.")

def enter_cave(current_room):
    print(current_room["enter_message"])
    print(current_room["light_message"])
    response = input("> ")
    if response.lower() in ["yes", "y"]:
        investigate_light(current_room)
    else:
        print("Okay, let's turn back.")

def investigate_light(current_room):
    print(current_room["light_description"])
    print(current_room["chest_message"])
    response = input("> ")
    if response.lower() in ["yes", "y"]:
        open_chest(current_room)
    else:
        print("Alright, let's keep moving.")

def open_chest(current_room):
    print(current_room["chest_contents"])
    print(current_room["take_message"])
    response = input("> ")
    if response.lower() in ["yes", "y"]:
        current_room["inventory"] = ["key", "paper"]
        print(current_room["next_step"])
        response = input("> ")
        if response.lower() in ["explore", "explore the cave"]:
            explore_cave(current_room)
        else:
            print("Alright, let's keep moving.")
    else:
        print("Okay, let's keep moving.")

def explore_cave(current_room):
    print(current_room["explore_message"])
    response = input("> ")
    if response.lower() in ["yes", "y"]:
        print(current_room["door_message"])
        response = input("> ")
        if response.lower() in ["yes", "y"]:
            if "key" in current_room["inventory"]:
                print(current_room["win_message"])
            else:
                print(current_room["locked_message"])
        else:
            print("Alright, let's keep exploring.")

# Define the game's rooms and their properties using dictionaries
rooms = {
    "outside": {
        "description": "You find yourself standing in front of a dark, forbidding cave. Do you dare enter?",
        "enter_message": "You step inside the cave and immediately feel a chill in the air.",
        "light_message": "You can barely see in the darkness, but you notice a small light flickering in the distance. Do you want to investigate?",
        "light_description": "You cautiously make your way towards the light, and as you get closer you see that it's coming from a torch mounted on the wall. There's also a small wooden chest nearby. Do you want to open it?",
        "chest_message": "Inside the chest, you find a small key and a piece of paper with strange symbols on it. Do you want to take them?",
        "chest_contents": "You now have the key and the paper. What do you want to do next?",
        "take_message": "> take key and paper",
        "next_step": "As you continue deeper into the cave, you come across a large, ornate door. There's a keyhole in the door. Do you want to use the key?",
        "explore_message": "Alright, let's keep exploring.",
        "door_message": "You unlock the door with the key and step through. Congratulations, you have won the game!",
        "win_message": "Congratulations, you have won the game!",
        "locked_message": "The door is locked. You need a key to open it.",
        "inventory": []
    }
}

start_game()

