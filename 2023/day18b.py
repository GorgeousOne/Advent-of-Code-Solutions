# https://adventofcode.com/2023/day/18

import re
import numpy as np

with open("day18_input copy.txt") as file:
# with open("day18_input.txt") as file:
	text = file.read().splitlines()

class YLine:
	def __init__(self, x, y1, y2) -> None:
		self.x = x
		self.y_min = min(y1, y2)
		self.y_max = max(y1, y2)

	def intersects(self, y):
		return self.y_min <= y and self.y_max >= y

	# def intersect_type(self, y):
		# if

dirs = {
	"0": np.array([1, 0]),
	"1": np.array([0, 1]),
	"2": np.array([-1, 0]),
	"3": np.array([0, -1])
}

current = np.array([0, 0])
lagoon = []

for i, line in enumerate(text):
	parts = line.split()[2][2:-1]

	dir = dirs[parts[5]]
	times = int(parts[0:5], 16)
	next = current + dir * times

	if dir[0] == 0:
		lagoon.append(YLine(current[0], current[1], next[1]))

	print(current, next)
	current = next


print("trench", len(lagoon))
ends = [np.array([1, 1])]

lagoon.sort(key=lambda x: x.x)

y_start = min(lagoon, key=lambda x: x.y_min).y_min
y_end = max(lagoon, key=lambda x: x.y_max).y_max

bay_area = 0

y_steps = set(line.y_min for line in lagoon)
y_steps.add(y_end + 1)
y_steps = sorted(list(y_steps))

for i, y in enumerate(y_steps[:-1]):
	print("---", y, "---")

	y_next = y_steps[i + 1]
	height = y_next - y

	inside = False
	hit_min = False
	hit_max = False
	last_intersect = None

	for line in lagoon:
		if not line.intersects(y):
			continue
		new_intersect = line.x

		if y == line.y_min:
			if hit_max:
				inside = not inside
				hit_min = False
				hit_max = False
			else:
				hit_min = True
				hit_max = False
		elif y == line.y_max:
			if hit_min:
				inside = not inside
				hit_min = False
				hit_max = False
			else:
				hit_min = False
				hit_max = True
		else:
			inside = not inside
			hit_min = False
			hit_max = False
		print(line.x, "in" if inside else "out")

		if not inside:
			print("increase ", (new_intersect - last_intersect + 1), "*", height)
			bay_area += (new_intersect - last_intersect + 1) * height
		last_intersect = new_intersect

print()
print(bay_area)

