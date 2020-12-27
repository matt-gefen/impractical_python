# Pseudocode
# Load a list of first names
# Load a list of surnames
# Choose a first name at random
# Assign the name to a variable
# Choose a surname at random
# Assign the name to a variable
# Print the names to the screen (in red)
# Ask the user to quit or play again
# If user plays again: 
    # repeat
# Else 
    # end and exit

import sys
import random
import generator_names as names

def name_generation(first, last):
    """Return a randomly generated name
    
    Arguments:
    first = first name of the generated result
    last = surname of the generated result
    
    Returns:
    string: combination of first and last
    """

    while True:
        firstname = random.choice(first)
        lastname = random.choice(last)

        print("\n\n")
        print("{} {}".format(firstname,lastname), file=sys.stderr)
        print("\n\n")

        try_again =  input("\n\nTry again? (Press ENTER else n to quit)\n")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit")

def main():
    print('\n\nWelcome to the D&D Random Civilian Name Generator')

    while True:    
        options = input(
            "\n\nWhat type o' name you lookin' fer?\n1.Ridiculous \n2.Barovian\n")
        if options == '1':
            name_generation(names.first_ridiculous,names.last_ridiculous)
        elif options == '2':
            name_generation(names.first_barovia,names.last_barovia)
        else:
            print("\nNot an option! Pick a number from the list\n")

if __name__ == "__main__":
 main()