# https://adventofcode.com/2023/day/24

import re
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# with open("day24_input copy.txt") as file:
with open("day24_input.txt") as file:
	text = file.read().splitlines()

hails = []

for i, line in enumerate(text):
	p, v = line.split(" @ ")
	ps = [float(x) for x in p.split(", ")]
	vs = [float(x) for x in v.split(", ")]
	hails.append((np.array(ps), np.array(vs)))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def generate_line(point, velocity, dist=500):
	velocity = velocity / np.linalg.norm(velocity)
	line = [point, point + dist * velocity]
	return np.array(line)

print(len(hails), "lines")
# Plot each 3D line
for line in hails[1:5]:
	p, v = line
	points = generate_line(p, v, 1000000000000000)
	ax.plot3D(points[:, 0], points[:, 1], points[:, 2])

# Customize the plot as needed
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()

# Show the interactive plot
plt.show()