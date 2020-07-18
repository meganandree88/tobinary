'''
File name: tobinary.py
Homework #4
Problem #2
This file provides the necessary functions to convert a decimal number (base-10)to the binary number (base-2). 
'''

import math

def toBinary(num):
    '''
    This function takes a decimal number and converts it to a binary number. The binary number is returned as a string. 
    This function has one input: num
    This function has one output: acc
    '''
    acc = ''
    binaryNum = ''
    
    if num == 0:
        acc = '0'
    else:
        numLoop = int((math.log2(num)) + 1) #calculates the number of characters needed to represent the decimal number
        for n in range(0, numLoop):
            if isOdd(num):
                acc = '1' + acc
            else:
                acc = '0' + acc
            num = num // 2
            
    return acc

def isOdd(num):
    '''
    This function determines if the decimal number is odd or even. 
    This function has one input: num
    This function has one output: False or True
    '''
    if num % 2 == 0:
        return False
    else:
        return True

def main():

    print('The numbers 0-32 written in binary:')
    print('///////////////////////////////////')
    for num in range(33): #prints out the binary numbers for the numbers 0-32
        print(num, 'in binary is',toBinary(num)) #calls the toBinary function


main()
