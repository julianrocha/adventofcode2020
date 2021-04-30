numbers = open("input_data/day9.txt").read().splitlines()

numbers = [int(num) for num in numbers]


i = 25
invalid_num = -1
invalid_i = -1
while i < len(numbers):
	preamble = numbers[i-25:i]
	sums = []
	n1 = 0
	while n1 < len(preamble):
		n2 = n1+1
		while n2 < len(preamble):
			if preamble[n1] != preamble[n2]:
				sums.append(preamble[n1] + preamble[n2])
			n2+=1
		n1+=1
	if numbers[i] not in sums:
		invalid_num = numbers[i]
		invalid_i = i
		break
	i+=1

print(invalid_num, invalid_i)

# Part 2 

for set_size in range(2, len(numbers)):
	for i_start in range(0, len(numbers) - set_size + 1):
		set_sum = 0
		for i in range(i_start, i_start + set_size):
			set_sum+=numbers[i]
		if set_sum == invalid_num:
			print(min(numbers[i_start:i_start+set_size]) + max(numbers[i_start:i_start+set_size]))
			exit()

