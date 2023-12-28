# https://adventofcode.com/2023/day/24

import numpy as np
import z3

# with open("day24_input copy.txt") as file:
with open("day24_input.txt") as file:
	text = file.read().splitlines()

positions = []
velocities = []

for i, line in enumerate(text):
	p, v = line.split(" @ ")
	positions.append([int(x) for x in p.split(", ")])
	velocities.append([int(x) for x in v.split(", ")])


p1 = positions[0]
p2 = positions[1]
p3 = positions[2]
v1 = velocities[0]
v2 = velocities[1]
v3 = velocities[2]

p_ix, p_iy, p_iz = z3.Ints('p_ix p_iy p_iz')
v_ix, v_iy, v_iz = z3.Ints('v_ix v_iy v_iz')
t1, t2, t3 = z3.Ints('t1 t2 t3')

eq1_x = p_ix + t1 * v_ix == p1[0] + t1 * v1[0]
eq1_y = p_iy + t1 * v_iy == p1[1] + t1 * v1[1]
eq1_z = p_iz + t1 * v_iz == p1[2] + t1 * v1[2]

eq2_x = p_ix + t2 * v_ix == p2[0] + t2 * v2[0]
eq2_y = p_iy + t2 * v_iy == p2[1] + t2 * v2[1]
eq2_z = p_iz + t2 * v_iz == p2[2] + t2 * v2[2]

eq3_x = p_ix + t3 * v_ix == p3[0] + t3 * v3[0]
eq3_y = p_iy + t3 * v_iy == p3[1] + t3 * v3[1]
eq3_z = p_iz + t3 * v_iz == p3[2] + t3 * v3[2]

print(z3.simplify(p_ix + t1 * v_ix - (p1[0] + t1 * v1[0])))
eq1_x = z3.simplify(p_ix + t1 * v_ix - (p1[0] + t1 * v1[0])) == 0
eq1_y = z3.simplify(p_iy + t1 * v_iy - (p1[1] + t1 * v1[1])) == 0
eq1_z = z3.simplify(p_iz + t1 * v_iz - (p1[2] + t1 * v1[2])) == 0

eq2_x = z3.simplify(p_ix + t2 * v_ix - (p2[0] + t2 * v2[0])) == 0
eq2_y = z3.simplify(p_iy + t2 * v_iy - (p2[1] + t2 * v2[1])) == 0
eq2_z = z3.simplify(p_iz + t2 * v_iz - (p2[2] + t2 * v2[2])) == 0

eq3_x = z3.simplify(p_ix + t3 * v_ix - (p3[0] + t3 * v3[0])) == 0
eq3_y = z3.simplify(p_iy + t3 * v_iy - (p3[1] + t3 * v3[1])) == 0
eq3_z = z3.simplify(p_iz + t3 * v_iz - (p3[2] + t3 * v3[2])) == 0

solver = z3.Solver()
solver.add(eq1_x, eq1_y, eq1_z, eq2_x, eq2_y, eq2_z, eq3_x, eq3_y, eq3_z)

if solver.check() == z3.sat:
	model = solver.model()
	result_px = model[p_ix].as_long()
	result_py = model[p_iy].as_long()
	result_pz = model[p_iz].as_long()
	print(f"pz: {result_px}, py: {result_py}, pz: {result_pz}")
	print(result_px + result_py + result_pz)
else:
	print("No solution found.")