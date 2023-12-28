# https://adventofcode.com/2023/day/3
import re

not_symbols = ".1234567890"

def has_symbol_neighbor(y, x_start, x_end, text):

	# print(max(0, y-1), min(len(text) - 1, y+2))
	# print(max(0, x_start-1), min(len(text[0]) - 1, x_end+1))

	for y in range(max(0, y-1), min(len(text), y+2)):
		for x in range(max(0, x_start-1), min(len(text[0]), x_end+1)):
			# print(text[y][x])
			if text[y][x] not in not_symbols:
				return True
	return False

with open("day03_input copy.txt") as file:
# with open("day03_input.txt") as file:
	text = file.read().splitlines()


part_sums = 0

for i, line in enumerate(text):
	for match in re.finditer(r"\d+", line):
		# print("---",match.group(0))
		if has_symbol_neighbor(i, *match.span(), text):
			part_sums += int(match.group(0))


print(part_sums)