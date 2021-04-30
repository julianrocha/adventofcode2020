import numpy as np

input_data = open("input_data/day17.txt").read().splitlines()
cycles = 6

z_start_len = 1
y_start_len = len(input_data)
x_start_len = len(input_data[0])
# create 4 dimensional space
z_len = 1 + 2*cycles
y_len = y_start_len + 2*cycles
x_len = x_start_len + 2*cycles
p_dim = np.zeros((z_len,y_len,x_len))

for y, line in enumerate(input_data):
        for x, cube in enumerate(line):
                if cube == '#':
                        p_dim[z_len//2][y_len//2-y_start_len//2+y][x_len//2-x_start_len//2+x] = 1

def check_cube(z_cube,y_cube,x_cube,p_dim):
    active_neigh = 0
    for z in range(z_cube-1,z_cube+2):
            if z < 0 or z >= len(p_dim):
                    continue
            for y in range(y_cube-1,y_cube+2):
                    if y < 0 or y >= len(p_dim[z]):
                            continue
                    for x in range(x_cube-1,x_cube+2):
                            if x < 0 or x >= len(p_dim[z][y]) or (z,y,x) == (z_cube,y_cube,x_cube):
                                    continue
                            active_neigh += p_dim[z][y][x]
    if p_dim[z_cube][y_cube][x_cube] and active_neigh in [2,3]:
            return 1
    if not p_dim[z_cube][y_cube][x_cube] and active_neigh == 3:
            return 1
    return 0

def run_cycle(p_dim):
    p_dim_cpy = np.copy(p_dim)
    for z in range(0, z_len):
            for y in range(0, y_len):
                    for x in range(0, x_len):
                            p_dim_cpy[z][y][x] = check_cube(z,y,x,p_dim)
    return p_dim_cpy

cycle = 0
while cycle < cycles:
        p_dim = run_cycle(p_dim)
        cycle+=1

ans = 0
for z_plane in p_dim:
        for y_line in z_plane:
                for cube in y_line:
                        ans+=cube
print(ans)
