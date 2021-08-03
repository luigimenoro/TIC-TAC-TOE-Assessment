# TIC TAC TOE base component, main component of the TIC TAC TOE game
import random
from itertools import cycle
from instruction import instructions_array

# variables/arrays that are going to be called in this program
possible_answers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #/// an array/lists that are the valid response which are also going to used in the "valid_input" function which checks if the user's input is valid
instructions_list = ['yes', 'no'] ; game_modes = ["1", "2"] ; valid_response = ["1", "2", "3"] #/// an array/lists that are the valid response which are also going to used in the "valid_input" function which checks if the user's input is valid
game_mode1 = [ "Player vs Player", "Computer vs Player"]  ; played = ["Computer vs Player", "Player vs Player"] #/// an array/lists to adress what mode the player has played 
f = open ('Welcome to tictactoe ascii.txt', "r") #//// variable to call the ascii text which I have imported from a text file.
names = [] # /// empty array to append the names of the user that are going to be used in the game
elements = [] # /// empty array to append the chosen elements of the user that are going to be used in the game

# Function for the board that is going to be used to display the 3 x 3 grid.
def display_board(board, p1_element, p2_element):
    blankBoard = """
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
                                                                            +==========================+
 """

    for i in range(1, 10):
        if (board[i] == p1_element or board[i] == p2_element):
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
    print(blankBoard)

# function for copying the board which is to going to be used for the main alogotrithm of the computer's move
def getBoardCopy(board):
    # make a duplicate of the board list and return it the duplicate.
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

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

# function that checks if a player wins
def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False

# a class for the player's information in order to identify wether the user is a computer or a player:
class Player:
    def __init__(self, is_human, symbol, name):
        self.is_human = is_human
        self.symbol = symbol
        self.name = name
        self.score = 0

# check user's input
def valid_input(question, valid_lists, error):
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
    choice = valid_input("Please select an empty space between 1 and 9 : ",
                       possible_answers, "Wrong Input, please select an empty sapce between 1 and 9")

    while not space_check(board, int(choice)):
        choice = valid_input("This space isn't free. Please choose between 1 and 9 : ",
                           possible_answers, "Wrong Input, please select an empty sapce between 1 and 9")
    return choice

# The computer's move, which chooses a random number from the moves lists. This function is going to be used in the algorithm
def chooseRandomMove(board, movesList):
    possibleMoves = []
    for i in movesList:
        if space_check(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# the main alogorthm for the computer's move, this algotrithm checks for any possible outcomes and technically the computer is playing against itself, to see which moves can give out the possible outcome and which moves can cause the computer to lose.
def getComputerMove(board, computerLetter, humanelement):
    # a mock test, given the board and mock computer's letter, determine where to move
    if computerLetter == "B":
        playerLetter = humanelement
    else:
        playerLetter = humanelement

    # algorithm for the TIC TAC TOE AI:
    # Check, if we can win the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if space_check(copy, i):
            place_marker(copy, computerLetter, i)
            if win_check(copy, computerLetter):
                return i

    # Check if the player could win on their next move and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if space_check(copy, i):
            place_marker(copy, playerLetter, i)
            if win_check(copy, playerLetter):
                return i

    # try to take one of the corners, if they are free
    choice = chooseRandomMove(board, [1, 3, 7, 9])
    if choice != None:
        return choice
    # try to take the center, if it is free.
    if space_check(board, 5) == "#":
        return 5
    # move on one of the sides
    return chooseRandomMove(board, [2, 4, 6, 8])

# function that asks the human player for their names. It will alternately ask the user's name starting with player 1
def asking_name(n, names, elements):
    while n != 3:
        # asks the user for their name and put their name into a vairable called "name"
        name = input("Hi player {} what would be your name?: ".format(n)) ;  names.append(name) # append or put the input to an empty array called names

        # check if the user's input is not the same as the first user's input
        if n == 2 and name == names[n - 2]:
            del names[n - 1]
            # if the input is the same then, the program asks the user to try again.
            name = input("I am sorry, but that name has already been taken.PLease choose again: ") ; names.append(name) # when the user has finished entering their name. The program then appends it to the empty variable called names

        # asks the user for their preffered element, and put their element to a variable called "elemenet"
        element = input("Hi {} I heard you were ready to play TIC TAC TOE. What would your element be?: ".format(names[n - 1])); elements.append(element)  # append or put the input to an empty array called names
        # check if the user's input is not the same as the first user's input
        if n == 2 and element == elements[n - 2]:
            del elements[n - 1]
            # if the input is the same then, the program asks the user to try again.
            element = input("I am sorry {}, but that element has already been taken by {}. PLease choose again: ".format( names[n-1], names[n - 2])) ; elements.append(element) # when the user has finished entering their element. The program then appends it to the empty variable called elements
        n += 1
