import re

input_data = open("input_data/day14_sample.txt").read().splitlines()
mask_1 = 0 # X->0, 0->0, 1->1, OR with value to get masked
mask_0 = 0 # X->1, 0->0, 1->1, AND with value to get masked
memory = {}
instruction_extraction = re.compile(r'mem\[(\d+)\] = (\d+)')
for line in input_data:
    if line[:4] == 'mask':
        mask_1 = 0
        mask_0 = 0
        for position, bit in enumerate(line[7:]):
            if bit == 'X':
                mask_0+=2**(35-position)
            elif bit == '1':
                mask_1+=2**(35-position)
                mask_0+=2**(35-position)
    else:
        r = instruction_extraction.match(line)
        address = int(r.group(1))
        value = int(r.group(2))
        value = value | mask_1
        value = value & mask_0
        memory[address] = value
        
sum = 0
for value in memory.values():
    sum += value
#print(sum)

# Part 2
mask = 0
# 0-> unchanged
# 1-> overwrite to 1
# X-> overwrite to 0, for each X position, 
memory = {}
for line in input_data:
    if line[:4] == 'mask':
        mask_1 = 0
        mask_0 = 0
        for position, bit in enumerate(line[7:]):
            if bit == 'X':
                mask+=2**(35-position)
            elif bit == '1':
                mask+=2**(35-position)
    else:
        r = instruction_extraction.match(line)
        address = int(r.group(1))
        value = int(r.group(2))
        memory[address] = value

sum = 0
for value in memory.values():
    sum += value
print(sum) # should be 208