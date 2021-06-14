# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:56:53 2021

@author: Issamu Umeda
"""

import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10


def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    even_number = 1
    while even_number % 2 != 0:
        even_number = random.randint(10, 20)
    return even_number
