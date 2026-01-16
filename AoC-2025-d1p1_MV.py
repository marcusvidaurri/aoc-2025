"""

Advent of Code 2025

--- Day 1: Secret Entrance (Part 1) ---

User: Marcus Vidaurri

"""

import numpy as np

"""
FUNCTIONS
"""

"""
# Define function to READ the list of instructions. TEST DATA ONLY
def read(ins):
    instructions = []
    count = 0
    for i in ins:
        if i == 'L' or i == 'R': #check for new instruction
            if count != 0:
                instructions.append(string) #add string at onset of new instruction
            string = i #begin new string
        else:
            string = string + i #write string
        count += 1
    instructions.append(string) #add final string
    return(instructions)
"""

# Define function to ROTATE the safe given an instruction to do so.
def rotate(inst, p):
    dir = inst[0]
    num = int(inst[1:])
    if dir == 'L':
        p = p - num
    else:
        p = p + num
    while p < 0:
        p = p + 100
    while p > 99:
        p = p - 100
    return p

"""
PROCESS
"""

# Begin with dial set to 50.
pos = 50

# Begin counting zeros.
zer=0

# Import list of instructions.
#instruct_str = 'L168L330R948L1005R60L55L1L99R14L82' # TEST DATA ONLY
#instruct_lst = list(instruct_str) # TEST DATA ONLY
#instructions = read(instruct_lst) # TEST DATA ONLY
instructions = np.loadtxt('input.txt',dtype=str)

# For each instruction, rotate the dial
for i in instructions:
    #print(i) # check instruction
    pos = rotate(i,pos) # update position after rotation
    #print(pos) # check position
    if pos == 0:
        zer += 1 # tally the number of times the dial is set to zero
        #print('zero counted: ' + str(zer)) # signal zeros

# Return the number of times the dial is set to zero.
print('The password is: ' + str(zer))
