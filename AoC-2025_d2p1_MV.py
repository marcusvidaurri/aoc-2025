"""

Advent of Code 2025

--- Day 2: Gift Shop (Part 1) ---

User: Marcus Vidaurri

"""

import numpy as np

"""
PROCESS
"""

# Import the product ID ranges.
ranges = np.loadtxt('input2.txt',dtype=str,delimiter=',',)
products = [] # placeholder for complete list of IDs (may not be necessary)

# Separate all product IDs and scan for invalid IDs.
invalid_total = 0
for r in ranges:
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
        if len(IDs) % 2 == 0: # check product IDs of even length
            hl = int(len(IDs) / 2) # half the length of the ID
            fh = IDs[0:hl] # first half of the ID
            sh = IDs[hl:] # second half of the ID
            if fh == sh: # check for repeat sequences
                #print('Invalid ID found: ' + IDs) # TEST DATA ONLY
                invalid_total += ID # add to tally
        i += 1
    #print(r); print(IDstart); print(IDend); print(di) # TEST DATA ONLY

#print(products) # TEST DATA ONLY

# Return the sum of invalid IDs.
print('The sum of the invalid IDs is: ' + str(invalid_total))
