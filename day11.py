import copy

'''
If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
'''
input1 = open("input_data/day11.txt").read().splitlines()
input1 = [[char for char in line] for line in input1]
input2 = copy.deepcopy(input1)

left_bound = 0
right_bound = len(input1[0]) - 1
upper_bound = 0
lower_bound = len(input1) - 1

def run_algo(input1, input2):
    no_change = 1
    for row in range(0,len(input1)):
        for col in range(0,len(input1[0])):
            if(input1[row][col] == '.'):
                input2[row][col] = input1[row][col]
                continue
            adjacent_seats = [
                (row-1,col-1), (row-1,col), (row-1,col+1),
                (row, col-1), (row,col+1), 
                (row+1,col-1), (row+1,col), (row+1,col+1)
            ]
            adjacent_seats = [seat for seat in adjacent_seats if seat[0] >= upper_bound and seat[0] <= lower_bound and seat[1] >= left_bound and seat[1] <= right_bound]
            if(input1[row][col] == 'L'):
                new_status = '#'
                for seat in adjacent_seats:
                    if input1[seat[0]][seat[1]] == '#':
                        new_status = 'L'
                        break
                input2[row][col] = new_status
            elif(input1[row][col] == '#'):
                num_adj_occ = 0
                for seat in adjacent_seats:
                    if input1[seat[0]][seat[1]] == '#':
                        num_adj_occ+=1
                input2[row][col] =  'L' if num_adj_occ>=4 else '#'
            if input1[row][col] != input2[row][col]:
                no_change = 0
    return no_change

'''
num_runs = 0
while(1):
    if(run_algo(input1, input2)):
        break
    num_runs+=1
    tmp = input1
    input1 = input2
    input2 = tmp

num_occupied = 0
for line in input1:
    for seat in line:
        num_occupied+= 1 if(seat == '#') else 0


print(num_runs, num_occupied)
'''
adjacent_seats = {}
adjacent_seats[(0,0)] = [(0,1),(1,0)]

for row in range(0,len(input1)):
    for col in range(0,len(input1[0])):
        if(input1[row][col] == 'L'):
            adjacent_seats[(row,col)] = []
            for increment_row, increment_col in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                adj_row = row + increment_row
                adj_col = col + increment_col
                while(adj_row >= upper_bound and adj_row <= lower_bound and adj_col >= left_bound and adj_col <= right_bound):
                    if(input1[adj_row][adj_col] == 'L'):
                        adjacent_seats[(row,col)].append((adj_row, adj_col))
                        break
                    adj_row+=increment_row
                    adj_col+=increment_col

# Part 2
def run_algo2(input1, input2):
    no_change = 1
    for row in range(0,len(input1)):
        for col in range(0,len(input1[0])):
            if(input1[row][col] == '.'):
                input2[row][col] = input1[row][col]
                continue

            if(input1[row][col] == 'L'):
                new_status = '#'
                for seat in adjacent_seats[(row, col)]:
                    if input1[seat[0]][seat[1]] == '#':
                        new_status = 'L'
                        break
                input2[row][col] = new_status
            elif(input1[row][col] == '#'):
                num_adj_occ = 0
                for seat in adjacent_seats[(row, col)]:
                    if input1[seat[0]][seat[1]] == '#':
                        num_adj_occ+=1
                input2[row][col] =  'L' if num_adj_occ>=5 else '#'
            if input1[row][col] != input2[row][col]:
                no_change = 0
    return no_change

num_runs = 0
while(1):
    if(run_algo2(input1, input2)):
        num_runs+=1
        break
    num_runs+=1
    tmp = input1
    input1 = input2
    input2 = tmp

num_occupied = 0
for line in input1:
    for seat in line:
        num_occupied+= 1 if(seat == '#') else 0

print(num_runs, num_occupied)