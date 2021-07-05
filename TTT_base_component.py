# TIC TAC TOE base component

import random

#Lists of valid response goes here:
#these lists are the valid responses for game modes question.
game_modes = {"computer vs player", "player vs player", "comp vs player"}
# # lists for the valid response to use in checking user's input
instruction_list = {"yes", "no",}
# array for the instructions
instructions_array = [
    """
    You begin by entering your element, and you 
    are going to use that element throughout the game.
    """,
    """
    Then the game will show a big 3 x 3 grid
    """,
    """
    Where it will ask you where you want to put your 
    own element to the 3 x 3 grid. 
    """,
    """
    To put your own element to the grids you need to enter the number that 
    orresponds to the spot where you want the element to be entered.
             |     |     
          1  |  2  |  3 
        _____|_____|_____
             |     |     
          4  |  5  |  6  
        _____|_____|_____
             |     |     
          7  |  8  |  9  
             |     |     
    """,
    """
    Each players will take turn to put their element to the grid.  
    The first player to have a consecutive element in a row win.
    """,
    """
    Have Fun…
    """,
]
# this variable is to call the ascii art for the welcoming of the user
f = open ('Welcome to tictactoe ascii.txt', "r")
# array to put the players names and also to check.
names = []
# array for the players' element
elements = []




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
# function for showing instruction one by one
def instruction():
    # to ask the user if they have played TIC TAC TOE before:
    instruction = intchecker("Have you played TIC TAC TOE before?:", instruction_list, "I am sorry wrong input, please try again")

    # to convert user's response to lower case in order
    instruction.lower()
    
    # if user enters yes: this function will break and continue
    if instruction == "no":
    # to print the instructions, everytime the user presses enter, another set of instruction would be printed
        print("Please enter to continue")
        for n in instructions_array:
                user_input =input("")
                if user_input == "":
                    print(n)
# function that will ask the name for players in player vs player
def asking_name(n):
    while n != 3:
        # asks the user for their name and put their name into a vairable called "name"
        name = input("Hi player {} what would be your name?: ".format(n))
        # append or put the input to an empty array called names
        names.append(name)

        # check if the user's input is not the same as the first user's input
        if n == 2 and name == names[n - 2]:
            del names[n - 1]
            # if the input is the same then, the program asks the user to try again.
            name = input("I am sorry, but that name has already been taken.PLease choose again: ")
            # when the user has finished entering their name. The program then appends it to the empty variable called names
            names.append(name)

        # asks the user for their preffered element, and put their element to a variable called "elemenet"
        element = input("Hi {} I heard you were ready to play TIC TAC TOE. What would your element be?: ".format(names[n - 1]))
        # append or put the input to an empty array called names
        elements.append(element)

        # check if the user's input is not the same as the first user's input
        if n == 2 and element == elements[n - 2]:
            del elements[n - 1]
            # if the input is the same then, the program asks the user to try again.
            element = input("I am sorry {}, but that element has already been taken by {}. PLease choose again: ".format(names[n-1], names[n - 2]))
            # when the user has finished entering their element. The program then appends it to the empty variable called elements
            elements.append(element)

        n += 1

# Function for player vs player
def player_vs_player():
    # asks both of the player for their names using the function called asking_name
    asking_name(1)


# function for computer vs player




#Main routine goes here
def start_game():
    # This section is for welcoming the user, it is going to call the txt file that consists the ascii art
    print(''.join([line for line in f]))

    # this section is to ask the user if they have played tic tac toe before
    instruction()
    # Asks the user if they want to play either computer vs player or player vs player
    print("/n")
    ask_game_mode = intchecker("Hi user welcome to TIC TAC TOE which game mode do you want to play with.\n1. <player vs player> \n2. <computer vs player> \n", game_modes, 
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
        player_vs_player()