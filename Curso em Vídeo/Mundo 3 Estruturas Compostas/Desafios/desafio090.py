# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 22:20:01 2021

@author: Issamu Umeda
"""
student = {}
student['name'] = input('Name: ')
student['average'] = float(input('Average of {}: '.format(student['name'])))
if student['average'] >= 7:
    student['situation'] = 'Approved'
elif student['average'] >= 5:
    student['situation'] = 'Retake'
else:
    student['situation'] = 'Reproved'
print('-=' * 15)

for key, value in student.items():
    print('   - {} is {}'.format(key, value))
