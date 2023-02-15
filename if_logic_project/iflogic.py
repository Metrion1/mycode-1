#!/usr/bin/python3


"""What kind of Snyder's of Hanover (TM) Pretzel are you? 

        options are: 
        Twisted Pretzel Sticks
        Rounds
        Traditional Pretzels
        Flavored Pretzel Pieces
        Chocolate covered Pretzels
        Braised Twist Pretzels
        Pretzel Sandwiches
        Gluten Free Pretzels

"""

  #Variables established to keep track of user score
TwistedPretzelSticks = 0
Rounds = 0
TraditionalPretzels = 0
FlavoredPretzelPieces = 0
ChocolateCoveredPretzels = 0
BraisedTwistPretzels = 0
PretzelSandwiches = 0
GlutenFreePretzels = 0

while True: # This loop will repeat untitl the user types in "yes" or "no"
    answer = input('Are you afraid of gluten? ')    #collect input from user

    if answer.lower() == 'yes':    #logic to check if user supplied correct answer
        print('okay, next question!')
        GlutenFreePretzels += 1
        break    #escape while loop and adds to glutenfreepretzels, after user answered "yes"
    elif answer.lower() == 'no':
        print("okay, next question!")
        break    #escape the loop and moves to the next question if answered "no"
    else:               #if answer was wrong, and the round is not yet 3
        print('Sorry. You must answer with either "Yes" or "No".') #prompts the user to answer with the proper answers.
while True:
    answer = input('Do you like to dance? ')    #collect input from user
    
    if answer.lower() == 'yes':    #logic to check if user supplied correct answer
        print('okay, next question!')
        TwistedPretzelSticks += 1
        break     #escape while loop
    elif answer.lower() == 'no':
        print('okay, next question!')
        break
    else:
        print('Sorry. Try again!')    #if answer was wrong, and the round is not yet 3
while True:
    answer = input('Do you like lots of flavor? ')    #collect input from user
    
    if answer.lower() == 'yes':    #logic to check if user supplied correct answer
        print('okay, next question!')
        FlavoredPretzelPieces += 1
        break     #escape while loop
    elif answer.lower() == 'no':
        print('okay, next question!')
        break
    else:
        print('Sorry. Try again!')    #if answer was wrong, and the round is not yet 3


print(f""" 
FINAL SCORES:
Twisted Pretzel Sticks: {TwistedPretzelSticks}
Rounds: {Rounds}
TraditionalPretzels: {TraditionalPretzels}
FlavoredPretzelPieces: {FlavoredPretzelPieces}
ChocolateCoveredPretzels: {ChocolateCoveredPretzels}
BraisedTwistPretzels: {BraisedTwistPretzels}
PretzelSandwiches: {PretzelSandwiches}
GlutenFreePretzels: {GlutenFreePretzels}""")



