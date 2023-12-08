# Day 8

import re
import numpy as np

import math

# with open("day08_input copy.txt") as file:
with open("day08_input.txt") as file:
	text = file.read().splitlines()


def get_steps(graph, current_node, turns):
	current_steps = 0

	while(True):
		next_turn = turns[current_steps % len(turns)]
		current_node = graph[current_node][next_turn]
		current_steps += 1

		if current_node[-1] == "Z":
			return current_steps		


graph = {}
turns = text[0]

for i, line in enumerate(text[2:]):
	graph[line[0:3]] = {"L": line[7:10], "R": line[12:15]}

nodes = list(filter(lambda node: node[-1] == "A", graph.keys()))
i = 0

steps = [get_steps(graph, node, turns) for node in nodes]
# ye for the answer I just slapped those in some LCM calculator
# ---------------------------

def lcm(a, b):
	return a * b // math.gcd(a, b)

def massive_lcm(some_list):
	if len(some_list) == 2:
		return lcm(some_list[0], some_list[1])
	return lcm(some_list[0], massive_lcm(some_list[1:]))

print(massive_lcm(steps))

