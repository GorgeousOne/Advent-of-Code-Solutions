# https://adventofcode.com/2023/day/17

import numpy as np
import priority_queue as pq
from collections import defaultdict

# with open("day17_input copy.txt") as file:
with open("day17_input.txt") as file:
	text = file.read().splitlines()

w = len(text[0])
h = len(text)

heat = np.zeros((w, h), dtype=int)

for y, line in enumerate(text):
	for x, letter in enumerate(line):
		heat[x, y] = int(letter)

def is_in_grid(x, y):
	return 0 <= x < w and 0 <= y < h

def add(a, b):
	return (a[0] + b[0], a[1] + b[1])

dirs = {
	0: (1, 0),
	1: (0, 1),
	2: (-1, 0),
	3: (0, -1),
}

queue = pq.PriorityQueue()
queue.add_task((0, 0, 0, 1))
queue.add_task((0, 0, 1, 1))

losses = defaultdict(lambda: (w+h)*9)
losses[(0, 0, 0, 1)] = 0
losses[(0, 0, 1, 1)] = 0

i = 0

while True:
	current = queue.pop_task()
	x, y, last_dir, consecutive = current
	loss = losses[current]

	if i % 20000 == 0:
		print(i, loss, len(queue.pq))
	i += 1

	if x == w-1 and y == h-1 and consecutive >= 4:
		print(loss)
		exit()

	new_dirs = []

	if consecutive >= 4:
		new_dirs.append(((last_dir + 1) % 4, 1))
		new_dirs.append(((last_dir - 1) % 4, 1))

	if consecutive < 10:
		new_dirs.append((last_dir, consecutive + 1))

	for new_dir, new_consecutive in new_dirs:
		new_x = x + dirs[new_dir][0]
		new_y = y + dirs[new_dir][1]

		if not is_in_grid(new_x, new_y):
			continue
		new_loss = loss + heat[new_x, new_y]
		new_step = (new_x, new_y, new_dir, new_consecutive)

		if new_loss < losses[new_step]:
			losses[new_step] = new_loss
			queue.add_task(new_step, new_loss)

