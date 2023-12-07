# Day 7

import re
import numpy as np
from operator import countOf

vals = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def compare_hands(hand1, hand2):
	rank1 = get_rank(hand1)
	rank2 = get_rank(hand2)

	if rank1 < rank2:
		return -1
	elif rank1 > rank2:
		return 1
	else:
		return is_higher(hand1, hand2)


def is_higher(hand, other):
	for i in range(5):
		i1 = vals.index(hand[i])
		i2 = vals.index(other[i])
		if i1 < i2:
			return 1
		elif i1 > i2:
			return -1
	return 0


def get_rank(hand):
	sorted = sort_letters(hand)

	if is_fiver(sorted):
		return 6
	elif is_fourer(sorted):
		if "J" in sorted: #make 5
			return 6
		return 5
	elif is_house(sorted):
		if "J" in sorted: #make 5
			return 6
		return 4
	elif is_threeer(sorted):
		if "J" in sorted: #make 4
			return 5
		return 3
	elif is_two_pair(sorted):
		if "J" in sorted:
			if sorted["J"] == 2: 
				return 5 #make 4
			else: 
				return 4 #make house
		return 2
	elif is_one_pair(sorted):
		if "J" in sorted: #make 3
			return 3
		return 1

	if "J" in sorted: #make pair
		return 1
	return 0


def sort_letters(hand):
	sorted = {}
	for card in hand:
		sorted[card] = sorted.get(card, 0) + 1
	return sorted

def is_fiver(sorted):
	return 5 in sorted.values()

def is_fourer(sorted):
	return 4 in sorted.values()

def is_house(sorted):
	return 3 in sorted.values() and 2 in sorted.values()

def is_threeer(sorted):
	return 3 in sorted.values()

def is_two_pair(sorted):
	return countOf(sorted.values(), 2) == 2

def is_one_pair(sorted):
	return 2 in sorted.values()




# with open("day07_input copy.txt") as file:
with open("day07_input.txt") as file:
	text = file.read().splitlines()

stakes = []

for i, line in enumerate(text):
	stakes.append(line.split())

from functools import cmp_to_key
stakes = sorted(stakes, key=cmp_to_key(lambda x, y: compare_hands(x[0], y[0])))

wins = 0
for i, val in enumerate(stakes):
	wins += (i+1) * int(val[1])
print (wins)
