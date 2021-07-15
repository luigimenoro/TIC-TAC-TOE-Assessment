# Component 6 for TIC TAC TOE
# To do:
"""
1. Ask user where they want to put their element to the grid.
2. Check if the user's response is valid, for example check if the response is withing the numbers 1-9
3. And part of the checking is also to check if the spot is available or not,for example if their is a element in that spot.
4. And if the response is invalid then ask them again.
-------------------------------------------------------------------------------------------------------
BUT IF IT IS VALID:
1. Get the code from component six and assign the element to the table. 
"""


# Asking for player 1 and player 2's names
p1_name = input("Player 1 what is your name?: ")
p2_name = input("Player 2 what is your name?: ")

names = [p1_name, p2_name]
# This is to asking players for their own element
p1_element = input("Player 1 what would your element be?: ")
p2_element = input("Player 2 what would your element be?: ")


possible_answers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]



def display_board(board):
    blankBoard="""
                                                                            +==========================+
                                                                            |        |        |        |
                                                                            |   1    |   2    |   3    |
                                                                            |        |        |        |
                                                                            |--------------------------|
                                                                            |        |        |        |
                                                                            |   4    |   5    |   6    |
                                                                            |        |        |        |
                                                                            |--------------------------|
                                                                            |        |        |        |
                                                                            |   7    |   8    |   9    |
                                                                            |        |        |        |
                                                                            +==========================+
"""

    for i in range(1,10):
        if (board[i] == p1_element or board[i] == p2_element):
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
    print(blankBoard)

# check user's input
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

# function for players to ask them where to put their own element
def player_choice(board):
    # this is the part where the the program asks the user where the want their element to be assaign in the grid
    choice = game_mode("Please select an empty space between 1 and 9 : ", possible_answers, "Wrong Input, please select an empty sapce between 1 and 9")

    while not space_check(board, int(choice)):
        choice = game_mode("This space isn't free. Please choose between 1 and 9 : ",possible_answers, "Wrong Input, please select an empty sapce between 1 and 9")
    return choice

# function to put player's element to their desired position, that was wasked on the function called "player_choice"
def place_marker(board, marker, position):
    board[position] = marker
    return board

# Function that checks if the board is already full which means that there are already no more open spots.
def full_board_check(board):
    return len([x for x in board if x == '#']) == 1

# function that checks if the space is free or if it is not.
def space_check(board, position):
    return board[position] == '#'


    

#main_routine:
def main():
    board = ['#'] * 10
    while True:
        i = 1
        players = [p1_element, p2_element]
        game_on = full_board_check(board)
        n = 0 
        while not game_on:
            # to print out the player who is supposed to be puttng their element
            print("It is {} turn".format(names[n]))
            # to ask where the player wants their element to be assigned to the board
            position = player_choice(board)

            if i % 2 == 0:
                    marker = players[1]
            else:
                    marker = players[0]
            
            place_marker(board, marker, int(position))

            display_board(board)

            i += 1
            n += 1
            # if n is now 2, change n to 1
            if n == 2:
                n = 0



main()
