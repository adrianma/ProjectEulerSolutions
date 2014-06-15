# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 11:59:58 2014

@author: adrianma
"""

import numpy as np

print 'Adrian Martinez Gomez'
print 'Problem 2 Project Euler'

sNLimit = 4*10^6
vFibNumbers = np.zeros((1,2),np.float128)
vFibNumbers = [1.0,2.0]
sArrIdx = 1
while(vFibNumbers[sArrIdx]<sNLimit):
    vFibNumbers.append(vFibNumbers[sArrIdx]+vFibNumbers[sArrIdx-1])
    sArrIdx = sArrIdx + 1
    
sResult = sum(np.mod(vFibNumbers,2)==0)
print 'The result is: ', sResult
    
    