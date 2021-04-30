
lines = open("input_data/day6.txt").read().splitlines()

num_groups=0
group = set()
total_count = 0
for line in lines:
	if line == '':
		num_groups+=1
		total_count+=len(group)
		group = set()
		continue
	for q in line:
		group.add(q)

print("Number of lines : " + str(len(lines)))
print("Number of groups: " + str(num_groups))
print("Total Count is  : " + str(total_count))

# Part 2
import string

num_groups=0
group = set(list(string.ascii_lowercase))
total_count = 0
for line in lines:
	if line == '':
		num_groups+=1
		total_count+=len(group)
		group = set(list(string.ascii_lowercase))
		continue
	personal_questions = set()
	for q in line:
		personal_questions.add(q)
	group = group.intersection(personal_questions)


print("Number of lines : " + str(len(lines)))
print("Number of groups: " + str(num_groups))
print("Total Count is  : " + str(total_count))
