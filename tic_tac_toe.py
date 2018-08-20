#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 17:37:32 2018

@author: sabbir
"""

board = {'topL': ' ', 'topM': ' ', 'topR': ' ', 'midL': ' ', 'midM': ' ', 'midR': ' ', 'botL': ' ', 'botM': ' ', 'botR': ' '}

def printboard(board):
    print(board['topL'], ' | ', board['topM'], ' | ', board['topR'])
    print('=-=-=-=-=-=-=-')
    print(board['midL'], ' | ', board['midM'], ' | ', board['midR'])
    print('=-=-=-=-=-=-=-')
    print(board['botL'], ' | ', board['botM'], ' | ', board['botR'])
    
    
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
    

turn = 'X'

for i in range(9):
    printboard(board)
    if i > 4:
        if is_winner(board):
            if turn == 'X':
                winner = 'O'
            else:
                winner = 'X'
            print('{} wins the game!'.format(winner))
            break
    print('Turn for ' + turn + '. ' + 'Which place? ')
    place = input()
    board[place] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
else:
    printboard(board)
    print('The match is drawn!')

