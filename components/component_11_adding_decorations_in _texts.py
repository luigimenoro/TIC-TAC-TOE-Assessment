# Component 11 for TIC TAC TOE
# To Do
'''
1. Create a class that contains 
'''

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# for component testing I will ask the user what colour they want the message to be in 
keep_going = ""
while keep_going != "xxx":

    # ask ther user what colour they want the text to be in
    colour = input("What colour do you want the text to be in <red>, <white>, <green>, <yellow>, <purple>, <cyan>: ")

    colour.upper()

    # to change white to bold
    if colour == "WHITE":
        colour == "BOLD"

    # ask what sentence they want to change the colour:
    sentence = input("Please type a sentence: ")

    # to do the magic
    print(color.RED + str(sentence) + color.END).format(sentence)