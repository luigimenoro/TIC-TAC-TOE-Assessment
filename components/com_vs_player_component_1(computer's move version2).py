import random 
from itertools import cycle


possible_answers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]



def display_board(board,p1_element, p2_element):
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

def chooseRandomMove(board, movesList):
    possibleMoves = []
    for i in movesList:
        if space_check(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None



def getComputerMove(board, computerLetter, humanelement):
    # a mock test, given the board and mock computer's letter, determine where to move
    if computerLetter == "B":
        playerLetter = humanelement
    else:
        playerLetter = humanelement

    
    #algorithm for the TIC TAC TOE AI:
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
    if space_check(board, 5):
        return 5


    # move on one of the sides
    return chooseRandomMove(board, [2, 4, 6, 8])
        


def replay():
    playAgain = input("Do you want to play again (y/n) ? ")
    if playAgain.lower() == 'y':
        return True
    if playAgain.lower() == 'n':
        return False
def asking_name(n,names,elements):
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



def main():
    print("Welcome to tic tac toe!")
    print("type the appropiate number to choose a game option: ")
    choice = input("1.player vs player\n2.player vs computer\n: ")
    if choice == '1':
        names = []
        elements = []
        asking_name(1, names, elements)
        player1_is_human = True
        player2_is_human = True
    elif choice == '2':
        player1_name = input("Choose a Name for player 1: ")
        p1_element = input("{} what would be your element?: ".format(player1_name))
        player2_name = "Computer"
        p2_element = "B"
        names = [player1_name, player2_name]
        elements = [p1_element, p2_element]
        player1_is_human = True
        player2_is_human = False
   
    player1 = Player(player1_is_human, elements[0], names[0])
    player2 = Player(player2_is_human, elements[1], names[1])
    players = [player1, player2]

    
    board = ['#'] * 10
    while True:
        i = 1
        players = [elements[0],elements[1]]
        game_on = full_board_check(board)
        n = 0 
        display_board(board,elements[0],elements[1])
        while not game_on:
            # to print out the player who is supposed to be puttng their element
            print("It is {} turn".format(names[n]))
            # to ask where the player wants their element to be assigned to the board
            if player1_is_human == True and player2_is_human == True:
                position = player_choice(board)
            
            if i % 2 == 0:
                    marker = players[1]
            else:
                    marker = players[0]

             # if user choose player vs computer
            if player1_is_human == True and player2_is_human == False:
                if marker == players[0]:
                    position = player_choice(board)
                else:
                    position = getComputerMove(board, p2_element, p1_element)

            
            place_marker(board, marker, int(position))

            display_board(board,elements[0],elements[1])

            i += 1
            # to check if the player has win or not
            if win_check(board, marker):
                print("Congratulations {} has won!".format(names[n]))
                break
            elif full_board_check(board):
                print("Wonderful, it is a tie!!")
            game_on = full_board_check(board)

             # To call whose turn it is for the player
            n += 1
            # if n is now 2, change n to 1, this is for the name calling
            if n == 2:
                n = 0

        if not replay():
          break


if __name__ == '__main__':
    main()