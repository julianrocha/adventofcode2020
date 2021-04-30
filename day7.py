import re

lines = open("input_data/day7.txt").read().splitlines()

container_extraction = re.compile(r'(.+) bags contain (.*bags?)\.')
rule_extraction = re.compile(r'(\d) (.*) bags?')
rules = {}

# 0 means could not find
# 1 means could find
def find_shiny_gold(colour):
	if rules[colour] == []:
		return 0
	for inner_colour in rules[colour]:
		if inner_colour[0] == 'shiny gold':
			return 1
	for inner_colour in rules[colour]:
		if find_shiny_gold(inner_colour[0]):
			return 1
	return 0



for line in lines:
	r = container_extraction.match(line)
	container = r.group(1)

	contents = []
	for rule in r.group(2).split(', '):
		r = rule_extraction.match(rule)
		if r is None:
			break
		num = r.group(1)
		colour = r.group(2)
		contents.append((r.group(2), r.group(1)))

	rules[container] = contents

total = 0 
for colour in rules.keys():
	if colour == 'shiny gold':
		continue
	if find_shiny_gold(colour):
		total+=1

print("Num colours: " + str(len(rules.keys())))
print("Total is   : " + str(total))


# Part 2


def count_bags_inside(colour):
	if rules[colour] == []:
		return 0
	total = 0
	for bag in rules[colour]:
		total += int(bag[1])
	for bag in rules[colour]:
		total += int(bag[1]) * count_bags_inside(bag[0])
	return total

print(count_bags_inside('shiny gold'))





