# Day 14

import re
import numpy as np

# with open("day14_input copy.txt") as file:
with open("day14_input.txt") as file:
	text = file.read().splitlines()

w = len(text[0])
h = len(text)
field = np.zeros((w, h), dtype=int)

for y, line in enumerate(text):
	for x, letter in enumerate(line):
		if letter == "#":
			field[x,y] = 1
		elif letter == "O":
			field[x,y] = 2

def roll_x(field, x, y, dx):
	max_x = field.shape[0] - 1 if dx > 0 else 0

	for i in range(x, max_x, dx):
		if field[i + dx, y] != 0:
			break
		field[i, y] = 0
		field[i + dx, y] = 2


def roll_y(field, x, y, dy):
	max_y = field.shape[1] - 1 if dy > 0 else 0

	for i in range(y, max_y, dy):
		if field[x, i + dy] != 0:
			break
		field[x, i] = 0
		field[x, i + dy] = 2

signs = [".", "#", "O"]

def display():
	for y in range(h):
		for x in range(w):
			print(signs[field[x,y]], end="")
		print("")
	print("")


def cycle(left):
	for y in range(h):
		for x in range(w):
			if field[x, y] == 2:
				roll_y(field, x, y, -1)

	for x in range(w):
		for y in range(h):
			if field[x, y] == 2:
				roll_x(field, x, y, -1)

	for y in range(h-1, -1, -1):
		for x in range(w):
			if field[x, y] == 2:
				roll_y(field, x, y, 1)

	for x in range(w-1, -1, -1):
		for y in range(h):
			if field[x, y] == 2:
				roll_x(field, x, y, 1)


states = []
check_repeat = True
times = 1000000000

while(times > 0):
	cycle(times)
	times -= 1
	states.insert(0, field.copy())

	if check_repeat:
		for i in range(1, len(states)):
			if np.array_equal(field, states[i]):
				print(times, "repeat after", i)
				times %= i
				print("cycle", times, "more")
				check_repeat = False

sums = 0

for y in range(h):
	for x in range(w):
		if field[x,y] == 2:
			sums += h - y

print(sums)


