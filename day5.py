import math

fh = open("input_data/day5.txt", "r")



max_seat_id = 0
min_seat_id = 127 * 8 + 7
print(list(range(48,875)))
total = sum(list(range(48,875)))
num_passes = 0
for line in fh.readlines():
	upper = 127
	lower = 0
	increment = 128/2
	for r in line[:-4]:
		if r == 'B':
			lower+=increment
		else:
			upper-=increment
		increment/=2
	row = upper

	upper = 7
	lower = 0
	increment = 8/2
	for c in line[-4:-1]:
		if c == 'R':
			lower+=increment
		else:
			upper-=increment
		increment/=2
	col = upper

	seat_id = row * 8 + col
	if seat_id > max_seat_id:
		max_seat_id = seat_id
	if seat_id < min_seat_id:
		min_seat_id = seat_id

	total-=seat_id
	num_passes+=1
	

	'''
	print(line)
	print(line[:-3])
	print(line[-4:-1])
	print("Row is "+ str(row))
	print("Col is "+ str(col))
	print("SID is "+ str(seat_id))
	print()
	'''
print(min_seat_id)
print(max_seat_id)
print(total)

fh.close()
