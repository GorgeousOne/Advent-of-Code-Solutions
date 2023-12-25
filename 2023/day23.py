# Day 23

import numpy as np

with open("day23_input copy.txt") as file:
# with open("day23_input.txt") as file:
	text = file.read().splitlines()

w = len(text[0])
h = len(text)
grid = np.empty((w, h), dtype=str)

for y, line in enumerate(text):
	for x, letter in enumerate(line):
		grid[x, y] = letter

class Node:
	def __init__(self, point):
		self.pos = point.copy()
		self.neighbors = []

	def edge(self, neighbor, length):
		self.neighbors.append((neighbor, length))

	def __hash__(self):
		return hash(tuple(self.pos))

	def __eq__(self, other):
		return np.array_equal(self.pos, other.pos)

	def __repr__(self):
		return f"{self.pos}"


	# D, U, R, L
directions = [
	np.array([0, 1]),
	np.array([0, -1]),
	np.array([1, 0]),
	np.array([-1, 0])]

start = Node(np.array([1, 0]))
end = Node(np.array([w-2, h-1]))

graph = {
	hash(start): start,
	hash(end): end
}

passes = {
	"v": np.array([0, 1]),
	"^": np.array([0, -1]),
	">": np.array([1, 0]),
	"<": np.array([-1, 0])
}

def discover_edge(node, next_dir):
	current = node.pos + next_dir
	last_dir = next_dir * -1
	path_length = 1

	while (True):
		new_dirs = []

		for dir in directions:
			if np.array_equal(dir, last_dir):
				continue

			next = current + dir
			x, y, = next

			if 0 <= x < w and 0 <= y < h and grid[x, y] != "#":
				path = grid[x, y]
				if path not in passes or np.array_equal(dir, passes[path]):
					new_dirs.append(dir)

		if len(new_dirs) == 0:
			# connect second node to start... or dont its not important
			# thingy = hash(tuple(current))

			# if thingy in graph:
			# 	neighbor = graph[thingy]
			# 	node.edge(neighbor, path_length)
			# 	break
			break

		if len(new_dirs) > 1:
			neighbor = Node(current)
			thingy = hash(neighbor)

			if thingy in graph:
				neighbor = graph[thingy]
				node.edge(neighbor, path_length)
				# print(node.pos, "->", neighbor.pos, path_length)
				break

			graph[thingy] = neighbor
			node.edge(neighbor, path_length)
			# print(node.pos, "->", neighbor.pos, path_length)
			# print("new", neighbor)

			discover_edge(neighbor, last_dir)
			for dir in new_dirs:
				discover_edge(neighbor, dir)
			break

		# print(current, new_dirs[0], "->", current + new_dirs[0], grid[x, y])
		current += new_dirs[0]
		last_dir = new_dirs[0] * -1
		path_length += 1


#print(grid[0, 1])
discover_edge(start, directions[0])

for node in graph.values():
	print(node, "->", node.neighbors)

def find_route(node, visited, travelled, path):
	dists = []
	next_visited = set(visited)
	next_visited.add(hash(node))

	next_path = list(path)
	next_path.append(node)

	if node is end:
		return (travelled, next_path)

	print(node.pos, "not", end.pos)
	for neighbor, edge in node.neighbors:
		if neighbor in visited:
			continue
		new_path = find_route(neighbor, next_visited, travelled + edge, next_path)

		if new_path:
			dists.append(new_path)

	if len(dists) == 0:
		return None
	return max(dists, lambda x: x[0])

print(find_route(start, set(), 1, []))