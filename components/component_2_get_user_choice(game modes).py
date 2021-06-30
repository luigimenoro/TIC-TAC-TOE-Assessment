# Component 2 for TIC TAC TOE
# To Do
'''
1. Ask user what mode they want to play
2. Make a list that shows valid statement
3. Check if the user's input is valid
4. Recycle the code so that we can use it for next codings
'''

# the main function that asks the user for their modes and check their response using a lists

def game_mode(question, game_modes, error):

    valid = False
    while not valid:

        # asks the user for their game mode and put choice in lowercase
        response = input(question).lower()

        # iterates through list and if reponse is an item
        # in the list (or the first letter of an item)
        # full item is returned

        for item in game_modes:
            if response == item[0] or response == item:
                return item
                print()
        
        # output error if item not in list
        print(error)
        print()


# lists of valid responses
game_modes = {"computer vs player", "player vs player", "xxx"}


# main routine asks the user 
# It is in while loop for testing purposes
keep_going = " "
while keep_going != "xxx":

      # Ask user for choice and check if it's valid
    print("\n")
    keep_going = game_mode("Hi user welcome to TIC TAC TOE which game mode do you want to play with.\n1. <player vs player> \n2. <computer vs player> \n ", game_modes, 
                            "I am sorry this is not one of the modes. Please choose between <computer vs player> or <player vs player>")


    # Print the user's response for testing purposes only
    print("You are going to play {}".format(keep_going))
    
