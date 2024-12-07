"""
https://adventofcode.com/2024/day/3
find all mul(#,#) operations in the input and sum their results
"""

import re

# with open("03test.txt", "r") as f:
with open("03input.txt", "r") as f:
	t = f.read().splitlines()
	t = ''.join(t)
sums = 0

pattern = r'mul\((\d+),(\d+)\)'
matches = re.findall(pattern, t)

for m in matches:
	sums += int(m[0]) * int(m[1])

print(matches)
print(sums)