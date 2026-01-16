"""

Advent of Code 2025

--- Day 1: Secret Entrance (Part 2) ---

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

"""
PROCESS
"""

# Begin with dial set to 50.
pos = 50

# Begin counting zeros.
zer=0

# Import list of instructions.
#instruct_str = 'L68L30R48L5R60L55L1L99R14L82' # TEST DATA ONLY
#instruct_lst = list(instruct_str) # TEST DATA ONLY
#instructions = read(instruct_lst) # TEST DATA ONLY
instructions = np.loadtxt('input1.txt',dtype=str)

# For each instruction, rotate the dial
for i in instructions:
    #print(i) # check instruction
    dir = i[0]
    num = int(i[1:])
    if dir == 'L':
        if pos == 0:
            zer -= 1 # account for double counts
        pos = pos - num
        while pos < 0:
            pos = pos + 100
            zer += 1
            #print('crossed zero while moving left! ' + str(zer))
        if pos == 0:
            zer += 1
            #print('reached zero while moving left!: ' + str(zer))
    else:
        pos = pos + num
        while pos > 99:
            pos = pos - 100
            zer += 1
            #print('touched zero while moving right! ' + str(zer))
    #print(pos) # check position

# Return the number of times the dial CLICKS at zero.
print('The password is: ' + str(zer))
