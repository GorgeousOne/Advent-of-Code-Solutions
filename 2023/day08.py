# Day 8

import re
import numpy as np

# with open("day08_input copy.txt") as file:
with open("day08_input.txt") as file:
	text = file.read().splitlines()

graph = {}
turns = text[0]

for i, line in enumerate(text[2:]):
	graph[line[0:3]] = {"L": line[7:10], "R": line[12:15]}

node = "AAA"
i = 0

while(True):
	node = graph[node][turns[i % len(turns)]]
	i += 1
	if node == "ZZZ":
		print(i)
		break
