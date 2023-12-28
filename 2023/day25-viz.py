# https://adventofcode.com/2023/day/25

import re
import numpy as np
import graphviz
import math


graph = graphviz.Graph(format='png', engine='neato')

with open("day25_input copy.txt") as file:
# with open("day25_input.txt") as file:
	text = file.read().splitlines()

parts = set()
edges = set()

for i, line in enumerate(text):
	part, cons = line.split(": ")
	cons = cons.split(" ")
	parts.add(part)
	graph.node(part, part)

	for con in cons:
		parts.add(con)
		edges.add((part, con))

size = 0.3 * len(parts) / (2*math.pi)
angle = 2 * math.pi / len(parts)

for i, part in enumerate(parts):
    current = i * angle
    x = size * math.cos(current)
    y = size * math.sin(current)
    graph.node(part, part, pos=f'{x},{y}!')

for edge in edges:
	start, end = edge
	graph.edge(start, end)

graph.save('circle_graph.dot')
graph.render('circle', format='png')
graph.view()