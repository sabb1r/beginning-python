#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 17:37:32 2018

@author: sabbir
"""
# %% Data Structre

import random

board = {'topL': ' ', 'topM': ' ', 'topR': ' ', 'midL': ' ', 'midM': ' ', 'midR': ' ', 'botL': ' ', 'botM': ' ', 'botR': ' '}

positions = ['topL', 'topM', 'topR', 'midL', 'midM', 'midR', 'botL', 'botM', 'botR']
corner_positions = ['topL', 'topR', 'botL', 'botR']

c_position = []
u_position = []

# %% Output Section

def printboard(board):
    print('\n')
    print(board['topL'], ' | ', board['topM'], ' | ', board['topR'])
    print('=-=-=-=-=-=-=-')
    print(board['midL'], ' | ', board['midM'], ' | ', board['midR'])
    print('=-=-=-=-=-=-=-')
    print(board['botL'], ' | ', board['botM'], ' | ', board['botR'])
    print('\n')
    
# %% Winner Detection 

def is_winner(board):
    for text in ['top', 'mid', 'bot']:
        if board[text + 'L'] == board[text + 'M'] == board[text + 'R'] != ' ':
            return True
    for text in ['L', 'M', 'R']:
        if board['top' + text] == board['mid' + text] == board['bot' + text] != ' ':
            return True
    if board['topL'] == board['midM'] == board['botR'] != ' ':
        return True
    elif board['topR'] == board['midM'] == board['botL'] != ' ':
        return True
    else:
        return False
# %% Check whether a position is empty or not
       
def is_empty(position):
    if board[position] != ' ':
        return False
    else:
        return True
     
# %% Choice Section

def critical_position(position):
     for text1 in ['top', 'mid', 'bot']:
          counter = 0
          for text2 in ['L', 'M', 'R']:
               if text1 + text2 in position:
                    counter += 1
          if counter == 2:
               if text1 + 'L' not in position:
                    if board[text1 + 'L'] == ' ':
                         return text1 + 'L'
               elif text1 + 'M' not in position:
                    if board[text1 + 'M'] == ' ':
                         return text1 + 'M'
               else:
                    if board[text1 + 'R'] == ' ':
                         return text1 + 'R'
     for text2 in ['L', 'M', 'R']:
          counter = 0
          for text1 in ['top', 'mid', 'bot']:
               if text1 + text2 in position:
                    counter += 1
          if counter == 2:
               if 'top' + text2 not in position:
                    if board['top' + text2] == ' ':
                         return 'top' + text2
               elif 'mid' + text2 not in position:
                    if board['mid' + text2] == ' ':
                         return 'mid' + text2
               else:
                    if board['bot' + text2] == ' ':
                         return 'bot' + text2 
     counter = 0
     if 'topL' in position:
          counter += 1
     if 'midM' in position:
          counter += 1
     if 'botR' in position:
          counter += 1
     if counter == 2:
          if 'topL' not in position:
               if board['topL'] == ' ':
                    return 'topL'
          if 'midM' not in position:
               if board['midM'] == ' ': 
                    return 'midM'
          else:
               if board['botR'] == ' ':
                    return 'botR'
     counter = 0
     if 'topR' in position:
          counter += 1
     if 'midM' in position:
          counter += 1
     if 'botL' in position:
          counter += 1
     if counter == 2:
          if 'topR' not in position:
               if board['topR'] == ' ':
                    return 'topL'
          if 'midM' not in position:
               if board['midM'] == ' ':
                    return 'midM'
          else:
               if board['botL'] == ' ':
                    return 'botL'
     
         
# %% Main Code

print('First player will play for "X", while the second player will play for "O"')     
player = input('Who will play first? (type "c" for computer or "u" for you): ')
#firstPlayer = 'c'
     
turn = 'X'

for i in range(9):
    printboard(board)
    
# Computer Choice Section
    if player == 'c':
         
        choiceNo = len(c_position) + 1
        critical_u = critical_position(u_position)
        critical_c = critical_position(c_position)
        
        if choiceNo == 1 and i != 0 and is_empty('midM'):
            place = 'midM'
        else:
            if critical_c:
                 place = critical_c
            else:
                 if critical_u:
                      place = critical_u
                 elif not corner_positions:
                      place = random.choice(positions - c_position - u_position)
                 else:
                      place = random.choice(corner_positions)
                
        if place in corner_positions:
             corner_positions.remove(place)
        c_position.append(place)
        print('Computer has made its choice as below: ')
        player = 'u'
# User Choice Section
    else:
        print('Turn for ' + turn + '. ' + 'Which place? ')
        place = input()
        if place in corner_positions:
             corner_positions.remove(place)
        u_position.append(place)
        player = 'c'
    if i >= 4:
        if is_winner(board):
            if turn == 'X':
                winner = 'O'
            else:
                winner = 'X'
            printboard(board)
            print('{} wins the game!'.format(winner))
            break     
    
    board[place] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
else:
    printboard(board)
    print('The match is drawn!')

