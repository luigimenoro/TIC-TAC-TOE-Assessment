# Component 10 for TIC TAC TOE
# To do:
"""
1. Make a function that clears the terminal 
"""
import os

# function that clears the terminal 
def clear():
	os.system("cls")
	print("the terminal has been cleared")



print("JIAWJFWIASKJFASKJFKJFASIFJSALKFSLGHWOOF")
print("JIAWJFWIASKJFASKJFKJFASIFJSALKFSLGHWOOF")
print("JIAWJFWIASKJFASKJFKJFASIFJSALKFSLGHWOOF")
print("JIAWJFWIASKJFASKJFKJFASIFJSALKFSLGHWOOF")
print("JIAWJFWIASKJFASKJFKJFASIFJSALKFSLGHWOOF")
    
# asking the user if they want to clear the terminal for component testing only
keep_going =  input("\nDo you want to clear the terminal: ")

if keep_going == "yes":
 clear()
