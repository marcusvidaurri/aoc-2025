"""

Advent of Code 2025

--- Day 3: Lobby (Part 2) ---

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
    jolt = '' # placeholder for bank joltage
    m = 0 # how many digits have we found
    pos = 0 # initial search point
    while m < n: # while we still need digits
        #print('searching for digit ' + str(m+1))
        i = pos + 1 # iterate beginning from search point
        while i < len(bank)-n+m+1: # so long as we leave room for further digits
            if int(batteries[i]) > int(batteries[pos]): # if we get new max
                pos = i # hit marker
            i+=1
        jolt += batteries[pos] # add max for that digit search
        #print('jolt so far: ' + jolt)
        pos+=1 # update position
        m+=1

    #print('jolt: ' + jolt) # TEST DATA ONLY
        
    return(int(jolt)) # return jolt rating
        
"""
PROCESS
"""

# Import the battery banks.
banks = np.loadtxt('input3.txt',dtype=str)

total_jolt = 0 # placeholder to store total output joltage
d = 12 # number of batteries (digits) to include

for b in banks: # sort through the banks,
    total_jolt += maxjolt(b,d) # adding max joltage from each

# Return the total output joltage.
print('The total output joltage is: ' + str(total_jolt))
