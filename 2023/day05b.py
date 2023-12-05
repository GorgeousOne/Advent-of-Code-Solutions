# Day 5

import re
import numpy as np
import copy

def get_nums(string):
	return [int(m) for m in re.findall(r"\d+", string)]

def ranges_intersect(start1, end1, start2, end2, step):
	return (start1 >= start2 and start1 <= end2) or (end1 >= start2 and end1 <= end2)

def split_seeds(seeds, seed, j, mapping):
	if seed[j][0] < mapping[0]:
		seed_copy = copy.deepcopy(seed)
		seed_copy[j][1] = mapping[0] - 1
		seeds.append(seed_copy)
		seed[j][0] = mapping[0]
		# print("new", seed_copy[j])
	# else:
		# print(seed[j][0], ">=", mapping[0])

	if seed[j][1] > mapping[1]:
		seed_copy = copy.deepcopy(seed)
		seed_copy[j][0] = mapping[1] + 1
		seeds.append(seed_copy)
		seed[j][1] = mapping[1]
		# print("new", seed_copy[j])
	# else:
		# print(seed[j][1], "<=", mapping[1])
	
	seed[j+1] = [(val + mapping[2]) for val in seed[j]]
	# print()

# with open("day05_input copy.txt") as file:
with open("day05_input.txt") as file:
	text = file.read().splitlines()

seeds = []
seed_ranges = get_nums(text[0].split(":")[1])

for i in range(0, len(seed_ranges), 2):
	seeds.append([[seed_ranges[i], seed_ranges[i] + seed_ranges[i+1] - 1], 
			  [-1, -1],
			  [-1, -1],
			  [-1, -1],
			  [-1, -1],
			  [-1, -1],
			  [-1, -1],
			  [-1, -1]])
	
# print(len(seeds), "seeds")
# print("\n".join([str(seed) for seed in seeds]))

names = ["seed", "soil", "fert", "water", "light", "temp", "humid", "loc"]
i = 3

for j in range(7):
	# print()
	# print("---", names[j+1], "---")
	map_ranges = []

	while (len(text) > i and text[i] != ""):
		nums = get_nums(text[i])
		map_ranges.append([nums[1], nums[1] + nums[2] - 1, nums[0] - nums[1]])
		# print(map_ranges[-1])
		i += 1

	for mapping in map_ranges:
		for seed in seeds:
			if ranges_intersect(*seed[j], *mapping):
				# print(seed[j],"intersects", mapping)
				split_seeds(seeds, seed, j, mapping)
	if j + 1 < 8:
		for seed in seeds:
			if seed[j + 1][0] == -1:
				seed[j + 1] = copy.deepcopy(seed[j])
	i += 2

min_num = min(seeds,key = lambda t: t[7][0])

# for seed in seeds:
	# print(seed)

print(len(seeds), "seeds")
print(min_num)
print(min_num[7][0])

