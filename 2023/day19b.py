# Day 19
import numpy as np
import copy

# with open("day19_input copy.txt") as file:
with open("day19_input.txt") as file:
	flow_lines, parts = file.read().split("\n\n")

flow_lines = flow_lines.splitlines()
parts_lines = parts.splitlines()

flows = {}
parts = []

def copy_gt(part, key, val):
	clone = copy.deepcopy(part)
	clone[key][0] = max(clone[key][0], val + 1)
	part[key][1] = min(part[key][1], val)

	return [
		clone if clone[key][0] < clone[key][1] else None,
		part if clone[key][1] > clone[key][0] else None
	]

def copy_lt(part, key, val):
	clone = copy.deepcopy(part)
	clone[key][1] = min(clone[key][1], val - 1)
	part[key][0] = max(part[key][0], val)

	return [
		clone if clone[key][1] >= clone[key][0] else None,
		part if clone[key][0] <= clone[key][1] else None
	]

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
				condition = lambda x, k=key, t=thresh: copy_gt(x, k, t)
			else:
				condition = lambda x, k=key, t=thresh: copy_lt(x, k, t)

		rules.append([condition, next_flow])
	flows[name] = rules


flows["A"] = None
flows["R"] = None

part = {key: [1, 4000] for key in "xmas"}
remaining = [["in", part]]

accepted = 0

def get_num(min_max):
	return min_max[1] + 1 - min_max[0]

def get_perms(part):
	return get_num(part["x"]) * get_num(part["m"]) * get_num(part["a"]) * get_num(part["s"])

while len(remaining) > 0:
	flow, part = remaining.pop()

	if flow == "A":
		accepted += get_perms(part)
		continue
	if flow == "R":
		continue
	
	# print("---", flow, "---")
	rules = flows[flow]
	current = part

	for rule in rules:
		if not rule[0]:
			remaining.append([rule[1], current])
			# print(current, "->", rule[1])
			break
		divided = rule[0](current)

		if divided[0]:
			remaining.append([rule[1], divided[0]])
			# print(divided[0], "->", rule[1])
		if divided[1]:
			current = divided[1]
		else:
			break
	
print(accepted)