# https://adventofcode.com/2023/day/15

import re
import numpy as np

# with open("day15_input copy.txt") as file:
with open("day15_input.txt") as file:
	text = file.read().replace("\n", "").split(",")

boxes = [[] for _ in range(256)]

for i, line in enumerate(text):
	is_remove = False

	if "-" in line:
		is_remove = True
		label = line[:-1]
	else:
		label = line[:-2]
		focal = int(line[-1])

	hashy = 0
	for x in label:
		hashy += ord(x)
		hashy *= 17
		hashy %= 256

	box = boxes[hashy]

	if is_remove:
		boxes[hashy] = [lens for lens in box if lens[0] != label]
	else:
		is_present = False
		for lens in box:
			if lens[0] == label:
				lens[1] = focal
				is_present = True
				break
		if not is_present:
			box.append([label, focal])

powers = 0

for i, box in enumerate(boxes):
	for j, lens in enumerate(box):
		power = (i + 1) * (j + 1) * lens[1]
		# print(lens[0], (i + 1), (j + 1), lens[1], "=", power)
		powers += power
print(powers)