# Component 9 for TIC TAC TOE
# To do:
"""
    After each round/game ends, ask the user if they want to play the same mode, 
    or play the other mode, or ask them if they want to quit

1. Import the function from component 2 to check for valid input 
1a. Make an array to store the valid_lists
2. Add a variable to state which mode the user picked
3. After the game finish ask the user if they want to play:
    a. The same mode they have previously played
    b. The other mode. (e.g. if they have previously played computer vs computer, ask them if they want to play player vs player & vice versa)
    c. If they want to quit.
4. Recycle the game

"""
# function that check if the user's input when asked if they have played the game before is valid
def game_mode(question, valid_lists, error):

    valid = False
    while not valid:

        # asks the user for their game mode and put choice in lowercase
        response = input(question).lower()

        # iterates through list and if reponse is an item
        # in the list (or the first letter of an item)
        # full item is returned

        for item in valid_lists:
            if response == item[0] or response == item:
                return item
                print()
        
        # output error if item not in list
        print(error)
        print()

# array to store the valid lists
valid_response = ["1", "2", "3"]
game_mode1 = [ "Player vs Player", "Computer vs Player"]
played = ["Computer vs Player", "Player vs Player"]

# While loop for component testing(only)
keep_going = ""
while keep_going != "xxx":
    # to represent the mode that the user played in the real code
    game_played = int(input("What mode do you want to play? | <1> Computer vs Player | <2> Player vs Player |: "))

    mode = game_mode1[game_played - 1]  

     # for component testing, it will print the game has finished to represent the game ending
    print("The game has finished\n")
    print()

    keep_going1 = game_mode(" Would you like to play again? | <1> To play the same mode | <2> To play {} | <3> To quit |: ".format(mode), valid_response, "Invalid input please try again")

    # if user picked 1
    if keep_going1 == "1":
        print("You are going to play {}".format(played[game_played - 1]))
        print()
    # if use picked 2:
    elif keep_going1 == "2":
        print("It is going to play {}".format(mode))
        print()
    # else quit the game
    else:
        print("In the real game it is going to end the game")
        print()
