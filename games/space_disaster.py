from UWIGoPiGo import *
import random
import os
import time
import pygame

timer = 20

init_eyes()

# Dictionary Array containing objects to draw as keys, and the repairs necessary to the ship
lists = [   {'drill':'Hull Breach'},
            {'syringe':'Life Support'},
            {'computer':'Central Processing Unit'},
            {'hexagon':'Solar Panel'},
            {'camera':'Visual Cortex'},
            {'battery':'Power Systems'},
            {'eye':'Sun Shield'}
        ]


correct = 0

# Shuffles the array to make every run randomised
random.shuffle(lists)
# Takes the first 3 elements of the array
run = lists[:3]

#Prints the problems that require fixing in the ship for this run
print ("Warning. Systems Critical.")
for i in run:
    print i.values()

# Iterates through array of objects (errors in ship) for this run
for obj in run:
    # Speaks and prints the required object to fix the ship error
    os.system("espeak -ven+f4 -a200 -p100 -s130 'Draw me a %s You have 10 seconds'" % obj.keys())
    print('Draw me a %s You have 10 seconds' % obj.keys())

    # Speaks countdown
    num = 10
    for i in range(num):
        os.system("espeak -ven+f4 -a200 -p100 -s130 '%d'" % (num-i))
    os.system("espeak -ven+f4 -a200 -p100 -s130 'Okay! Show me what you got!' ")
    print('Okay! Show me what you got!')

    # Captures image and recognises
    snap()
    result, score = see()
    print(result, score)
    os.system("espeak -ven+f4 -a200 -p100 -s130 'You drew a %s ' " % result )
    print('You drew a %s ' % result)

    # If detected object is one of the valid shapes, then the error is fixed
    if result == obj.keys():
        correct+1
        print("Initiating repairs on %s" % obj.values())
        os.system("espeak -ven+f4 -a200 -p100 -s130 'Initiating repairs on %s' " % obj.values() )
    else:
        print("Cannot proceed with repairs.")
        os.system("espeak -ven+f4 -a200 -p100 -s130 'Cannot proceed with repairs.' ")
        sleep(1)

# Checks if the player has managed to correct the errors
if correct >=3:
    os.system("espeak -ven+f4 -a200 -p100 -s130 'You are saved! ' ")
    print('You are saved!')

# Plays explosion sound on game loss
else:
    pygame.mixer.init()
    explosion = pygame.mixer.Sound("sounds/explosion.wav")
    explosion.play()
    time.sleep(4)
    explosion.stop()
    
          
         

