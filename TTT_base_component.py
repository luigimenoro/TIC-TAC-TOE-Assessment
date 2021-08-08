# TIC TAC TOE base component, main component of the TIC TAC TOE game
import random 
from instruction import instructions_array
import os
from instruction import color

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
                                                                            |        |        |        |
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
    # make a duplicate of the board list this is for the computer's algorithm
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
        print(color.RED + str(error) + color.END)
        print()

# function for players to ask them where to put their own element
def player_choice(board):
    # this is the part where the the program asks the user where the want their element to be assaign in the grid
    choice = valid_input("Please select an empty space between 1 and 9 : ",
                       possible_answers, "Wrong Input, please select an empty sapce between 1 and 9")

    while not space_check(board, int(choice)):
        choice = valid_input(color.RED + "This space isn't free. Please choose between 1 and 9 : " + color.END,
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

# function for showing instruction one by one
def instruction():
    # to ask the user if they have played TIC TAC TOE before:
    instruction = valid_input( color.BOLD + "Have you played my TIC TAC TOE before? <yes> or <no>:" + color.END, instructions_list, "I am sorry wrong input, please try again")

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

# function that asks the human player for their names. It will alternately ask the user's name starting with player 1
def asking_name(n, names, elements):
    while n != 3:
        # asks the user for their name and put their name into a vairable called "name"
        name = input("Hi player {} what would be your name?: ".format(n)) ;  names.append(name) # append or put the input to an empty array called names

        # check if the user's input is not the same as the first user's input
        if n == 2 and name == names[n - 2]:
            del names[n - 1]
            # if the input is the same then, the program asks the user to try again.
            name = input(color.RED + "I am sorry, but that name has already been taken. Please choose again: " + color.END) ; names.append(name) # when the user has finished entering their name. The program then appends it to the empty variable called names

        # asks the user for their preffered element, and put their element to a variable called "elemenet"
        element = input("Hi {} I heard you were ready to play TIC TAC TOE. What would your element be? (consist of only one letter only and no numbers e.g <K> or <&>)): ".format(names[n - 1])); elements.append(element)  # append or put the input to an empty array called names
        # check if the user's input is not the same as the first user's input
        if n == 2 and element == elements[n - 2]:
            del elements[n - 1]
            # if the input is the same then, the program asks the user to try again.
            element = input(color.RED +"I am sorry " + str(names[n-1]) + ", but that element has already been taken by " + str(names[n - 2]) + ". PLease choose again: " + color.END) ; elements.append(element) # when the user has finished entering their element. The program then appends it to the empty variable called elements
        n += 1

# function that clears the terminal after the user entered their element to the 3 x 3 grid
def clear():
	os.system("cls")
	print()

# a class for the different modes avaialbe in this program. There is a function for player vs player and also there is a function for comp_vs_player
class modes:
    def player_vs_player(): # function to asks for the element's of the two human players
        asking_name(1, names, elements)
    def comp_vs_player():
        player1_name = input("Choose a name for player 1: "); names.append(player1_name) # Asks the user for their name
        p1_element = input("{} what would be your element? (must be only one letter only, and not a number, and also not <B> e.g <K> or <&>)): ".format(player1_name)); elements.append(p1_element) # ask the user for their element

        # if user enters a more than two letter for their element or a number or the same as Computer's element program will asks again.
        while len(p1_element) > 1 or p1_element.isdigit() == True or p1_element.upper() == "B": 
            del elements[0] # Deletes that appended element if the p1_element satisfies the expressions
            p1_element = input( color.RED + "{} Invalid input (must be only one letter only. and not a number, and also not <B> e.g <K> or <&>)): ".format(player1_name) + color.END); elements.append(p1_element) # asks the user again for their element
        
        player2_name = "Computer"; names.append(player2_name)
        p2_element = "B" ;  elements.append(p2_element)

# Main routine goes here
def main():
    clear() # to clear the terminal 
    print(''.join([line for line in f])) # This section is for welcoming the user, it is going to call the txt file that consists the ascii art

    instruction()   # to ask the user if they have played the game before. if answer is yes, then it will, else it will show the instructions

    # Asks the user if they want to play either computer vs player or player vs player
    print("\n")
    choice = valid_input(color.BOLD + "Hi user welcome to TIC TAC TOE which game mode do you want to play with.\n<(1). player vs player>\n<(2). computer vs player>\n" + color.END, game_modes, "I am sorry this is not one of the modes. Please choose (1) for <computer vs player> or (2) for <player vs player>")

    # to determine what mode the user have played or what mode has not played
    not_played_mode = played[int(choice) - 1]  # Identifies which mode has been not played
    mode_played = game_mode1[int(choice) - 1]  # Identifies which mode has been played

    clear() # to clear the terminal

    print(color.UNDERLINE + "You are going to play " + str(mode_played) + color.END) # To remind the user what mode they are playing, in case they have forgotten. This message will also be underlines to emphasize the message more
    if choice== '1':  
        modes.player_vs_player() # If player wants to play player vs player, it is going to call the function called player_vs_player in the class called mode
        player1_is_human = True  #
        player2_is_human = True  #  And since the user wants the play player vs player all the users would be human
    elif choice == '2':
        modes.comp_vs_player() # If play wants to play computer vs player, it is the program will cal the function called comp_vs_player in the class called mode
        player1_is_human = True  #
        player2_is_human = False # And since the user wants to play computer vs player player 1 would be human, while player 2 would be not human or aka the Computer 

    clear() # to clear the terminal
    # Start of the while program for the tic tac toe game annd also for the reloop
    board = ['#'] * 10  # to generate the board by using multiplying the "Free" spots by 10
    while True:
        i = 1
        n = 0
        game_on = full_board_check(board) 
        display_board(board, elements[0], elements[1]) # Displays the empty board before the user puts in their element

        # The start of the proper game of tic tac toe
        while not game_on:     
            print(color.GREEN + "It is {}'s turn".format(names[n]) + color.END) # to print out the player who is supposed to be puttng their element
            # to ask where the player wants their element to be assigned to the board
            if player1_is_human == True and player2_is_human == True:
                position = player_choice(board)                         # If player 1 is human and player 2 is human then asks the user where they want their element to be put in the grid

            if i % 2 == 0: # to change the players according to the i variable. If the "i" variable is an even number it will change the current player to the next player. 
                marker = elements[1]
            else:                        
                marker = elements[0] 

             # if user choose player vs computer
            if player1_is_human == True and player2_is_human == False:  
                if marker == elements[0]:          # if the marker is the human player, it will asks the user where they want their element to be put in the 3 x 3 grid
                    position = player_choice(board)
                else:
                    position = getComputerMove(board, elements[1], elements[0])    # in order to get the position of the computer's element, computer's element would call the function named getComputerMove which is the main algorithm of the computer's move

            place_marker(board, marker, int(position))         # places the user or the computer's element on the 3 x 3 grid.

            clear() # clears the terminal 

            display_board(board, elements[0], elements[1]) # updates the board everytime the user enetered their element

            i += 1
            # to check if the player has win or not
            if choice == "2" and win_check(board, marker) and marker == elements[1]:
                print(color.RED + "You lost, Computer won the game!" + color.END)  # When the computer wins and the human loses, it will print the message that "you lost". And the whole message would be in red
                break
            elif win_check(board, marker):
                print(color.YELLOW + "Congratulations {} has won!".format(names[n]) + color.END) # When the computer or the other human player loses, it will congratulate the player that won. And the whole message would be in yellow.
                break
            elif full_board_check(board):
                print(color.PURPLE + "Wonderful, it is a tie!!" + color.END) # When the game turns out to be a tie, the program will say that it is a tie. And the whole message owuld be printed in purple to emphasize more. 
            game_on = full_board_check(board)

            # To call whose turn it is for the player
            n += 1
            # if n is now 2, change n to 1, this is for the name calling
            if n == 2:
                n = 0

        # deletes the element and name array for the reloop of the game
        del elements[:]
        del names[:]
        # reloop the game   
        keep_going1 = valid_input(" Would you like to play again? | <1> To play the same mode | <2> To play {} | <3> To quit |: ".format(not_played_mode), valid_response, "Invalid input please try again") # After each round finishes the program will ask the user if they want to play the game again
       

        if keep_going1 == '1' and mode_played == game_mode1[0] or keep_going1 == "2" and not_played_mode == played[1] : # 
            modes.player_vs_player()
            player1_is_human = True
            player2_is_human = True
         # if use picked 2:
        elif keep_going1 == "1" and mode_played == game_mode1[1] or keep_going1 == "2" and not_played_mode == played[0]  : 
            modes.comp_vs_player()
            player1_is_human = True
            player2_is_human = False
        elif keep_going1 == "3":
            print(color.CYAN + "Thankyou for playing the game" + color.END)
            break
        clear()

        board = ['#'] * 10

if __name__ == '__main__':
    main()
 