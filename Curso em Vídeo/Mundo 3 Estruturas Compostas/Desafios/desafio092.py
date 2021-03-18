# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:05:17 2021

@author: Issamu Umeda
"""
from datetime import date

person = {}
person['name'] = input('Name: ')
person['age'] = date.today().year - int(input('Year of Birth: '))
person['work_permit'] = int(input("Work Permit (0 if you don't have): "))
if person['work_permit'] != 0:
    person['hiring_year'] = int(input('Hiring Year: '))
    person['salary'] = float(input('Salary: R$'))
    person['retirement'] = person['age'] + ((person['hiring_year'] + 35) - date.today().year)
print('-=' * 15)
for keys, values in person.items():
    print('  - {} has the value of {}'.format(keys, values))
