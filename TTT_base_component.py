# TIC TAC TOE base component

import random

#Functions goes here

# function for the board

# Function to check for user's response
def intchecker(question, valid_lists, error):

    valid = False
    while not valid:

        # asks the user for their game mode and put choice in lowercase
        response = input(question).lower()

        # iterates through list and if reponse is an item
        # in the list (or the first letter of an item)
        # full item is returned

        for item in valid_lists:
            if response == item[0] or response == item:
                return response
                print()
        
        # output error if item not in list
        print(error)
        print()

# Function for player vs player

# function for computer vs player



#Lists of valid response goes here
#these lists are the valid responses for game modes question.
game_modes = {"computer vs player", "player vs player", "comp vs player"}

# this variable is to call the ascii art for the welcoming of the user
f = open ('Welcome to tictactoe ascii.txt', "r")


#Main routine goes here
def start_game():
    # This section is for welcoming the user, it is going to call the txt file that consists the ascii art
    print(''.join([line for line in f]))

    # Asks the user if they want to play either computer vs player or player vs player
    print("/n")
    ask_game_mode = intchecker("Hi user welcome to TIC TAC TOE which game mode do you want to play with.\n1. <player vs player> \n2. <computer vs player> \n ", game_modes, 
                                "I am sorry this is not one of the modes. Please choose between <computer vs player> or <player vs player>")

    # if user's response is comp vs player it will change it to computer vs player
    if ask_game_mode == "comp vs player":
        ask_game_mode = "computer vs player"

    # Print the user's response for testing purposes only
    print("You are going to play {}".format(ask_game_mode))

    # if user's response is one of the valid responses call the function
    if ask_game_mode == "computer vs player":
        # add the computer vs player function here

    else:
        # add the player vs player function here