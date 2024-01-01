# https://adventofcode.com/2023/day/21

import re
import numpy as np

with open("day21_input.txt") as file:
	text = file.read()
	some = (text.count(".") + 1) / (131 * 131)
	print(some)

# with open("day21_input copy.txt") as file:
with open("day21_input.txt") as file:
	text = file.read().splitlines()

w = len(text[0])
h = len(text)
garden = np.zeros((w, h), dtype=int)

for y, line in enumerate(text):
	for x, letter in enumerate(line):
		if letter == "#":
			garden[x, y] = 1
		elif letter == "S":
			start = (x, y)


def count_free(area_fun):
	evens = 0
	odds = 0

	for y in range(h):
		for x in range(w):
			if not area_fun(x, y):
				continue
			if garden[x, y] == 1:
				continue
			if (x + y) % 2 == 0:
				evens += 1
			else:
				odds += 1
	return evens, odds



free_mid = count_free(lambda x, y: abs(x - 65) + abs(y - 65) <= 65)
free_tl = count_free(lambda x, y: x + y < 65)
free_bl = count_free(lambda x, y: x + (130 - y) < 65)
free_tr = count_free(lambda x, y: (130 - x) + y < 65)
free_br = count_free(lambda x, y: (130 - x) + (130 - y) < 65)

combined = [free_mid, free_bl, free_br, free_tl, free_tr]
steps = 26_501_365

radius = (steps) // w + 1

even_squares = radius * radius
odd_squares = (radius - 1) * (radius - 1)

even_corners = even_squares + (radius - 1)
odd_corners = odd_squares - radius

free_plots = even_squares * free_mid[0] + odd_squares * free_mid[1]
free_plots += even_corners * free_bl[0] + odd_corners * free_bl[1]
free_plots += even_corners * free_tl[0] + odd_corners * free_tl[1]
free_plots += even_corners * free_br[0] + odd_corners * free_br[1]
free_plots += even_corners * free_tl[0] + odd_corners * free_tr[1]


free = 0

for x in combined:
	free += x[0] + x[1]

print((steps * steps + (steps-1) * (steps-1)) * some)
print(free_plots)