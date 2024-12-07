"""
https://adventofcode.com/2024/day/3
find all mul(#,#) operations in the input and sum their results
only count them if most recently there was a 'do()' and no 'don't()'
"""
import re

# with open("03test.txt", "r") as f:
with open("03input.txt", "r") as f:
	t = f.read().splitlines()
	t = ''.join(t)

sums = 0
m_count = 0

p1 = r'do\(\)'
p2 = r'don\'t\(\)'
pattern = r'mul\((\d+),(\d+)\)'

split = re.split(p1, t)

for s in split:
	split2 = re.split(p2, s)
	matches = re.findall(pattern, split2[0])
	print(matches)
	for m in matches:
		sums += int(m[0]) * int(m[1])
	m_count += len(split)

print(m_count)
print(sums)