# array for the instructions
instructions_array = [
    """
    You are asked to enter you preferred symbol, and you 
    are going to use that symbol throughout the game.
    """,
    """
    Then the game will show a big 3 x 3 grid
    """,
    """
    Where it will ask you where you want to put your 
    chosen symbol to the 3 x 3 grid. 
    """,
    """
    To put your symbol to the 3 x 3 grid, you need to enter the number that 
    corresponds to the spot where you want your symbol to be entered.
    ---------------------------
             |     |     
          1  |  2  |  3 
        _____|_____|_____
             |     |     
          4  |  5  |  6  
        _____|_____|_____
             |     |     
          7  |  8  |  9  
             |     |       
    ---------------------------
    """,
    """
    Each players will take turns putting their symbol to the grid.  
    The first player to have a consecutive element in a row wins.
    ___________________________________________________________

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
    ___________________________________________________________
    """,
    """
    Have Fun playing the game
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