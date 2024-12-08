"""
https://adventofcode.com/2024/day/8
Create all possible pairs of 2d positions of antennas with the same letter in the input.
List all their antinodes reoccuring on the line of each pair that are still inside the field.
"""
from collections import defaultdict
import numpy as np

# with open("08test.txt", "r") as f:
with open("08input.txt", "r") as f:
	t = f.read().splitlines()

w, h = len(t[0]), len(t)
ants = defaultdict(list)

def in_range(p):
	return (p[0] >= 0 and p[0] < w and
		 p[1] >= 0 and p[1] < h)

for y, l in enumerate(t):
	for x, c in enumerate(l):
		if c != '.':
			ants[c].append(np.array([x, y]))

nodes = set()

for c, l in ants.items():
	# print("---", c)
	for i, a1 in enumerate(l[:-1]):
		for j, a2 in enumerate(l[i+1:]):
			# print(a1, a2)
			dist = a2 - a1
			for i in range(1000):
				n1 = a1 + i * dist
				n2 = a1 - i * dist
				if in_range(n1):
					nodes.add(tuple(n1))
				if in_range(n2):
					nodes.add(tuple(n2))

print(len(nodes))
