"""
https://adventofcode.com/2024/day/9
Parse a disk map, identifying files and free spaces based on alternating digits (each digit marks the length of a segment).
Move whole files, in descending order, to the leftmost span of free space that can fit them; leave files that cannot fit unmoved.
Calculate a checksum using block positions and their file IDs.

"""
from collections import defaultdict

# with open("09test.txt", "r") as f:
with open("09input.txt", "r") as f:
	l = f.read().strip()

disk = {}
spaces = []
pointer = 0

for i, c in enumerate(l):
	s = int(c)
	if i % 2 == 0:
		disk[i//2] = (pointer, s)
	elif s > 0:
		spaces.append((pointer, s))
	pointer += s

for i in range(max(disk.keys()), 0, -1):
	idx1, s1 = disk[i]
	for i2 in range(len(spaces)):
		idx2, s2 = spaces[i2]
		if idx2 > idx1:
			break
		if s2 < s1:
			continue
		disk[i] = (idx2, s1)
		if s2 > s1:
			spaces[i2] = (idx2 + s1, s2 - s1)
		else:
			del spaces[i2]
		break

print(disk)
check = 0
for i, (x, s) in disk.items():
	# print(i, x, s)
	for x2 in range(x, x+s):
		check += x2*i
print(check)

