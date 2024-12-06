"""
https://adventofcode.com/2024/day/6
a guard walks on a square game field, turning right in front of obstacles, until they leave the field.
find out all ways to put 1 extra obstacle on the field, so that they walk in circles infinitely.
"""
import numpy as np
import tqdm

dirs = np.array([
	[0, -1],
	[1, 0],
	[0, 1],
	[-1, 0]
])

def does_leave(field, g):
	i = 0
	d = dirs[i]
	path = set()

	while g[0] >= 0 and g[0] < field.shape[0] and g[1] >= 0 and g[1] < field.shape[1]:
		pos = (tuple(g), i)
		# print(pos)
		if pos in path:
			return False, path

		path.add(pos)
		fw = g + d
		# print(fw)
		if fw[0] >= 0 and fw[0] < field.shape[0] and fw[1] >= 0 and fw[1] < field.shape[1]:
			if 1 == field[tuple(fw)]:
				i += 1
				i %= 4
				d = dirs[i]
				# print("turn")
			else:
				# print("walk")
				g = fw
		else:
			return True, path


# with open("06test.txt", "r") as f:
with open("06input.txt", "r") as f:
	t = f.read().splitlines()

field = np.zeros((len(t[0]), len(t)), dtype=np.int64)

for y, l in enumerate(t):
	for x, c in enumerate(l):
		if c == '#':
			field[x,y] = 1
		elif c == '^':
			g = np.array([x, y], dtype=np.int64)


_, def_path = does_leave(field, g)
crates = set()

# put a crate after each step of the default path
# check with the new field if they ever leave
for pos, i in tqdm.tqdm(def_path):
	pos = np.array(pos)
	dir = dirs[i]
	crate = pos + dir
	if crate[0] >= 0 and crate[0] < field.shape[0] and crate[1] >= 0 and crate[1] < field.shape[1]:
		if 1 == field[tuple(crate)]:
			continue
		if (tuple(crate) in crates):
			continue
		field2 = np.copy(field)
		field2[tuple(crate)] = 1

		leaves, _ = does_leave(field2, g)
		if not leaves:
			# print("crate", crate)
			crates.add(tuple(crate))

print(len(crates))


