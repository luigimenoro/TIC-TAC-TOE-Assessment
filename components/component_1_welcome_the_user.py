# Component 2 for TIC TAC TOE
# To Do
'''
1. Welcome the user by showing the ascii art that you made
2. Call the notepad that has the ascii text within it
3. Print the ascii text
'''

f = open ('Welcome to tictactoe ascii.txt', "r")

# Ask the user if they want to play tic tac toe (for component testing only)
ask_user = " "
while ask_user != "xxx":
    ask_user = input("Do you want to play TIC TAC TOE: ")
    ask_user.lower()
    if ask_user == "yes":
        print(''.join([line for line in f]))

