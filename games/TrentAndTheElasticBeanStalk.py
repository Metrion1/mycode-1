#!/usr/bin/python3

# choose your own adventure game with 50 turns (with multiple doors)

# initialize variables
turn = 1

# define game function
def game(turn):
    print("Turn", turn)

    if turn == 1:
        print("You are in a dark room. There are three doors in front of you.")
        print("Which door do you choose?")
        choice = input("Enter 1, 2, 3, 4, or 5: ")

        if choice == "1":
            print("You open the first door and find a treasure chest full of gold!")
        elif choice == "2":
            print("You open the second door and find a monster waiting for you. You are defeated.")
            turn -= 1
        elif choice == "3":
            print("You open the third door and find a trap. You are caught and cannot escape.")
            turn -= 1
        elif choice == "4":
            print("You open the fourth door and find a magical sword. You pick it up and continue on.")
        elif choice == "5":
            print("You open the fifth door and find a healing potion. You drink it and continue on.")
        else:
            print("Invalid input. Please try again.")
            turn -= 1

    else:
        print("You come to a crossroads. There are four paths ahead of you.")
        print("Which path do you choose?")
        choice = input("Enter 1, 2, 3, or 4: ")

        if choice == "1":
            print("You follow the first path and encounter a bandit. You defeat him and continue on.")
        elif choice == "2":
            print("You follow the second path and find a dead end. You turn around and try another path.")
            turn -= 1
        elif choice == "3":
            print("You follow the third path and find a hidden treasure. You add it to your collection and continue on.")
        elif choice == "4":
            print("You follow the fourth path and come to a bridge. You successfully cross it and continue on.")
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

