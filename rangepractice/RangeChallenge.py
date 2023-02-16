#!/usr/bin/python3

#Write a script that will output all 99 line sof the song "99 Bottles of Beer on the Wall". 

def main():

    # For every number from 99 to 0, sing the line of the song "99 Bottle sof Beer on the Wall".
    for num in range(99, 0, -1):
        print(f"{num} bottles of beer on the wall, {num} bottle sof beer! You take one down, pass it around...")

main()
