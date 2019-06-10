# Cellular Automata
Code related to the wonderful world of cellular automata.

(1) cellularautomata.py is my first attempt. This script prints in the terminal.
(2) onedimCA_print.py uses matplotlib to output a nicer picture. Allowing for finer resolution.
    Also this second script has two different evolution functions pertaining to different choices for the off-end cells:
       (i) I think it is convention to set the off-end cells to 'alive' i.e. 1. First function does this.
       (ii) But the second function sets the off-end cell equal to the last cell at the opposite end i.e. wraps grid into a                 cylinder.
       
Animations: onedimCA_animation.py produces an animation of all 256 Elementary Cellular Automata each with a different random initial state. Whereas, onedimCA_animationfixedrule.py produces an animation of the evolution of a fixed rule from a random initial state. 

life.py and life_aux.py (together) run John Conway's "Game of Life". Again, it is assumed that off-end cells are all dead. 
            
Jobs to-do:     
                
                i. Write functions which generate interesting initial conditions for life.

               ii. Figure out how to set up initial conditions in an easy manner. 
               
              iii. Dream: Make an app which allows user to click cells on/off in order to define the initial condition. 
              
               iv. Dream: Have the board move with a dynamic part i.e. (effectively) infinite board 

Unfortunately GLaDOS has infected one of my scripts. If she promises you cake, do not believe her. 
