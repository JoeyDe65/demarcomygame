# File created by: Joey De Marco
'''
Write out the steps needed for two people to play
ROCK PAPER SCISSORS....

Game design:

Goals
Rules
Feedback
Freedom

Nouns and verbs

Nouns
Player choice
Choices: rock paper and scissors

Verbs
decide who wins

'''

# libraries
from time import sleep
from random import randint

choices0 = ["Rock", "Paper", "Scissors"]

print("Let's play:")

for i in choices0:
    print(i)

sleep(1)

# allow user to choose something
def choose():
    # global allows for the variable user to be used outside the choose function
    global user
    user = input("Choose rock paper or scissors")
    print("the user chose " + user)


def cpu_randchoice():
    print("computer randomly decides...")
    return choices0[randint(0,2)]

def compare():
    cpu = cpu_randchoice()
    print("the computer chose", cpu)
    user = "Rock"
    cpu = "Scissors"
    if user == cpu:
        print("you tied")
    elif user.upper() == "ROCK" and cpu == "Scissors":
        print("you won!!!")
    elif user.upper() == "PAPER" and cpu == "Rock":
        print("you won!!!")
    elif user == "Scissors" and cpu == "Paper":
        print("you won!!!")
    elif cpu == "Rock" and user == "Scissors":
        print("you lost!!!")
    elif cpu.upper() == "PAPER" and user == "Rock":
        print("you lost!!!")
    elif cpu == "Scissors" and user == "Paper":
        print("you lost!!!")
    else:
        print("$$$$ an error occured $$$$")
# function gets user input to play
choose()
# function randomly chooses for computer
compare()