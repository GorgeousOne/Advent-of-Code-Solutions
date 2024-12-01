'''--- regexes ---'''
import re
match = re.search(r'hello', 'hello world')
nums = [int(x) for x in re.findall(r'\d+', '12 23 34 45')]
replace = re.sub(r"cats|dogs", "animals", "i love cats and dogs")
print(match, nums, replace)


'''--- default dict (lambda) ---'''
from collections import defaultdict
d = defaultdict(lambda: 7)
print(d[4])
print(d)


'''--- graph visualization ---'''
import graphviz
# g = graphviz.Graph(format='png', engine='neato') # no arrows
g = graphviz.Digraph(format='png', engine='neato')
g.node('A', 'King Arthur')
g.node('B', 'Sir Bedevere the Wise')
g.edge('B', 'A')

#g.save('g.dot')
g.render('circle', format='png')
g.view()


'''--- priority queue ---'''
import priority_queue as pq
q = pq.PriorityQueue()
q.add_task("asdf", 1)
q.add_task("ghij", 0)
print(q.pop_task())
print(q.pop_task())


'''--- formula solving ---'''
import z3
x, y = z3.Ints('x, y')
# z3.simplify
eq1 = x + y == 12
eq2 = 2 * x == y

solver = z3.Solver()
solver.add(eq1, eq2)
if solver.check() == z3.sat:
	print(solver.model())