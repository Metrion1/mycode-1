#!/usr/bin/python3

round = 0  #start counting at 0

answer= " "

while round < 3 and answer != "Brian":
    round += 1 #Increase the round count by 1.

    answer = input('Finish the movie title, "Monty Python\'s The Life of  _______": ')    #collect input from user

    if answer.title() == 'Brian':    #logic to check if user supplied correct answer
        print('Correct')    
        break    #escape while loop
    elif answer == "Shrubbery":
        print("You gave the super secret answer!")
        break    #escape while loop
    elif round == 3:    #Logic to ensure round has not yet reached 3.
        print('sorry, the answer was Brian.')
        break    #escape while loop
    else:               #if answer was wrong, and the round is not yet 3
        print('Sorry. Try again!')

