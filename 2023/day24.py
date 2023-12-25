# Day 24

import re
import numpy as np

# with open("day24_input copy.txt") as file:
with open("day24_input.txt") as file:
	text = file.read().splitlines()

hails = []

for i, line in enumerate(text):
	p, v = line.split(" @ ")
	ps = [float(x) for x in p.split(", ")[:2]]
	vs = [float(x) for x in v.split(", ")[:2]]
	hails.append((np.array(ps), np.array(vs)))


def find_intersection(p1, v1, p2, v2):
	A = np.array([v1, -v2]).T
	b = p2 - p1

	try:
		s, t = np.linalg.solve(A, b)
		if s > 0 and t > 0:
			return p1 + s * v1
		return None
	except np.linalg.LinAlgError:
		# If the system is singular (no unique solution), lines are parallel
		return None


def in_bounds(p, min_val, max_val):
	return min_val <= p[0] <= max_val and min_val <= p[1] <= max_val

sums = 0

for i in range(len(hails) - 1):
	p1, v1 = hails[i]

	for j in range(i + 1, len(hails)):
		p2, v2 = hails[j]
		meet = find_intersection(p1, v1, p2, v2)

		if meet is not None and in_bounds(meet, 200000000000000, 400000000000000):
			sums += 1
			# print(p1, p2)
			# print("----", meet)
print(sums)