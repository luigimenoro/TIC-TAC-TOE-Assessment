# Computer Versus Player mode component 1
# To do
# Brief: 
# in this component we need to get a random number between 1 - 9, in order for 
# the computer to choose which space in the grid it wants to go to.
"""
--------------------------------------------------------------
1.  For component testing) ask the user for number between 1 and 9. 
2. Get a random number between 1 and 9 and print that this number will represent the computer's choice
3. If the computer's chosen number has been picked by the user then print that it has already been picked, and 
make the user get a random number between 1 and 9, until it gets a valid numbenr

"""
from random import randint

def c2():
    keep_going = ""
    # while loop to for component testing only
    while keep_going != "xxx":
        # asking user for a number between 1 and 9
        print("User's input")
        ask_user = int(input("Please choose a number between 1 and 9: "))

        # generating a random number between 1 and 9 for computer's move
        comp_choice = randint(1, 9)
        print("Computer's choice")
        print("I choose number {}".format(comp_choice))

        # to check if comp_choice is equal to ask_user
        if comp_choice == ask_user:
            print("computer choice is the same user's input")

            while comp_choice == ask_user:
                comp_choice = randint(1, 9)
                print("I choose another number {}".format(comp_choice))

        keep_going = print("Keep going??")


c2()