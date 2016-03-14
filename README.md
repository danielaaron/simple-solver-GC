# simple-solver-GC
*Simple solver for non-looping games*

**User Input:**
To input the three given functions and the initial position,
users should write a userfile.py, in the same directory as
this file, containing the four given user inputs. Be sure to
follow the data types below. 

**Data Types:** (f: input --> output)

initial_position: string

primitive(pos): string --> "win", "loss", "tie"

gen_moves(pos): string --> list

do_moves(pos, move): string --> string 

**Notes:**
> Game states are always strings.

> gen_moves must generate all possible
  choices of the opponent and return only the 
  gamestates in which it's the user's move.
  
> This solver can't handle looping games.

