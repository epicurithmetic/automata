### Cellular Automaton

In this repository I have code which implements one-dimensional and two-dimensional cellular automaton. This includes notes which could be used to learn what these automaton are. 

---

#### Elementary Cellular Automata

Elementary (one-dimensional) cellular automata are are completely classified by Stephen Wolfram using the *Wolfram code* for elementary automaton code. Since the evolution of a state depends on its current state and that of its two direct neighbours, this yields eight evolution possibilities.

**

Example: Consider the case that a cell dies when it and both of its neighbours are alive, and otherwise lives (or comes alive). This can be represented with the following table.  

                              | 111 ||| 110 ||| 101 ||| 100 ||| 011 ||| 010 ||| 001 ||| 000 |
                              |  0  |||  1  |||  1  |||  1  |||  1  |||  1  |||  1  |||  1  |

Notice it takes a binary string of length eight to specify each of the evolution rules i.e. a binary number of maximum length eight. This shows that there are 8^2 = 256 possible elementary cellular automaton. This example corresponds to Wolfram code = 127.

Note: The Wolfram code for classification uses the table in the order given in this example. 

**

##### How does this code work

Terminal Printing: Given an initial binary string this code updates the string based on a number (i.e. Wolfram code) between 0 - 255. Storing each iteration in a list. When all of the iterations are completed they are printed in the terminal under the map 0 = ' _ ' and 1 = ' # '. This does not make for high resolution images, but the complex structures of these automaton are still visible with this printing choice. (cellularautomata.py)

PyPlot Printing: This uses the same algorithm to generate the data, but uses bitmap imaging and matplotlib/pyplot to make higher resolution images of the automaton. (onedimCA_print.py)

![Elementary Automaton 90](https://github.com/epicurithmetic/automata/blob/master/CA90_cylinder.png)

Notice: for the choice of initial conditions of one alive cell in the center and rest the rest dead this process (Wolfram code 90) gives the famous fractal known as the *Sierpinksi triangle*.

PyPlot Animations: Further to the higher resolution of images, matplotlib is employed to animate the processes. This yields mp4s which show the update process. (onedimCA_animation.py)

 ![Elementary Automaton 90](https://github.com/epicurithmetic/automata/blob/master/elementary%20automata%20animations/CA_Rule90'.mp4)

---

#### Two Dimensional Cellular Automata: Conway's Game of Life

We have seen that there are only finitely many (256) elementary automaton. Moving up one dimension to two dimensional automaton opens us up to infinitely many possibilities. My code considers only one of these inifinite possibilities; the automaton called *Conway's Game of Life*, often referred to simply as **Life**.

##### Update Rules for Life


##### Examples 


##### Further Tasks to Complete



