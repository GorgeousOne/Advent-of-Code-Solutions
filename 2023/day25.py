# Day 25

import random

class Node:
	def __init__(self, name):
		self.name = name
		self.lut = {name: (None, None, 0)}
		self.neighbors = set()

	def set_dist(self, other_name, next_name, edge_idx, dist):
		self.lut[other_name] = (next_name, edge_idx, dist)

	def add_neighbor(self, other_name, edge_idx):
		self.lut[other_name] = (other_name, edge_idx, 1)
		self.neighbors.add((other_name, edge_idx))

	def get_dist(self, other):
		return self.lut.get(other, (None, None, 99999))


# with open("day25_input copy.txt") as file:
with open("day25_input.txt") as file:
	text = file.read().splitlines()

nodes = {}
edges = []
edge_iter = 0

for i, line in enumerate(text):
	part, cons = line.split(": ")
	cons = cons.split(" ")

	if part not in nodes:
		nodes[part] = Node(part)
	new_node = nodes[part]

	for con in cons:
		if con not in nodes:
			nodes[con] = Node(con)
		other_node = nodes[con]
		other_node.add_neighbor(part, edge_iter)
		new_node.add_neighbor(con, edge_iter)
		edges.append((part, con))
		edge_iter += 1

def populate_dists(node):
	unvisited = [(nodes[name], 2) for name, _ in node.neighbors]

	while(len(unvisited) > 0):
		current, min_dist = unvisited.pop(0)

		for other_name, edge in current.neighbors:
			other = nodes[other_name]
			if min_dist < other.get_dist(node.name)[2]:
				other.set_dist(node.name, current.name, edge, min_dist)
				unvisited.append((other, min_dist + 1))


def get_path(node1, node2):
	path = []
	_, _, dist = node1.get_dist(node2.name)
	current = node1

	for _ in range(dist):
		next_name, edge_idx, _ = current.get_dist(node2.name)
		path.append(edge_idx)
		current = nodes[next_name]
	return path

occurences = {}

def del_edge(idx):
	left, right = edges[idx]
	nodes[left].neighbors.remove((right, idx))
	nodes[right].neighbors.remove((left, idx))

pure_nodes = list(nodes.values())

for node in nodes.values():
	populate_dists(node)

for i in range(1000):
	node = random.choice(pure_nodes)
	other = random.choice(pure_nodes)
	# populate_dists(node)

	path = get_path(other, node)
	for edge in path:
		occurences[edge] = occurences.get(edge, 0) + 1

sorted_edges = sorted(list(occurences.keys()), key=lambda x: occurences[x])

for idx in sorted_edges[-10:]:
	print(edges[idx], occurences[idx])

to_delete = sorted_edges[-3:]

for edge in to_delete:
	del_edge(edge)

rnd = random.choice(pure_nodes)
group = [rnd]
unvisited = [rnd]

while(len(unvisited)):
	current = unvisited.pop()

	for other_name, edge in current.neighbors:
		other = nodes[other_name]

		if other not in group:
			group.append(other)
			unvisited.append(other)

print(len(nodes))
print(len(group))
print(len(nodes) - len(group))
print((len(nodes) - len(group)) * len(group))
