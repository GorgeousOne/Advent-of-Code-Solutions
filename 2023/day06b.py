# https://adventofcode.com/2023/day/6

import re
import numpy as np

def get_dist(race_time, acc_time):
	return (race_time - acc_time) * acc_time

# with open("day06_input copy.txt") as file:
with open("day06_input.txt") as file:
	text = file.read().splitlines()

time = int(text[0][9:].replace(" ", ""))
max_dist = int(text[1][9:].replace(" ", ""))

print(time, max_dist)
min_improve = -1
max_improve = -1

min = 0
max = time

while True:
	mid = (min + max) // 2

	if get_dist(time, mid) <= max_dist and get_dist(time, mid + 1) > max_dist:
		min_improve = mid + 1
		break

	if get_dist(time, mid) <= max_dist:
		min = mid
	else:
		max = mid


min = 0
max = time

while True:
	mid = (min + max) // 2

	if get_dist(time, mid) <= max_dist and get_dist(time, mid - 1) > max_dist:
		max_improve = mid - 1
		break

	if get_dist(time, mid) <= max_dist:
		max = mid
	else:
		min = mid
print(min_improve, max_improve)
print(max_improve - min_improve + 1)

