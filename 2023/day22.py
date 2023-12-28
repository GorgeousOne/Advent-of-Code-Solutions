# https://adventofcode.com/2023/day/22

import re
import numpy as np
import copy

# with open("day22_input copy.txt") as file:
with open("day22_input.txt") as file:
	text = file.read().splitlines()

bricks = {}
grid = np.zeros((500, 500, 500), dtype=int)

maxs = 0
mins = 0

for i, line in enumerate(text):
	brick = []
	start, end = line.split("~")
	xs, ys, zs = [int(s) for s in start.split(",")]
	xe, ye, ze = [int(e) + 1 for e in end.split(",")]

	maxs = max(maxs, xs, ys, zs, xe, ye, ze)
	mins = min(mins, xs, ys, zs, xe, ye, ze)

	for z in range(zs, ze):
		for y in range(ys, ye):
			for x in range(xs, xe):
				brick.append(np.array([x, y, z]))
				grid[x, y, z] = i + 1
	bricks[i + 1] = (brick)

# print(maxs, mins)
# print(bricks)
z_bricks = sorted(list(bricks.keys()), key=lambda n: min([block[2] for block in bricks[n]]))

bottoms = {i: set() for i in range(1, len(bricks) + 1)}
tops = {i: set() for i in range(1, len(bricks) + 1)}


def drop_brick(i, brick):
	lowering = 0
	while(True):
		# print(lowering, end="")
		is_free = True

		for b in brick:
			if b[2] - lowering == 1:
				is_free = False
				break
			grid_val = grid[b[0], b[1], b[2] - 1 - lowering]

			if grid_val != 0 and grid_val != i:
				# print(lowering, chr(64 + i), "lands on", chr(64 + grid_val))
				tops[grid_val].add(i)
				bottoms[i].add(grid_val)
				is_free = False
		# print()
		if not is_free:
			break
		lowering += 1

	# hope the bricks are ordered by z value
	for b in brick:
		grid[b[0], b[1], b[2]] = 0
		grid[b[0], b[1], b[2] - lowering] = i
		# print(b[0], b[1], b[2] - 1)

for i in z_bricks:
	drop_brick(i, bricks[i])

# for key, vals in tops.items():
# 	print(chr(64 + key), "is beneath", [chr(64 + i) for i in vals])
# for key, vals in bottoms.items():
# 	print(chr(64 + key), "is ontop", [chr(64 + i) for i in vals])


useless = set()

for vals in bottoms.values():
	if len(vals) > 1:
		# print(vals, "over supportive")
		useless.update(vals)

for vals in bottoms.values():
	if len(vals) == 1:
		# print("only support", vals)
		useless.discard(*vals)

for key, vals in tops.items():
	if len(vals) == 0:
		# print(key, "not supportive")
		useless.add(key)

# print([chr(64 + i) for i in useless])
print(len(useless))


chain_sum = 0

for i in range(1, len(bricks) + 1):
	suppports = copy.deepcopy(bottoms)
	broken = set()
	next_breaks = [i]

	while(len(next_breaks) > 0):
		current = next_breaks.pop()
		nexts = tops[current]

		for next in nexts:

			if next in broken:
				continue

			suppports[next].discard(current)
			if len(suppports[next]) == 0:
				# print("above", i, "breaks", next)
				next_breaks.append(next)
				broken.add(next)
				chain_sum += 1


print(chain_sum)