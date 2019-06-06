# Elementary Cellular Automata: Animation of the evolution of a single rule.
rule = 166

import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# These are some auxillary functions required to do this.
def max_power_two(integer):

    """ This function inputs an integer (type int) and out puts the max power of
        2 that is less than or equal to the integer
    """

    count = 0
    powerlessthan = True

    while powerlessthan == True:

        if (2 ** (count + 1)) <= integer:
            count = count + 1
        else:
            powerlessthan = False

    return count
def decimal_to_binary(integer):

    """ This function inputs integer (type int) and out puts the binary
        representation (type str)
    """

    binaryrep = ''

    max = max_power_two(integer)

    for i in range(max,-1,-1):

        if (2 ** i) <= integer:
            binaryrep = binaryrep + '1'
            integer = integer - (2 ** i)
        else:
            binaryrep = binaryrep + '0'

    return binaryrep

# Function which realises the automata.
def np_onedim_CA(state, wolf_code):

    '''
        This function takes in a state (type list) consisting of 0s,1s and
        updates the state according to the rules given by wolf_code.

        wolf_code must be an integer [0,255]. These correspond to the coding
        of the one dimensional cellular automata rules defined by Steven
        Wolfram.

        Output = updated state (type list)

    '''

    # Obtain binary representation for the code.
    wolf_code_binary = decimal_to_binary(wolf_code)
    l_code = len(wolf_code_binary)

    # Length of the state
    l_state = len(state)

    # Pad wolf_code_binary to 8bits.
    wolf_code_binary = (8 - l_code)*'0' + wolf_code_binary
    wolf_code_binary = list(wolf_code_binary)

    # Build dictionary to determine the rules.
    wolf_evolultion = { '111': wolf_code_binary[0],
                        '110': wolf_code_binary[1],
                        '101': wolf_code_binary[2],
                        '100': wolf_code_binary[3],
                        '011': wolf_code_binary[4],
                        '010': wolf_code_binary[5],
                        '001': wolf_code_binary[6],
                        '000': wolf_code_binary[7]
                        }

    # This will be the output of the function.
    updated_state = []

    # First cell of the state. Convention: off-end state always 1.
    neighbourhood_start_list = [1,state[0],state[1]]
    neighbourhood_start = ''
    for x in neighbourhood_start_list:
        neighbourhood_start = neighbourhood_start + str(x)
    updated_state.append(int(wolf_evolultion[neighbourhood_start]))



    # Update the interior cells of the state.
    #count = 1
    for i in range(1,l_state-1):
        neighbourhood_interior_list = state[i-1:i+2]
        neighbourhood_interior = ''
        for x in neighbourhood_interior_list:
            neighbourhood_interior = neighbourhood_interior + str(x)
        updated_state.append(int(wolf_evolultion[neighbourhood_interior]))


    # End cell of the state. Convention: off-end state always 1.
    neighbourhood_end_list = [state[l_state-2],state[l_state-1],1]
    neighbourhood_end = ''
    for x in neighbourhood_end_list:
        neighbourhood_end = neighbourhood_end + str(x)
    updated_state.append(int(wolf_evolultion[neighbourhood_end]))

    return updated_state

# Initiate the plot.
fig = plt.figure()
plt.axis('off')

# Set the title of the plot.
plt.title('One Dimensional Cellular Automata: Wolfcode %s' % rule )

# Initiate the list of images used for the animation.
automata = []

# Grid resolution
res = 500

# Create the grid (g) to put the cells in.
x = np.linspace(0,1,res)
y = np.linspace(0,1,res)
g = x[np.newaxis,:] + y[:,np.newaxis]

# Array of zeroes which will eventually be the output to print.
CA = np.zeros(g.shape, dtype=int)

# Random initial state
initial_state = np.random.randint(2, size=res)

# This puts the initial state into the grid.
CA[0] = initial_state

# Now we update the automata list as we generate the automata.
for i in range(1,res):
    CA[i] = list(np_onedim_CA(CA[i-1],rule))
    automata.append(copy.deepcopy(CA))
    # Print current progress.
    print 'Automata iterating Step: %s' % i

image = []
count = 1

for data in automata:
    plt_im = plt.imshow(data, cmap='hot',extent=[-1.5, 1.5, -1, 1], animated = True)
    image.append([plt_im])
    # Print current progress.
    print 'Creating image %s' % count
    count = count + 1


# ArtistAnimation does all of the stiching together of the frames for us.
ani = animation.ArtistAnimation(fig, image, interval = 100, blit=True,
                                repeat_delay=0)
plt.show()
