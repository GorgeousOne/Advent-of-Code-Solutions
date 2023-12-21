# Day 20

import re
import numpy as np

# with open("day20_input copy.txt") as file:
with open("day20_input.txt") as file:
	text = file.read().splitlines()

class Module:
	def __init__(self, name, outputs) -> None:
			self.outputs = outputs
			self.name = name


class Broadcast(Module):
	def __init__(self, outputs) -> None:
		super().__init__("broadcaster", outputs)

	def trigger(self, input, high_pulse):
		return [[self.name, o, high_pulse] for o in self.outputs]
			
	def __repr__(self):
		return f"{self.name} -> {', '.join(self.outputs)}"
	

class FlipFlop(Module):
	def __init__(self, name, outputs) -> None:
		super().__init__(name, outputs)
		self.state = False

	def trigger(self, input, high_pulse):
		if high_pulse:
			return []
		self.state = not self.state
		return [[self.name, o, self.state] for o in self.outputs]

	def __repr__(self):
		return f"%{self.name} -> {', '.join(self.outputs)}"


class Conjunction(Module):
	def __init__(self, name, outputs) -> None:
		super().__init__(name, outputs)
		self.input_states = {}
		self.state = False

	def trigger(self, input, high_pulse):
		self.input_states[input] = high_pulse
		self.state = all(self.input_states.values())
		return [[self.name, o, not self.state] for o in self.outputs]

	def __repr__(self):
		return f"&{self.name} -> {', '.join(self.outputs)}"
	

modules = {}

for i, line in enumerate(text):
	input, output = line.split(" -> ")
	outputs = output.split(", ")

	if input == "broadcaster":
		modules[input] = Broadcast(outputs)
		continue

	name = input[1:]

	if input[0] == "%":
		modules[name] = FlipFlop(name, outputs)
	else:
		modules[name] = Conjunction(name, outputs)

for module in modules.values():
	if type(module) == Conjunction:
		module.input_states = {m.name: False for m in modules.values() if module.name in m.outputs}

print(modules)

for i in range(1, 10000):
	queue = [["button", "broadcaster", False]]
	pulses = 0

	while(len(queue) > 0):
		pulse = queue.pop(0)

		if pulse[1] not in modules:
			continue

		if pulse[1] in ["xp", "ln", "gp", "xl"] and not pulse[2]:
			print(i, pulse[1])

		outputs = modules[pulse[1]].trigger(pulse[0], pulse[2])
		queue.extend(outputs)

# your mom now take the lowest loop of those 4 nodes and lcm sync the shit out of them
