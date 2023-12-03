# Day 3
import re

def is_gear_neighbor(y, x_start, x_end, text):
	for y in range(max(0, y-1), min(len(text) - 1, y+2)):
		for x in range(max(0, x_start-1), min(len(text[0]) - 1, x_end+1)):
			if text[y][x] == "*":
				return True
	return False


def neigh_contains(y, x, neigh):
	print
	if y == neigh[0] and x >= neigh[1] and x < neigh[2]:
		return True
		

def get_gear_neighs(y, x, gear_neighs):
	neigh_set = []
	for dy in range(max(0, y-1), min(len(text), y+2)):
		for dx in range(max(0, x-1), min(len(text[0]), x+2)):
			for neigh in gear_neighs:
				if neigh_contains(dy, dx, neigh) and neigh not in neigh_set:
					neigh_set.append(neigh)
	return neigh_set


# with open("day03_input copy.txt") as file:
with open("day03_input.txt") as file:
	text = file.read().splitlines()

possible_neighs = []
gear_sums = 0

for y, line in enumerate(text):
	for match in re.finditer(r"\d+", line):
		# print("---",match.group(0))
		if is_gear_neighbor(y, *match.span(), text):
			possible_neighs.append([y, *match.span(), int(int(match.group(0)))])

for y, line in enumerate(text):
	for match in re.finditer(r"\*", line):
		x = match.start()
		neighs = get_gear_neighs(y, x, possible_neighs)

		if len(neighs) == 2:
			# print(neighs[0][3] * neighs[1][3])
			gear_sums += neighs[0][3] * neighs[1][3]

print(gear_sums)