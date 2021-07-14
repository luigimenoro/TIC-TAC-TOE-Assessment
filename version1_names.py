

p1_name = input("Player 1 what is your name?")
p2_name = input("Player 2 what is your name")

names = [p1_name, p2_name]

keep_going = ""
n = 0
while keep_going != "xxx":
    keep_going = input("please press <enter>")
    if keep_going == "":
        print("It is player {} turn".format(names[n]))
    n += 1
    if n == 2:
        n = 0


while keep_going != "pop":
    lol = input("please select a space")
    if lol == "":
        print("you have to be kidding me")


