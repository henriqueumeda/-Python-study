# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:12:27 2021

@author: Issamu Umeda
"""

import pylab as plt

def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1 + mRate) + monthly]
    return base, savings

def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel+rateLabel, label = 'retire:'+str(monthly)+
                     ':'+str(int(rate*100)))
            plt.legend(loc = 'upper left')

monthlies = [500, 700, 900, 1100]
rates = [.03, .05, .07]
terms = 40*12
displayRetireWMonthsAndRates(monthlies, rates, terms)
