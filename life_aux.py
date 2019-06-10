# Two Dimensional Cellular Automaton - John Conway's "Game of Life"
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Script to store all auxillary functions for running "life".

# ----------------------------------------------------------------------------
#                 Determining the Conway neighourhood.
# ----------------------------------------------------------------------------

# First we need to know the neighbourhood of a cell in order to determine
# how that cell should evolve.

# As with the elementary cellular automaton, we have to make a descion about
# the border rules:
#                   i. Infinite board?
#                  ii. Board wraps into cylinder?
#                 iii. All off-edge cells dead/alive?

def ConwayNeighbourhood(grid, row, col):

    """
        Input: Grid (type nd-array) and row,col are index of an entry in grid.

        Output: Number (type int) of alive cells in Conway neighbourhood.

        Assumptions:
         i. Grid is square i.e. same number of rows and columns.
        ii. Off-grid cells are dead i.e. contribute no live cells.
                    You have reached the edge of the earth...


    """

    dimension_grid = len(grid[0])
    alive_cells = 0

    # First we will check if the cell is in a corner:

    # Top left corner.
    if (row == 0 and col == 0):

        # In this case there are three neighbours.
        alive_cells += (grid[row,col+1] + grid[row+1,col+1] + grid[row+1,col])

    # Top right corner.
    elif (row == 0 and col == (dimension_grid-1)):

        # In this case there are three neighbours.
        alive_cells += (grid[row,col-1] + grid[row-1,col-1] + grid[row-1,col])

    # Bottom left corner.
    elif (row == (dimension_grid-1) and col == 0):

        # In this case there are three neighbours.
        alive_cells += (grid[row-1, col] + grid[row-1,col+1] + grid[row,col+1])

    # Bottom right corner.
    elif (row == (dimension_grid-1) and col == (dimension_grid-1)):

        # In this case there are three neighbours.
        alive_cells += (grid[row,col-1] + grid[row-1,col-1] + grid[row-1,col])


    # Now we will check if a cell is on an edge:

    # Note: we have already dealt with corner cases. So these are edge
    #       cells which are not in the corner.

    # Left hand edge.
    elif (col == 0):

        # This case there are five neighbours.
        alive_cells += (grid[row-1,col]+grid[row-1,col+1]+grid[row,col+1]+grid[row+1,col+1]+grid[row+1,col])

    # Right hand edge.
    elif (col == dimension_grid-1):

        # In this case there are five neighbours
        alive_cells += (grid[row-1,col]+grid[row-1,col-1]+grid[row,col-1]+grid[row+1,col-1]+grid[row+1,col])

    # Now we will check if a cell is on the top or bottom edge of the grid.

    # Top edge.
    elif (row == 0):

        # In this case there are five neighbours.
        alive_cells += (grid[row,col-1]+grid[row+1,col-1]+grid[row+1,col]+grid[row+1,col+1]+grid[row,col+1])

    # Bottom edge.
    elif (row == dimension_grid-1):

        # In this case there are five neighbours.
        alive_cells += (grid[row,col-1]+grid[row-1,col-1]+grid[row-1,col]+grid[row-1,col+1]+grid[row,col+1])

    # The rest of the cells are interior with eight neighbours.

    else:
        # Top neighbours.
        alive_cells += (grid[row-1,col-1] + grid[row-1,col] + grid[row-1, col+1])
        # Botom neighbours.
        alive_cells += (grid[row+1,col-1] + grid[row+1,col] + grid[row+1, col+1])
        # Side neighbours
        alive_cells += (grid[row,col-1] + grid[row,col+1])

    return alive_cells

# ----------------------------------------------------------------------------
#                      Determining the next state.
# ----------------------------------------------------------------------------

# Given an initial square numpy.ndarray we need a function that will out put
# the next state following the rules of Conway's "Life".

def ConwayLifeIter(grid):

    """
        Input: square numpy.ndarray consisting of 0,1.

        Update this array based on the rules of Conway's "Game of Life"

        Output: square numpy.ndarray consisting of 0,1.

    """
    updated_grid = np.zeros(grid.shape, dtype=int)
    dimension_grid = len(grid[0])

    for i in range(0,dimension_grid):

        for j in range(0,dimension_grid):

            if ((grid[i,j] == 1) and (ConwayNeighbourhood(grid,i,j) < 2) ):
                # Fewer than two neighbours, you die.
                updated_grid[i,j] = 0

            elif ( (grid[i,j] == 1) and ( (ConwayNeighbourhood(grid,i,j) == 2) or (ConwayNeighbourhood(grid,i,j) == 3) ) ):
                # Alive with two or three neighbours, you remain alive.
                updated_grid[i,j] = grid[i,j]

            elif ( (grid[i,j] == 1) and (ConwayNeighbourhood(grid,i,j) > 3) ):
                # Alive with more than three neighbours, you die. Over population.
                updated_grid[i,j] = 0

            elif  ( (grid[i,j] == 0) and (ConwayNeighbourhood(grid,i,j) == 3) ):
                updated_grid[i,j] = 1

            else:
                updated_grid[i,j] = grid[i,j]

    return updated_grid

# ----------------------------------------------------------------------------
#                       Terminal Printer of Life
# ----------------------------------------------------------------------------

def ConwayLifePrinter(grid):

    """
        Only used to make checking the functions easier. Normally matplotlib
        will be used to animate the moments together.

        Basically it turns the rows into strings. Moreover, turns the 0 to space
        and turns the 1s to #.

    """

    grid_printable = []

    # Turn each row into a string.
    for row in grid:

        row_printable = ""

        # Turn each element of the row into a space ' ' or a hash '#'.
        for i in row:

            if i == 0:
                row_printable += ' '

            else:
                row_printable += '#'

        grid_printable.append(row_printable)

    return grid_printable

# ----------------------------------------------------------------------------
#                 Creating objects to put into arrays.
# ----------------------------------------------------------------------------

# I hope to have ready made initial states which can easily be
# imbedded into the initial numpy array. This will save having to enter
# each initial state every time I want to use it. 

# Fixed initial conditions.
def hive():

    '''
        The "hive" is known as a "still-life" as it does not change
        according to Conway's rules.
        Output: numpy.ndarray which can be imbedded into an instance of
        "Game of Life".

        Size 3 by 4.

    '''

    hive = np.array([[0,1,1,0],[1,0,0,1],[0,1,1,0]])

    return hive
