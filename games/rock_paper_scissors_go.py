from random import randint
from UWIGoPiGo import *
import random
import os
import time
import pygame

init_eyes()

#create a list of play options
t = ["rock", "paper", "scissors"]
 
#assign a random play to the computer
computer = t[randint(0,2)]
 
for i in range(1):
    os.system("espeak -ven+f4 -a200 -p100 -s130 'Rock, paper, scissors, GO!'")
#best 2 out of 3
    os.system("espeak -ven+f4 -a200 -p100 -s130 '%s!'" % computer)
    snap()
    player, value = see()
    print(player, value)
    if player == computer:
        os.system("espeak -ven+f4 -a200 -p100 -s130 'We tie!'")
    elif player == "rock":
        if computer == "Paper":
            os.system("espeak -ven+f4 -a200 -p100 -s130 'I win!'")
        else:
            os.system("espeak -ven+f4 -a200 -p100 -s130 'Aw good job. You won!'")
    elif player == "paper":
        if computer == "scissors":
            os.system("espeak -ven+f4 -a200 -p100 -s130 'Too bad. You lost!'")
        else:
            os.system("espeak -ven+f4 -a200 -p100 -s130 'Great job. You won!'")
    elif player == "scissors":
        if computer == "rock":
            os.system("espeak -ven+f4 -a200 -p100 -s130 'Aw too bad. You lost!'")
        else:
            os.system("espeak -ven+f4 -a200 -p100 -s130 'Good job. You won!'")
    else:
        os.system("espeak -ven+f4 -a200 -p100 -s130 'Wait a second. We are not playing rock, paper, scissors, %s!'" % player)
    computer = t[randint(0,2)]
