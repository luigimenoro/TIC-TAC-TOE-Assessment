# Component 5 for TIC TAC TOE
# To Do
'''
1. Make a function that makes the 3 x 3 grid. Inside the grid are arrays or numbers so that we can append the user's input to that array
'''
# represents the tic tac toe values of the 3 x 3 grid
def display_board(board):
    blankBoard="""
                                                                            +=======================+
                                                                            |       |       |       |
                                                                            |   1   |   2   |   3   |
                                                                            |       |       |       |
                                                                            |-----------------------|
                                                                            |       |       |       |
                                                                            |   4   |   5   |   6   |
                                                                            |       |       |       |
                                                                            |-----------------------|
                                                                            |       |       |       |
                                                                            |   7   |   8   |   9   |
                                                                            |       |       |       |
                                                                            +=======================+
"""

    for i in range(1,10):
        if (board[i] == '#put something here for player 1' or board[i] == 'put something here for player 2'):
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
    print(blankBoard)

board = ['#'] * 10

display_board(board)
