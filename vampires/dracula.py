#!/usr/bin/python3

# Read in the content of the "Dracula" novel as a file object. 
    #Keep track of the vampires in the text. 
vampires= 0
def main():
    global vampires
    # Open the dracula.txt file as a file object.
    with open("dracula.txt","r") as vampy:
        # Copy selected lines into file object vampytimes.txt
        with open("vampytimes.txt","w") as fang:
            # Select the line in the vampfile if it has "vampire" in it.
            for line in vampy:
                if "vampire" in line.lower():
                    # Prints the line in the file object and counts the times. 
                    print(line)
                    vampires += 1
                    fang.write(line)


main()  #... but on this line you execute the code where you count up the vampires :)

print(vampires) # print again AFTER main() runs any you'll have your vampire count!








