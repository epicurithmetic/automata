# Cellular Automata

# First job: write a function that updates a list according to one
#            of the Wolfram rules.

print '\n'
print 'One-Dimensional Cellular Automata:\n'

# Specify the rule number using Wolfram's code - Integer (0 - 255)
# This is now input by the user in each run.
rule = 90
print '\n'


## Note: Once the code is working, we can ask the user to input the rule they
##       want to see when the script runs.

# These are some auxillary functions used to turn the rule name
# into the corresponding binary string.
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

# Binary string corresponding to the rule
rule_binary = decimal_to_binary(rule)

# In general this will not be 8-bits. So we need to pad the string.
len_rule = len(rule_binary)
rule_binary = (8 - len_rule)*'0' + rule_binary

# We will store the state-update instructions in the following dictionary.
rule_evolultion = { '111': rule_binary[0],
                    '110': rule_binary[1],
                    '101': rule_binary[2],
                    '100': rule_binary[3],
                    '011': rule_binary[4],
                    '010': rule_binary[5],
                    '001': rule_binary[6],
                    '000': rule_binary[7]
                    }

# Print this dictionary in a table to tell the user how the states update.

print 'This table explains how Rule %s updates a state based upon (i) its current state' % rule
print 'and (ii) the state of its immediate neighbours.'
print '-'*63
print '| 111 ||| 110 ||| 101 ||| 100 ||| 011 ||| 010 ||| 001 ||| 000 |'
#print '\n'
print '|  %s  |||  %s  |||  %s  |||  %s  |||  %s  |||  %s  |||  %s  |||  %s  |' % (rule_binary[0],
                                                                                   rule_binary[1],
                                                                                   rule_binary[2],
                                                                                   rule_binary[3],
                                                                                   rule_binary[4],
                                                                                   rule_binary[5],
                                                                                   rule_binary[6],
                                                                                   rule_binary[7]
                                                                                   )
print 'Note: the end points of a finite state will be assumed to have an off-end'
print '      neighbour in state 1.'


# Now we need an initial condition to evolve.
initial_state_1 = '101101001001010101001001'
initial_state_2 = '010010010101010100100100'
initial_state_3 = '111110010000100100010011'
initial_state = initial_state_1 + initial_state_2 + initial_state_3
print '\nThe initial state entered into the automata this time is:'
print initial_state
print 'When we print it we use the identification 0 = *blank* and 1 = #'
print 'This way patterns are easier to discern.'
print '\n'

# Define a function which updates a list according to a Wolfram code.
def onedim_CA(state, wolf_code):

    '''
        This function takes in a state (type string) consisting of 0s,1s and
        updates the state according to the rules given by wolf_code.

        wolf_code must be an integer [0,255]. These correspond to the coding
        of the one dimensional cellular automata rules defined by Steven
        Wolfram.

        Output = updated state (type string)

    '''

    # Obtain binary representation for the code.
    wolf_code_binary = decimal_to_binary(wolf_code)
    l_code = len(wolf_code_binary)

    # Length of the state
    l_state = len(state)

    # Pad wolf_code_binary to 8bits.
    wolf_code_binary = (8 - l_code)*'0' + wolf_code_binary

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
    updated_state = ''

    # First cell of the state. Convention: off-end state always 1.
    neighbourhood_start = '1' + state[0:2]
    updated_state = updated_state + wolf_evolultion[neighbourhood_start]


    # Update the interior cells of the state.
    #count = 1
    for i in range(1,l_state-1):
        neighbourhood_interior = state[i-1:i+2]
        updated_state = updated_state + wolf_evolultion[neighbourhood_interior]


    # End cell of the state. Convention: off-end state always 1.
    neighbourhood_end = state[l_state-2:l_state] + '1'
    updated_state = updated_state + wolf_evolultion[neighbourhood_end]

    return updated_state


# Iterate the update function a number of times. Storing all of the states.
sierpinski = [initial_state]
updated_state = initial_state
iter = 1

while iter < 30:
    updated_state = onedim_CA(updated_state,rule)
    sierpinski.append(updated_state)
    iter += 1

# Massage the states into a form more suitable for human viewing.
sierpinski_printable = []
for state in sierpinski:
    # Need state to be a list to change the entries
    state = list(state)

    for i in range(0,len(state)):
        if state[i] == '0':
            state[i] = ' '
        else:
            state[i] = '#'

    # Put the state back into string to make it easier to print.
    print_state = ''
    for x in state:
        print_state = print_state + x

    sierpinski_printable.append(print_state)

# Print the iterations.
for state in sierpinski_printable:
    print state
