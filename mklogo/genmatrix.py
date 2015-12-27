#!/usr/bin/env python



matrix = '['
while True:
    pointXY = raw_input('Enter XY: ')
    if pointXY == 'e':
        matrix = matrix[:-1]+']' 
        break
        
    pointX = pointXY[0]
    pointY = pointXY[1]
    point = pointX + ',' + pointY
    if (pointX.strip() != 'exit') or (pointY.strip() != 'exit'):
        matrix += ('('+point+'),')
    else:
        matrix = matrix[:-1]+']'
        break

print matrix
