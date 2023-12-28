# https://adventofcode.com/2023/day/4

import re
import numpy as np

# with open("day04_input copy.txt") as file:
with open("day04_input.txt") as file:
	text = file.read().splitlines()

point_scale = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

point_sum = 0

for line in text:
	nums = line.split(":")[1]
	win_text, num_text = nums.split("|")

	win_nums = [int(s) for s in re.findall(r"\d+", win_text)]
	nums = [int(s) for s in  re.findall(r"\d+", num_text)]

	correct_nums = 0
	for num in nums:
		if num in win_nums:
			correct_nums += 1
	point_sum += point_scale[correct_nums]


print(point_sum)

