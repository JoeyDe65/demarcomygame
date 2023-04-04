# File created by: Joey De Marco
'''
1. Two people meet up to play
2. Each player has a choice of 3 options: rock, paper, or scissors
3. On the count of 3 each player puts out an action (paper beats rock, rock beats scissors, scissors beats paper)
4. First person to win 2 out of the 3 matches wins

Game design:

Goals: beat opponent
Rules: Must choose only one option; can only display option after 3 seconds
Feedback: Win or Lose
Freedom: The choice of what option to use

Nouns(variables) and verbs(functions)

Nouns: Rules, Choices, Wins, Losses.
Verbs: The freedom of what to choose, deciding who wins, deciding who looses.

'''

# libraries
import time
from time import sleep
from random import randint

print ("Let's play Rock, Paper, Scissors")
sleep (3)
print ("yo")

choices = ["rock", "paper", "scissors"]

def choose():
    print("get player choice...")
    global user
    user = input("Choose rock paper or scissors")
    # return user
def shoot():
    #computer decides
    print("computer rando decides")

def compare ():
    print("compare choices...")
# function gets user input to play
choose()
print("the user chose "+ user)
#function randomly chooses for computer
shoot()
compare()

print (randint(1.3))

choices0 = ["Wizard", "Thief", "Fighter"]
choices1= ["Rock", "Paper", "Scissors"]
choices2 = ["Lizard", "Spock", "Kirk"]

games = [choices0, choices1, choices2]

my_library = [games]

print("Let's play:")
# print(choices[0])
# print(choices[1])
# print(choices[2])

print(my_library[0])
print(my_library[0][0])
print(my_library[0][0][0])
print(my_library[0][0][0][0])

sleep(1)

# allow user to choose something
def choose():
    print("get player choice...")
    global user
    user = input("Choose rock paper or scissors")
    # return user


# cpu_randchoice
def cpu_randchoice():
    # computer decides
    print("computer randomly decides...")
    return choices0[randint(0,2)]
x = 5
y = 12

def compare():
    cpu = cpu_randchoice()
    print("the computer chose", cpu)
    # user = "Rock"
    cpu = "Scissors"
    if user == cpu:
        print("you tied")
    elif user.upper() == "ROCK" and cpu == "Scissors":
        print("you won!!!")
    # elif user == "Paper" and cpu == "Rock":
    #     print("you won!!!")
    # elif user == "Scissors" and cpu == "Paper":
    #     print("you won!!!")
    # elif cpu == "Rock" and user == "Scissors":
    #     print("you lost!!!")
    # elif cpu == "Paper" and user == "Rock":
    #     print("you lost!!!")
    # elif cpu == "Scissors" and user == "Paper":
    #     print("you lost!!!")
    else:
        print("$$$$ an error occured $$$$")


    print("compare choices...")
# function gets user input to play
choose()
print("the user chose " + user)
# function randomly chooses for computer
compare()