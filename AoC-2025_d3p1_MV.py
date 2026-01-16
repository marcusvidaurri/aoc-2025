"""

Advent of Code 2025

--- Day 3: Lobby (Part 1) ---

User: Marcus Vidaurri

"""

import numpy as np

"""
FUNCTIONS
"""

# Define function to read max joltage from bank.
def maxjolt(bank,n):
    #print(bank) # TEST DATA ONLY
    batteries = [bank[i:i+1] for i in range(0, len(bank), 1)] # split
    pos1 = 0
    i = 1
    while i < len(bank)-n+1: # find first digit (and position)
        if int(batteries[i]) > int(batteries[pos1]):
            pos1 = i
        i+=1

    pos2 = pos1+1
    j = pos2
    while j < len(bank)-n+2: # find next digit (and position)
        if int(batteries[j]) > int(batteries[pos2]):
            pos2 = j
        j+=1
    jolt = batteries[pos1] + batteries[pos2]

    #print('jolt: ' + jolt) # TEST DATA ONLY
        
    return(int(jolt)) # return jolt rating
        
"""
PROCESS
"""

# Import the battery banks.
banks = np.loadtxt('input3.txt',dtype=str)

total_jolt = 0 # placeholder to store total output joltage
d = 2 # number of batteries (digits)

for b in banks: # sort through the banks,
    total_jolt += maxjolt(b,d) # adding max joltage from each

# Return the total output joltage.
print('The total output joltage is: ' + str(total_jolt))
