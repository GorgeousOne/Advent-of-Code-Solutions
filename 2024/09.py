"""
https://adventofcode.com/2024/day/9
Parse a disk map, identifying files and free spaces based on alternating digits (each digit marks the length of a segment).
Simulate moving file blocks one at a time to the leftmost free spaces to eliminate gaps.
Calculate a checksum using block positions and their file IDs.
"""
from collections import defaultdict

# with open("09test.txt", "r") as f:
with open("09input.txt", "r") as f:
	l = f.read().strip()

disk = []
pointer = 0

for i, c in enumerate(l):
	s = int(c)
	if i % 2 == 0:
		disk = disk + [(i//2) for _ in range(s)]
	else:
		disk = disk + [-1 for _ in range(s)]

while pointer < len(disk):
	while pointer < len(disk) and disk[pointer] != -1:
		pointer += 1
	if pointer < len(disk):
		data = disk[-1]
		del disk[-1]
		disk[pointer] = data

check = sum([i * x for i, x in enumerate(disk)])
print(disk)
print(check)
