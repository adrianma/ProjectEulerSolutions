# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 00:09:44 2014

@author: adrianma
"""

print 'Adrian Martinez Gomez'
print 'Problem 20 Project Euler'

def Ffactorial(n):
    return n*Ffactorial(n-1) if(n>1) else 1

t100factorial = str(Ffactorial(100))

sResult = 0
for i in t100factorial:
    sResult = sResult + int(i)
    
print 'The result is: ', sResult