# Component 4 for TIC TAC TOE
'''
To do:
--------------------------------------------------------------------------------------------
1.  Ask the player 1 for their name. Store the name into a variable called player_1name. 
2. After asking player 1 for their name, used that name to ask for their preffered element that is going 
to be used throughout the game

3. Then ask player 2 for their name. Check if player 2's name is not the same as player 1. If
not then store the name to play_2name. 
4. After asking player 2 for their name, used that name to ask for their preffered element. Check if the 
element is not the same as player 1. If so, then ask them again until Player 2 enters a new element. 
to be used throughout the game
---------------------------------------------------------------------------------------------
'''
# array to put the players names and also to check.
names = []
# array for the players' element
elements = []

# this is the main routine
# while loop just for component testing only

# function to ask players for their name and their preffered element
def asking_name(n):
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


asking_name(1)

# to show the arary for component testing only
#printing the array
print("\n")
print("The name array is: ") 
for i in names:
    print(i, end = ' ')

print("\n")

#printing the array
print("The element array is : ")
for i in elements:
    print(i, end = ' ')