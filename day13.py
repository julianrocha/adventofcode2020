input_data = open("input_data/day13.txt").read().splitlines()

earliest_estimate = int(input_data[0])
buses = [int(bus) for bus in input_data[1].split(',') if bus != 'x']

earliest_actual = earliest_estimate + max(buses)
bus_choice = -1

for bus in buses:
    departure = earliest_estimate + (bus - earliest_estimate%bus)
    if departure < earliest_actual:
        earliest_actual = departure
        bus_choice = bus
#print((earliest_actual-earliest_estimate)*bus_choice)

# Part 2
buses = input_data[1].split(',')
offsets = {}
for i in range(len(buses)):
    if buses[i] != 'x':
        buses[i] = int(buses[i])
        offsets[buses[i]] = i
buses = [int(bus) for bus in input_data[1].split(',') if bus != 'x']

t = 0
print(buses)
print(offsets)
# offsets: {41: 0, 37: 35, 541: 41, 23: 49, 13: 54, 17: 58, 29: 70, 983: 72, 19: 91}
'''
(t + 0) % 41 == 0
(t + 35) % 37 == 0
(t + 41) % 541 == 0
(t + 49) % 23 == 0
(t + 54) % 13 == 0
(t + 58) % 17 == 0
(t + 70) % 29 == 0
(t + 72) % 983 == 0
(t + 91) % 19 == 0
'''

# got stuck but this number theory helped me: https://paste.debian.net/plainh/f26a33ae
t = buses[0]
dynamic_timer = t
for bus in range(1,len(buses)):
    while(1):
        if (t+offsets[buses[bus]])%buses[bus] == 0:
            break
        t+=dynamic_timer
    dynamic_timer*=buses[bus] # We can increment by multiple of previous buses
print(t)
