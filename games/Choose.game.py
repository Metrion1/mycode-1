#!/usr/bin/python3
# choose your own adventure game with 50 turns (with restart)

# initialize variables
turn = 1

# define game function
def game(turn):
    print("Turn", turn)
    print("You are in a dark room. There are three doors in front of you.")
    print("Which door do you choose?")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("You open the first door and find a treasure chest full of gold!")
    elif choice == "2":
        print("You open the second door and find a monster waiting for you. You are defeated.")
        turn -= 1
    elif choice == "3":
        print("You open the third door and find a trap. You are caught and cannot escape.")
        turn -= 1
    else:
        print("Invalid input. Please try again.")
        turn -= 1

    turn += 1
    if turn > 50:
        print("Congratulations! You made it to the end of the game!")
        return

    game(turn)

# start the game
game(turn)

