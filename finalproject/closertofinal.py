#!/usr/bin/python3
import time
import random

def start():
    #setting the scene
    print("..." "\n... ... \n Your eyes open slowly to a stark white frozen wasteland")
    time.sleep(2)
    answer= input("What are you called? \n >")
    print(f"You start out with {player_strength} strength, {player_health} health, and {player_food} food.")
    print("----------------------------------------------------------------")
    time.sleep(1)
    return answer

#Player Stats
player_health = 20
player_strength = 10
player_food = 0
lemming_health = 5
lemming_str = 1
bear_health = 400
bear_str = 40 
taken_paths = []
player_name = start() 

print(f"Welcome, {player_name}, to the Frozen Wasteland! Your mission begins now.")
print("----------------------------------------------------------------")
# First prompt with 5 paths to choose from
print("You have awaken on the frozen tundra. You can see a golden disc piercing the clouded sky. \n The ground and sky blend together, and the light makes your eyes hurt if you open them more than a squint.")


while True: # move this down below all those prints if you don't want to see them every time    
    print("What do you do?")
    print("1. Head towards the North.")
    print("2. Head towards the South.")
    print("3. Head towards the West.")
    print("4. Head towards the East.")

    # Get user input for the first prompt
    prompt = int(input("Enter the number of your choice: "))

    # Check the user's input and determine the outcome
    if prompt == 1:
        if "lemmings" not in taken_paths:
            print("You hear a rumble, and look around. You see a horde of wild lemmings coming straight at you.")

            while True: # starting an infinite loop

                    if lemming_health <= 0:
                        player_food += 10
                        taken_paths.append("lemmings")
                        print(f"The lemming is dead! You are victorious! You now have {player_food} pieces of food in your inventory.")
                        # add whatever else you want to happen before combat ends here
                        break

                    elif player_health <= 0:
                        print("The lemmings have defeated you! How embarrassing!")
                        break

                    #Ask the user if they want to attack or flee
                    decide= input("What do you do?\n(Roll to attack) or (Go back)>")

                    #If the user chooses to attack
                    if decide.lower() != "roll to attack":
                        print("You flee!")
                        break
                

                    player_roll = random.randint(1, 20) + player_strength
                    lemming_roll = random.randint(1, 20)

                    #The player rolls higher than the lemming and has a successfull attack
                    if player_roll > lemming_roll:
                        damage = random.randint(1, 6) + player_strength
                        lemming_health -= damage
                        print(f"You hit the lemming horde for {damage} damage. The horde has {lemming_health} health remaining.")
                    #The player rolls lower than the lemming 
                    elif player_roll < lemming_roll:
                        damage = random.randint(1, 4) + lemming_str
                        player_health -= damage
                        print(f"The lemming horde hits you for {damage} damage. You have {player_health} health remaining.")
                    #The player and the lemming roll the same
                    elif player_roll == lemming_roll:
                        print(f"You and the lemming horde both miss!")




    if prompt == 2:
        if "polar bear" not in taken_paths:
            print("You feel the ground rumble beneath your frozen feet. You and look around. A giant, white polar bear is coming straight at you!")

            while True: # starting an infinite loop

                    if bear_health <= 0:
                        print("The bear is dead! That's incredible! You are victorious!")
                        player_food += 100
                        taken_paths.append("polar bear")
                        # add whatever else you want to happen before combat ends here
                        break

                    elif player_health <= 0:
                        print("The polar bear feasts on your mangled carcass, you have been defeated!")
                        print("=============\n GAME OVER\n=============")
                        exit()
                        break

                    #Ask the user if they want to attack or flee
                    decide= input("What do you do?\n(Roll to attack) or (Go back)>")

                    #If the user chooses to attack
                    if decide.lower() != "roll to attack":
                        print("You flee!")
                        break


                    player_roll = random.randint(1, 20) + player_strength
                    bear_roll = random.randint(1, 20) + bear_str

                    #The player rolls higher than the polar bear and has a successfull attack
                    if player_roll > bear_roll:
                        damage = random.randint(1, 6) + player_strength
                        bear_health -= damage
                        print(f"You hit the polar bear for {damage} damage. The beast has {bear_health} health remaining.")
                    #The player rolls lower than the bear 
                    elif player_roll < bear_roll:
                        damage = random.randint(1, 12) + bear_str
                        player_health -= damage 
                        print(f"The polar bear hits you for {damage} damage. You have no health remaining.")
                    #The player and the bear  roll the same
                    elif player_roll == bear_roll:
                        print(f"You and the bear both miss!")


    if prompt == 3:
        if "yellow snow" not in taken_paths:
            print("You head West, step after dreary step. Do your eyes deceive you? A puddle of mustard steams in front of you. This would pair excellently with any food in your inventory.")

            while True: # starting an infinite loop
                #Prompt the user for a choice
                if player_health <= 0:
                        print("You have contracted leptospirosis and died from kidney and liver failure.")
                        print("=============\n GAME OVER\n=============")
                        exit()
                        break
                else: 

                    decide= input("What do you do?\n (Eat the mustard) or (Go Back)")
                    
                    if decide.lower() == "eat the mustard" and player_food <= 0:
                        damage = random.randint(1, 12)
                        player_health -= damage
                        
                        print(f"Ew! Gross! That wasn't mustard, that was yellow snow! Your health drops {damage} points and is now at {player_health} points.")
                    
                    elif decide.lower() == "eat the mustard" and player_food > 0:
                        damage = random.randint(1, 4)
                        player_health -= damage
                        player_food = player_food -1
                        print(f"Ew! Gross! That wasn't mustard, that was yellow snow! Your health drops {damage} and you wasted 1 piece of food. You now only have {player_food} pieces of food left.")
                    
                        #If the user chooses to attack
                    if decide.lower() != "eat the mustard":
                            print("You return to the crossroads.")
                            break
