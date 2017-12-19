# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:18:54 2017

@author: kwbatson
"""

userPass = ["Admin", "Basalisk","Groundhog","Football","Rearrange"]

print("Type one from among these: " + str(userPass))

for guessesTaken in range (1,5):
    print("Take a guess.")
    guess = input()
    
    if guess != "Basalisk":
        print("Incorrect.")
    else:
        break
    
if guess == "Basalisk":
    print("Exact match: Granting user access.")
    
else:
    print("SYSTEM SHUTDOWN INNITIATED")
        
