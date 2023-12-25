from graphviz import Digraph

# Create a Digraph object
graph = Digraph('example_graph', format='png')

# # Add nodes
# graph.node('A', 'Node A')
# graph.node('B', 'Node B')
# graph.node('C', 'Node C')

# # Add edges
# graph.edge('A', 'B', 'Edge 1')
# graph.edge('B', 'C', 'Edge 2')
# graph.edge('C', 'A', 'Edge 3')


# with open("day20_input copy.txt") as file:
with open("day20_input.txt") as file:
	text = file.read().splitlines()

outps = {}
colors = {}


for i, line in enumerate(text):
	input, output = line.split(" -> ")
	outputs = output.split(", ")

	if input == "broadcaster":
		graph.node("broadcaster", "broadcaster", color="red", pos=f"{i},{i}!")
		colors["broadcaster"] = "red"
		outps["broadcaster"] = outputs
		continue

	name = input[1:]

	if input[0] == "%":
		graph.node(name, input, color="green", pos=f"{i},{i}!")
		colors[name] = "green"
		outps[name] = outputs
	else:
		graph.node(name, input, color="blue", pos=f"{i},{i}!")
		colors[name] = "blue"
		outps[name] = outputs

for key, vals in outps.items():
	for o in vals:
		graph.edge(key, o, "", color=colors[key])

# Save and render the graph
graph.render('example_graph', view=True)
