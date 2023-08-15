from random import *
import time


def winner():
    if player[0].casefold() == "r" and com[0].casefold() == "s":
        return player
    elif player[0].casefold() == "p" and com[0].casefold() == "r":
        return player
    elif player[0].casefold() == "s" and com[0].casefold() == "p":
        return player
    elif player[0].casefold() == com[0].casefold():
        return " DRAW ".center(50, "=")
    return com


print("Hi! Welcome to play Rock-Paper-Scissors\n")
rps = ["ROCK", "PAPER", "SCISSORS"]
playername = input("Enter your NAME --> ")
print("The GAME Starts in..")
# counter
for i in range(3, -1, -1):
    time.sleep(1)
    print(i, sep=" --> ")
print("Lets start...".center(50))
cont = ""
while cont == "":
    # actual process
    print()
    time.sleep(0.5)
    print("ROCK..", end="\n")
    time.sleep(0.5)
    print("PAPER..", end="\n")
    time.sleep(0.5)
    print("SCISSORS..!!")
    com = choice(rps)
    player = input("Enter yours : ")
    while player[0].casefold() not in "rps":
        print("At least enter the FIRST LETTER of your Choice Try Again !!")
        player = input("Enter yours : ")
    print(f'Computer chose {com}')
    if winner() is player:
        print(f" {playername} WON ".center(50, "-"))
    elif winner() is com:
        print(" Computer WON ".center(50, "-"))
    else:
        print(winner())
    cont = input("Press Enter to CONTINUE or Anything to EXIT ---> ")
