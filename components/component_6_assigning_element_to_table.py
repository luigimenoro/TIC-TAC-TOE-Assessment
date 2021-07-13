# Component 6 for TIC TAC TOE

import os
"""
1. Assigning user's element to their picked spot, checking if it works
"""

p1_element = input("Player 1 what woul your element be?")
p2_element = input("Player 2 what woul your element be?")

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

# function for players to put their element  
def player_choice(board):
    choice = input("Please select an empty space between 1 and 9 : ")
    return choice

def place_marker(board, marker, position):
    board[position] = marker
    return board

def full_board_check(board):
    return len([x for x in board if x == '#']) == 1


    


 #main_routine:
def main():
    board = ['#'] * 10
    while True:
        i = 1
        players = [p1_element, p2_element]

        game_on = full_board_check(board)
        while not game_on:
            position = player_choice(board)

            if i % 2 == 0:
                    marker = players[1]
            else:
                    marker = players[0]
            
            place_marker(board, marker, int(position))

            display_board(board)

            i += 1


main()
