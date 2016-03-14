import sys
from userfile import initial_position, primitive, gen_moves, do_moves

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

