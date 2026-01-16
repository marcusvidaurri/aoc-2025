"""

Advent of Code 2025

--- Day 2: Gift Shop (Part 2) ---

User: Marcus Vidaurri

"""

import numpy as np
import math as m

"""
FUNCTIONS
"""

# Define function to check for invalid IDs.
def check(ids):
    l = len(ids)
    n = 0
    if l % 2 == 0: # even
        while n < l/2: # check each up to half
            split = [ids[i:i+n+1] for i in range(0, len(ids), n+1)] # split ID
            #print(split) # TEST DATA ONLY
            j = 1
            while j < len(split): 
                if split[j] == split[0]: # if elements match the base
                    #print('match!')  # TEST DATA ONLY
                    if j == len(split)-1: # if we've checked all elements
                        #print('invalid!')  # TEST DATA ONLY
                        return(int(ids)) # return invalid ID
                    j+=1
                else:
                    #print('break!')  # TEST DATA ONLY
                    break
            n+=1
            
    else: # odd
        while n < m.floor(l/2): # check each up to half
            split = [ids[i:i+n+1] for i in range(0, len(ids), n+1)] # split ID
            #print(split) # TEST DATA ONLY
            j = 1
            while j < len(split): 
                if split[j] == split[0]: # if elements match the base
                    #print('match!') # TEST DATA ONLY
                    if j == len(split)-1: # if we've checked all elements
                        #print('invalid!')  # TEST DATA ONLY
                        return(int(ids)) # return invalid ID
                    j+=1
                else:
                    #print('break!')  # TEST DATA ONLY
                    break
            n+=2
    return(0)

"""
PROCESS
"""

# Import the product ID ranges.
ranges = np.loadtxt('input2.txt',dtype=str,delimiter=',',)
products = [] # placeholder for complete list of IDs (may not be necessary)

# Separate all product IDs and scan for invalid IDs.
invalid_total = 0
for r in ranges:
    #print(r) # TEST DATA ONLY
    i = 0
    while i < len(r): # search range for dash
        if r[i] == '-':
            di = i
        i += 1
    IDstart = int(r[0:di]) # first ID in range
    IDend = int(r[(di+1):]) # last ID in range
    n = IDend - IDstart
    i = 0
    while i < n+1: # scan each ID in range
        ID = IDstart + i
        products.append(ID) # add to complete list of IDs (may not be necessary)
        IDs = str(ID)
        invalid_total += check(IDs) # check individual ID string
        i += 1

# Return the sum of invalid IDs.
print('The sum of the invalid IDs is: ' + str(invalid_total))
