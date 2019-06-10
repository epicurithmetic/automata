# Two Dimensional Cellular Automaton - John Conway's "Game of Life"
from life_aux import *
import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Aim: run Conway's "Game of Life" and present an animation of the progression.

#       1. Generate the grid on which "Life" takes place.
#       2. Write function to recognise the neighbourhood of a cell (life_aux.py)
#           i. Conway neighbourhood
#          ii. Von-Neumann Neighbourhood
#       3. Write a function which generates particular initial conditions(life_aux.py)
#       4. Figure out how to pass these initial conditions into the grid.


# ----------------------------------------------------------------------------
# The following part of the script generates the grid on which "Life" unfolds.
# ----------------------------------------------------------------------------

# Grid resolution
res = 10

# Create the grid (g) to put the cells in.
x = np.linspace(0,1,res)
y = np.linspace(0,1,res)
g = x[np.newaxis,:] + y[:,np.newaxis]

# This array of zeros will later be given initial conditions more interesting
# than everything being 0 i.e. dead.
CA = np.zeros(g.shape, dtype=int)

# The following lines set up some test initial conditions, the behaviour of
# which are easily determined by hand and so can be used to test the code.

#This puts a "Block" in the top right-hand corner: these are "still-lifes"
CA[1,1] = 1
CA[1,2] = 1
CA[2,2] = 1
CA[2,1] = 1

# This puts a "Blinker" in the top left-hand corner: these are oscillators (2)
CA[1,6] = 1
CA[2,6] = 1
CA[3,6] = 1

#This puts a "beacon" in the grid: another oscillator (2)
CA[4,2] = 1
CA[5,2] = 1
CA[4,1] = 1
CA[5,1] = 1
CA[6,3] = 1
CA[6,4] = 1
CA[7,3] = 1
CA[7,4] = 1

# ----------------------------------------------------------------------------
#        The following part of the script creates the next state.
# ----------------------------------------------------------------------------

life = [CA]
updated_CA = CA
iterations = 0

while iterations < 100:
    updated_CA = ConwayLifeIter(copy.deepcopy(updated_CA))
    life.append(updated_CA)
    iterations += 1

# Commented code just there to check everything worked!

# # Loops to print the moments in a human viewer friendly format.
# for moment in life:
#     # Make the moment printable.
#     moment_print = ConwayLifePrinter(moment)
#     # Print the moments.
#     for x in moment_print:
#         print x

# ----------------------------------------------------------------------------
#        The following part of the script animates moments together.
# ----------------------------------------------------------------------------

life_flow = []

fig = plt.figure(facecolor = 'black')
plt.axis('off')

for moment in life:
    plt_im = plt.imshow(moment, cmap='binary',extent=[-1.5, 1.5, -1, 1], animated = True)
    life_flow.append([plt_im])

ani = animation.ArtistAnimation(fig, life_flow, interval = 1000, blit=True,
                                repeat_delay=0)
plt.show()
