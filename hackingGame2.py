# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:18:54 2017

@author: kwbatson
"""
import random

listNumber = random.randint(0,4)


userPass = ["Admin", "Basalisk","Groundhog","Football","Rearrange"]

print("Type one from among these: " + str(userPass))
#while userWish == "Yes":
    for guessesTaken in range (1,5):
        print("Take a guess.")
        guess = input()
    
        if guess != userPass[listNumber]:
            print("Incorrect.")
        else:
            break
    
    if guess == userPass[listNumber]:
        print("Exact match: Granting user access.")
        print ("Would you like to play again?")
        userWish = input()
    
    else:
        print("SYSTEM SHUTDOWN INNITIATED")
        print ("Would you like to play again?")
        userWish = input()

  
 
