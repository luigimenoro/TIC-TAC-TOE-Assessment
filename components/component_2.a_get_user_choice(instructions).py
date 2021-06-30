# Component 2.a for TIC TAC TOE
# To Do
'''
1. Ask user if they have played TIC TAC TOE before
2. Make a list that shows valid statement
3. Check if the user's input is valid
4. Use the code in component 2 so that we can just call it in the base component if we need the function
'''

# the main function that asks the user if they have played and check their response using a lists
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


# lists for the valid response to use in checking user's input
instruction_list = {"yes", "no","xxx"}

# main routine asks the user 
# It is in while loop for testing purposes
keep_going = " "
while keep_going != "xxx":

      # Ask user for choice and check if it's valid
    print("\n")
    keep_going = game_mode("Hi user, before we start have you played TIC TAC TOE before <yes> or <no>: ", instruction_list, 
                            "I am sorry this is not one of the modes. Please choose between <yes> or <no>")


    # Print the user's response for testing purposes only
    if keep_going == "no":
      print("The game will show instructions")
    else:
        print("The game will continue")
    

