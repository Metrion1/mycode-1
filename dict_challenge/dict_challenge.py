#!/usr/bin/python3

#This script will anser user questions about superhero information


"""Dictionary Challenge Script"""

#Define the maine fucntions
def main():

    char_nam = input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n>").title()
    char_stat = input("What statistic do you want to know about? (real name, super power, archenemy)\n>").lower()

#Establish the dictionary
    marvelchars= {
    "Starlord":
    {"real name": "peter quill",
    "super power": "dance moves",
    "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
    "super power": "shape shifter",
    "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner", 
    "super power": "super strength",
    "archenemy": "adrenaline"}
                    }


    print(f"{char_nam}'s {char_stat} is: {marvelchars[char_nam][char_stat]}")

#Call main fuction
main()
