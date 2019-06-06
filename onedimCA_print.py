# One Dimensional Cellular Automata with numpy and better printing.

# This time we will use numpy to make the grid and matplotlib to do the
# display of the states.
import numpy as np
import matplotlib.pyplot as plt


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

# Grid resolution
res = 1000

# Create the grid (g) to put the cells in.
x = np.linspace(0,1,res)
y = np.linspace(0,1,res)
g = x[np.newaxis,:] + y[:,np.newaxis]

# Array of zeroes which will eventually be the output to print.
CA = np.zeros(g.shape, dtype=int)

# Set the initial state. Update CA to have this as the first row.

# This sets the initial state to have the center call 'alive' and the
# remainder of the cells 'dead'
# list_of_zeroes = [0]*(res/2 - 1)
# initial_state = list_of_zeroes + [1] + list_of_zeroes + [0]

# Random initial state
initial_state = np.random.randint(2, size=res)

# This puts the initial state into the grid.
CA[0] = initial_state

# Now we need to update the remaining states according to the Wolf code:
rule = 109

# We have the function that updates a given state. This has one minor alteration
# compared to the original. We need to turn the input list into a string and
# then back into a list to output it.
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

# Rather than have the 'off-end' cells alive. We can wrap the domain
# into a cylinder by making the 'off-end' cell equal to the cell at
# the other end.
def np_onedim_CA_cylinder(state, wolf_code):

    '''
        This function takes in a state (type list) consisting of 0s,1s and
        updates the state according to the rules given by wolf_code.

        wolf_code must be an integer [0,255]. These correspond to the coding
        of the one dimensional cellular automata rules defined by Steven
        Wolfram.

        This code is different in that it equates the twosides. The 'off-end'
        cells are no longer set equal to 'alive' but equal to the cell
        at the other end. Hence wrapped like a cylinder.

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
    neighbourhood_start_list = [state[l_state-1],state[0],state[1]]
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
    neighbourhood_end_list = [state[l_state-2],state[l_state-1],state[0]]
    neighbourhood_end = ''
    for x in neighbourhood_end_list:
        neighbourhood_end = neighbourhood_end + str(x)
    updated_state.append(int(wolf_evolultion[neighbourhood_end]))

    return updated_state

for i in range(1,res):
    CA[i] = list(np_onedim_CA(CA[i-1],rule))

# Displays the figure. Define title for figure. Saves the figure.
figure = plt.figure(figsize=[15,10])
plt.axis('off')
plt.title('One Dimensional Cellular Automata: Wolfram Code = %s. \nOff Grid = "Alive"' % rule)
plt.imshow(CA, cmap='hot',extent=[-1.5, 1.5, -1, 1])
plt.savefig("CA%s.png" % rule)
plt.show()
