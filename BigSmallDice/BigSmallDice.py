import os
import sys
import random 
import time

print("Big or Small Dice Dame")
print("Press any key to start")

system = False

while system == False:
    
    keyInput = input()

    diceA = random.randint(0,6)
    diceB = random.randint(0,6) 
    diceC = random.randint(0,6)

    result = diceA + diceB + diceC
    time.sleep(3)

    if result > 10:
       print(result)
       print("BIG")
       
    else:
       print(result)
       print("SMALL")
       
    print("Press any key to continue")
    strNext = input()
    diceA = diceB = diceC = 0
    os.system("cls")
