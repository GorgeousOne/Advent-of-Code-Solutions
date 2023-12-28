# https://adventofcode.com/2023/day/15

import re
import numpy as np

# with open("day15_input copy.txt") as file:
with open("day15_input.txt") as file:
	text = file.read().replace("\n", "").split(",")

sums = 0
for i, line in enumerate(text):
	hashy = 0
	for x in line:
		hashy += ord(x)
		hashy *= 17
		hashy %= 256
	# print(hashy)
	sums += hashy

print(sums)