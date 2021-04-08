# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:52:36 2021

@author: Issamu Umeda
"""

import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    even_number = 1
    while even_number % 2 != 0:
        even_number = random.randint(0, 99)
    return even_number

print(genEven())
