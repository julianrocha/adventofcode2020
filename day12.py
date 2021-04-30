import math

instructions = open("input_data/day12.txt").read().splitlines()

distance_x = 0
distance_y = 0
rotation = 0
for instruction in instructions:
    action = instruction[0]
    value = int(instruction[1:])
    if action == 'N':
        distance_y += value
    if action == 'S':
        distance_y -= value
    if action == 'E':
        distance_x += value
    if action == 'W':
        distance_x -= value
    if action == 'L':
        rotation = (rotation + value) % 360
    if action == 'R':
        rotation = (rotation - value) % 360
    if action == 'F':
        distance_x += value * math.cos(rotation * math.pi/180)
        distance_y += value * math.sin(rotation * math.pi/180)
print(abs(distance_x) + abs(distance_y))

# Part 2
way_x = 10
way_y = 1
ship_x = 0
ship_y = 0
for instruction in instructions:
    action = instruction[0]
    value = int(instruction[1:])
    if action == 'N':
        way_y += value
    elif action == 'S':
        way_y -= value
    elif action == 'E':
        way_x += value
    elif action == 'W':
        way_x -= value
    elif instruction in ['L90','R270']:
        way_x, way_y = -1*way_y, way_x
    elif instruction in ['L180','R180']:
        way_x, way_y = -1*way_x, -1*way_y
    elif instruction in ['L270','R90']:
        way_x, way_y = way_y, -1*way_x
    elif action == 'F':
        ship_x+=value*way_x
        ship_y+=value*way_y
print(abs(ship_x) + abs(ship_y))

