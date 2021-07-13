# Component 3 for TIC TAC TOE
# To Do
'''
1.  User the code in component 2.a to check if the user know how to play tic tac toe
2. If user already know how to play tic tac toe (for component testing only = print "The game will continue")
   But in the real thing, it is not going ot say that instead the game will just continue itself
4.  If the user does not know how to play tic tac toe or entered "NO" or "no"
    then the game will show the instructions
5.  Create a function where everytime the user presses enter, new sets of instructions are displayed.
'''
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

# function that when the user presses enter, it will print the array[x] one by one
def bluh():
    print("Please enter to continue")
    for n in instructions_array:
             user_input =input("")
             if user_input == "":
                 print(n)
             


# Lists or array that will be used to show instructions

# lists for the valid response to use in checking user's input
instruction_list = {"yes", "no","xxx"}

# Array for the instructions
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
    ____________________________________________________________

    Just like this wins:
             |     |     
          0  |  X  |  0
        _____|_____|_____
             |     |     
          X  |  X  |  0  
        _____|_____|_____
             |     |     
          0  |  X  |  X  
             |     |     

    """,
    """
    Have Fun…
    """,
]


              
keep_going = ""
while keep_going != "xxx":
    instruction = game_mode("Have you played TIC TAC TOE before?:", instruction_list, "I am sorry wrong input, please try again")
    instruction.lower()
    if instruction == "no":
        bluh()
    elif instruction == "yes":
        print('The game will continue')
    else:
        break