# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:56:04 2017

@author: Sean
"""
high = 100
low = 0
guess = (high + low)//2
found = True
ans = 0
print('Please think of a number between 0 and 100!')
while(found):
    print('Is your secret number', guess)
    direction = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
    if direction == 'l':
        low = guess
    elif direction == 'h':
        high = guess
    elif direction == 'c':
        ans = guess
        found = False
    else:
        print('Sorry I did not understand your input.')
    guess = (high+low)//2
    
print('Game over. Your secret number was: ', ans)
    