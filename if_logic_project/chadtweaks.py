#!/usr/bin/python3

TwistedPretzelSticks = 0
Rounds = 0
TraditionalPretzels = 0
FlavoredPretzelPieces = 0
ChocolateCoveredPretzels = 0
BraisedTwistPretzels = 0
PretzelSandwiches = 0
GlutenFreePretzels = 0

while True: # this loop will repeat until the user types in "yes" or "no"
    answer = input('Are you afraid of gluten? ')

    if answer.lower() == 'yes':   
            print('okay, next question!')
            GlutenFreePretzels += 1
            break # exits the loop, adding 1 to glutenfreepretzels, after user answered "yes" 
    elif answer.lower() == 'no':
            print("okay, next question!")
            break # exits the loop after user answered "no"
    else:              
            print('You must answer "yes" or "no."') # scolds the user before repeating the loop

while True: # this loop will repeat until the user types in "yes" or "no"
    answer = input('Do you know the muffin man? ')

    if answer.lower() == 'yes':   
            print('okay, next question!')
            GlutenFreePretzels += 1
            break # exits the loop, adding 1 to glutenfreepretzels, after user answered "yes" 
    elif answer.lower() == 'no':
            print("okay, next question!")
            break # exits the loop after user answered "no"
    else:              
            print('You must answer "yes" or "no."') # scolds the user before repeating the loop
