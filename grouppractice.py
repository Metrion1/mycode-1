#!/usr/bin/env python3


#Tell the user their Chinese New Year animal based on their birthday. 

#Prompt the user for their name.
def main():    
    usr_name = input("Please enter your name:\n>") 
              
    usr_name = usr_name.title()    #Turns user input into Title Case

    #Prompts user for their birth year. 
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
            

    zodiac = {
      "Sign": ["Rabbit", "Rat", "Tiger", "Ox", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig"], 
      "year": [[2011, 1999, 1987, 1975, 1963], [2020, 2008, 1996, 1984, 1972, 1960], [2010, 1998, 1986, 1974, 1962], [2021, 2009, 1997, 1985, 1973, 1961], [2012, 2000, 1988, 1976, 1964], [2013, 2001, 1989, 1977, 1965], [2014, 2002, 1990, 1978, 1966], [2015, 2003, 1991, 1979, 1967], [2016, 2004, 1992, 1980, 1968], [2017, 2005, 1993, 1981, 1969], [2018, 2006, 1994, 1982, 1970], [2019, 2007, 1995, 1983, 1971]] 
    }           

    for eachlist in zodiac["year"]: # return each list of years one at a time
        if usr_date in eachlist: # is the user's birth year in that list?
            # once a match is found, find the associated sign
            # list.index() method returns the index number from a list
            # list.index("Rabbit") --> 0
            position= zodiac["year"].index(eachlist) # which list in that list is the match? position 0? position 3??
            print(zodiac["Sign"][position])
main()
