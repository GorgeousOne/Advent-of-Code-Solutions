# Day 6

import re
import numpy as np

# with open("day06_input copy.txt") as file:
with open("day06_input.txt") as file:
	text = file.read().splitlines()

times = [int(s) for s in re.findall("\d+", text[0][9:])]
max_dists = [int(s) for s in re.findall("\d+", text[1][9:])]
improves = []

for i in range(len(times)):
	time = times[i]
	max_dist = max_dists[i]
	improves.append(0)

	for j in range(time):
		dist = (time - j) * j
		if dist > max_dist:
			improves[i] += 1

print(improves)
sums = 1

for i in improves:
	sums *= i

print(sums)
