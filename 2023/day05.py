# https://adventofcode.com/2023/day/5

import re
import numpy as np

def get_nums(string):
	return [int(m) for m in re.findall(r"\d+", string)]

def is_in_range(x, start1, start2, step):
	return x >= start2 and x < start2 + step

def get_mapping(x, start1, start2, step):
	return start1 + (x - start2)


# with open("day05_input copy.txt") as file:
with open("day05_input.txt") as file:
	text = file.read().splitlines()

seeds = []

for num in get_nums(text[0].split(":")[1]):
	seeds.append([num, -1, -1, -1, -1, -1, -1, -1])

# print("\n".join([str(seed) for seed in seeds]))

names = ["seed", "soil", "fert", "water", "light", "temp", "humid", "loc"]
i = 3

for j in range(7):
	# print()
	# print("---",names[j+1],"---")

	while (len(text) > i and text[i] != ""):
		mapping = get_nums(text[i])
		# print(mapping)

		for seed in seeds:
			if is_in_range(seed[j], *mapping):
				seed[j+1] = get_mapping(seed[j], *mapping)
				# print("mapped", seed[j], seed[j+1])
		i += 1

	for seed in seeds:
		if seed[j+1] == -1:
			seed[j+1] = seed[j]

	i += 2

min_num = min(seeds,key = lambda t: t[7])

print(min_num)
print(min_num[0])
# print("\n".join([str(seed) for seed in seeds]))

