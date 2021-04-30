adapters = [int(num) for num in open("input_data/day10.txt").read().splitlines()]

adapters.sort()

prev = 0
one_jumps = 0
three_jumps = 0
for adapter in adapters:
	jump = adapter - prev
	if jump == 1:
		one_jumps+=1
	if jump == 3:
		three_jumps+=1
	prev = adapter
three_jumps+=1
print(one_jumps * three_jumps)


# Part 2
# Smaller test input
# adapters = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
# num distinct arragnements = 19208

device_joltage = max(adapters) + 3
port_joltage = 0

def jumps_from(joltage):
	if joltage == device_joltage or joltage + 1 == device_joltage or joltage + 2 == device_joltage or joltage + 3 == device_joltage:
		return 1
	paths = 0
	if joltage + 1 in adapters:
		paths += jumps_from(joltage + 1)
	if joltage + 2 in adapters:
		paths += jumps_from(joltage + 2)
	if joltage + 3 in adapters:
		paths += jumps_from(joltage + 3)
	return paths

# print(jumps_from(0))
# the above solution works for small input, but its time complexity will not be sufficient for the real input
# I think I will need to use some sort of dynamic programming approach

#adapters = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
#adapters.sort()
# I wil try caching results
ways_to_get_to = {}
ways_to_get_to[0] = 1 # one way to get to port

for adapter in adapters:
	ways = 0
	if adapter - 1 in ways_to_get_to:
		ways += ways_to_get_to[adapter - 1]
	if adapter - 2 in ways_to_get_to:
		ways += ways_to_get_to[adapter - 2]
	if adapter - 3 in ways_to_get_to:
		ways += ways_to_get_to[adapter - 3]

	ways_to_get_to[adapter] = ways

print(ways_to_get_to)
