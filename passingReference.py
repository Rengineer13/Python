# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:16:51 2017

@author: kwbatson
"""

def eggs(someParameter):
    someParameter.append("Hello")
    
spam = [1,2,3]
eggs(spam)
print(spam)