starting_numbers = [0,13,1,8,6,15]

second_latest_spoken = {}
latest_spoken = {}
for turn, num in enumerate(starting_numbers):
    latest_spoken[num] = turn+1

prev_number = starting_numbers[-1]

# for p2, try changing 2021 to 30000000
# time complexity is too large
for turn in range(len(starting_numbers)+1, 2021):
    current_num = -1
    if prev_number not in second_latest_spoken.keys(): # if prev_number was first occurence, say 0
        current_num = 0
    else: # otherwise say difference of latest 2 occurences
        current_num = latest_spoken[prev_number] - second_latest_spoken[prev_number]
    if current_num in latest_spoken.keys(): # this number has been spoken before
        second_latest_spoken[current_num] = latest_spoken[current_num]
    latest_spoken[current_num] = turn
    prev_number = current_num

# P2
starting_numbers = [0,13,1,8,6,15]
latest_spoken = {}

for turn, num in enumerate(starting_numbers):
    latest_spoken[num] = turn+1

prev_number = starting_numbers[-1]
for turn in range(len(starting_numbers)+1, 30000001):
    current_num
    if prev_number in latest_spoken: # was spoken previously
        current_num = turn - 1 - latest_spoken[prev_number]
    else: # was not spoken previously
        current_num = 0
    latest_spoken[prev_number] = turn - 1
    prev_number = current_num
print(prev_number)