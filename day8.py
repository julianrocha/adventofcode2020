
instructions = open("input_data/day8.txt").read().splitlines()

accumulator = 0
prev_executed = {}

i = 0
while i < len(instructions):
	if i in prev_executed:
		print(accumulator)
		break
	prev_executed[i] = 1
	operation = instructions[i][:3]
	value = int(instructions[i][3:])
	if(operation == 'nop'):
		i+=1
	if(operation == 'acc'):
		accumulator += value
		i+=1
	if(operation == 'jmp'):
		i+=value


# Part 2
def alter_instruction(i_change):
	accumulator = 0
	prev_executed = {}
	i = 0
	while i < len(instructions):
		if i in prev_executed:
			return -1
		prev_executed[i] = 1
		operation = instructions[i][:3]
		value = int(instructions[i][3:])

		if i == i_change and operation == 'nop':
			operation = 'jmp'
		if i == i_change and operation == 'jmp':
			operation = 'nop'

		if(operation == 'nop'):
			i+=1
		if(operation == 'acc'):
			accumulator += value
			i+=1
		if(operation == 'jmp'):
			i+=value
	print(accumulator)

i = 0
while i < len(instructions):
	alter_instruction(i)
	i+=1


