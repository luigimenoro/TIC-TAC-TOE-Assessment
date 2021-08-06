# array for the instructions
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
   ___________________________      

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
    Each players will take turn to put their element to the grid.  
    The first player to have a consecutive element in a row win.
    """,
    """
    Have Fun…
    """,
]

# class for the text colorizations
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