"""

Advent of Code 2025

--- Day 4: Printing Department (Part 2) ---

User: Marcus Vidaurri

"""

"""
FUNCTIONS
"""

"""
star = grid[j][i]
one = grid[j-1][i-1]
two = grid[j-1][i]
three = grid[j-1][i+1]
four = grid[j][i-1]
five = grid[j][i+1]
six = grid[j+1][i-1]
seven = grid[j+1][i]
eight = grid[j+1][i+1]
"""

# Define function to locate adjacent spaces on the shelves
def locate(grid,j,i):

    adj = ''
    adj += grid[j-1][i-1] # one
    adj += grid[j-1][i] # two
    adj += grid[j-1][i+1] # three
    adj += grid[j][i-1] # four
    adj += grid[j][i+1] # five
    adj += grid[j+1][i-1] # six
    adj += grid[j+1][i] # seven
    adj += grid[j+1][i+1] # eight

    return(adj)

# Define function to grab rolls and replace grid
def replace(grid,a_r):
    
    ng = [['.']*n for i in range(m)] # new grid
    r = 0 # rolls counted in this round
    
    j = 0
    while j < m:
        i = 0
        while i < n:
            if grid[j][i] == '@': # if the element is a roll
                a = 0 # begin counting adjacent rolls
                k = 0
                adj = locate(grid,j,i)
                while a < a_r and k < len(adj):
                    if adj[k] == '@':
                        a += 1
                    k+=1
                if a < a_r:
                    #print('a=' + str(a) + ' at ' + str(j) + ',' + str(i))
                    ng[j][i] = 'x'
                    r+=1
                else:
                    ng[j][i] = grid[j][i]
            i+=1
        j+=1

    return(ng, r)
        
"""
PROCESS
"""

# Import the shelves of paper.
with open('input4.txt') as file:
    grid = [line.strip() for line in file.readlines()]
    grid = ["." * len(grid[0])] + grid + ["." * len(grid[0])]
    grid = ["." + row + "." for row in grid]

""" Visualize grid - TEST DATA ONLY
for g in grid:
    print(g)
"""

m = len(grid) # rows
n = len(grid[0]) # columns
a_r = 4 # condition for accessibility
rolls = 0 # roll count

nr = 1 # new rolls (only to enter loop)

# Read each element of the grid, updating grid after each round
while nr != 0: # while we find new rolls
    nr = 0
    grid, nr = replace(grid,a_r) # replace grid & grab new rolls
    #print('Rolls this round: ' + str(nr)) # TEST DATA ONLY
    rolls += nr
    """ # Visualize new rolls - TEST DATA ONLY
    for g in grid:
        row = ''
        for i in range(len(g)):
            row += g[i]
        print(row)
    """

# Return the number of rolls accessible by forklift.
print('The total number of accessible rolls is: ' + str(rolls))
