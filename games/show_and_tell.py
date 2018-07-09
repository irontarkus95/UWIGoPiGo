from UWIGoPiGo import *
import random
import os
import time

init_eyes()

lists = ["phone", "pen", "water bottle", "glasses"]

rand = random.choice(lists)
os.system("espeak -ven+f3 -a200 -p100 -s130 'Show me a %s'" % rand)
print('Show me a %s' % rand)
snap()
result, score = see()
print(result, score)
os.system("espeak -ven+f4 -a200 -p100 -s130 'You showed me a %s ' " % result )
print('OH! It is a %s ' % result )



