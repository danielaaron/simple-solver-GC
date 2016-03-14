import sys
from userfile import initial_position, primitive, gen_moves, do_moves

"""
Data Types (f: input --> output):
initial_position: string
primitive(pos): string --> "win", "loss", "tie"
gen_moves(pos): string --> list
do_moves(pos, move): string --> string 

Notes:
> Game states are always strings
> gen_moves must generate all possible
  choices of the opponent and return only the 
  gamestates in which it's the user's move
> This solver can't handle looping games

User Input: 
To input the three given functions and the initial position,
users should write a userfile.py, in the same directory as
this file, containing the four given user inputs. 
"""



def solve(parents):
	children = []
	
	# generate all children of parents;
	# end if one is a win, remember ties,
	# exclude primitives from being parents next
	for p in parents: 
		moves = gen_moves(p) 
		for m in moves:
			d = do_moves(p,m) 
			if primitive(d) == "win":
				print "win"
				sys.exit()
			elif primitive(d) == "tie":
				ties.append(d)
			elif primitive(d) != "loss":
				children.append(d)

	# if children, make them parents
	# no children -> primitives reached 
	if children:
		solve(children)
	elif not children:
		if ties:
			print "tie"
		else:
			print "loss"

#### ---- ####

parents = [initial_position]
ties = []

solve(parents)

