# Day 19
import operator

import re
import numpy as np
import inspect

# with open("day19_input copy.txt") as file:
with open("day19_input.txt") as file:
	flow_lines, parts = file.read().split("\n\n")

flow_lines = flow_lines.splitlines()
parts_lines = parts.splitlines()

flows = {}
parts = []

def is_gt(x, m, y):
	print(m, x[m], ">", y, "?")
	return x[m] > y

def is_lt(x, m, y):
	print(m, x[m], type(x[m]), "<", y, type(y), "?")
	return x[m] < y

for i, line in enumerate(flow_lines):
	name, codes = line.split("{")
	rules = []

	for code in codes[:-1].split(","):
		rule = None

		if ":" in code:
			rule, next_flow = code.split(":")
		else:
			next_flow = code

		condition = None

		if rule:
			key = rule[0]
			operand = rule[1]
			thresh = int(rule[2:])

			if operand == ">":
				condition = lambda x, k=key, t=thresh: x[k] > t
			else:
				condition = lambda x, k=key, t=thresh: x[k] < t

		rules.append([condition, next_flow])
	flows[name] = rules

for line in parts_lines:
	members = line[1:-1].split(",")
	part = {}
	for member in members:
		key, value = member.split("=")
		part[key] = int(value)
	parts.append(part)

flows["A"] = None
flows["R"] = None

# print(flows)
# print(parts)

accepted = []
rejected = []

for part in parts:
	current_flow = "in"
	while True:
		if current_flow == "A":
			accepted.append(part)
			break
		if current_flow == "R":
			rejected.append(part)
			break
		
		rules = flows[current_flow]

		for rule in rules:
			if not rule[0]:
				current_flow = rule[1]
				break
			if rule[0](part):
				current_flow = rule[1]
				break

# print(accepted)
sums = sum([sum(part.values()) for part in accepted])
print(sums)