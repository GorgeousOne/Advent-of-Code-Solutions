# Day 17

import numpy as np
import time
import copy


with open("day17_input copy.txt") as file:
# with open("day17_input.txt") as file:
	text = file.read().splitlines()

w = len(text[0])
h = len(text)

heat = np.zeros((w, h), dtype=int)
for y, line in enumerate(text):
	for x, letter in enumerate(line):
		heat[x, y] = int(letter)


class Path:
	def __init__(self) -> None:
		self.last_dirs = []
		self.loss = 0
		self.steps = [np.array([0, 0])]

	def __str__(self):
		if len(self.steps) == 0:
			return "-"
		return "".join([str(heat[x[0], x[1]]) for x in reversed(self.steps)])

losses = np.full((w, h), 99999)
display = np.full((w, h), ".")
display[w-1, h-1] = "O"

dirs = [
	(-1, 0),
	(1, 0),
	(0, 1),
	(0, -1)
]

def is_in_grid(coord):
	return coord[0] >= 0 and coord[0] < w and coord[1] >= 0 and coord[1] < h

paths = [Path()]
solution = None

while(len(paths) > 0):
	current = min(paths, key=lambda x: x.loss)
	paths.remove(current)
	is_done = False

	for dir in dirs:
		if len(current.last_dirs) > 2 and all(np.array_equal(dir, x) for x in current.last_dirs[:3]):
			continue
		neigh = current.steps[0] + dir 

		if not is_in_grid(neigh) or any(np.array_equal(neigh, x) for x in current.steps):
			continue
		
		old_loss = losses[neigh[0], neigh[1]]
		new_loss = current.loss + heat[neigh[0], neigh[1]]

		if new_loss > old_loss:
			continue

		clone = copy.deepcopy(current)
		clone.last_dirs.insert(0, dir)
		clone.steps.insert(0, neigh)
		clone.loss = new_loss
		losses[neigh[0], neigh[1]] = new_loss
		paths.append(clone)

		if np.array_equal(neigh, np.array([w-1, h-1])):
			solution = clone
			is_done = True
			break
	
	if is_done:
		break

print(solution.loss)

vis = {
	(-1, 0): "<",
	(1, 0): ">",
	(0, 1): "v",
	(0, -1): "^"
}

for i, step in enumerate(solution.steps[:-1]):
	display[step[0], step[1]] = vis[tuple(solution.last_dirs[i])]

list_of_strings = [''.join(row) for row in display.T.tolist()]
# list_of_strings = [''.join([str(i) for i in row]) for row in heat.T.tolist()]
print("\n".join(list_of_strings))