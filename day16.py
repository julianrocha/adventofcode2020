input_data = open("input_data/day16.txt").read().splitlines()

rules = {}
your_ticket = []
nearby_tickets = []
for i, line in enumerate(input_data):
    if i <= 19:
        field, ranges = line.split(': ')
        lower_range, upper_range = ranges.split(' or ')
        values = []
        values += lower_range.split('-')
        values += upper_range.split('-')
        rule = set()
        rule |= {i for i in range(int(values[0]), int(values[1])+1)} # set, union
        rule |= {i for i in range(int(values[2]), int(values[3])+1)} # set, union
        rules[field] = rule
    if i == 22:
        your_ticket = [int(n) for n in line.split(',')]
    if i >= 25:
        nearby_tickets.append([int(n) for n in line.split(',')])

aggregate_rules = set()
for rule in rules.values():
    aggregate_rules |= rule

ans = 0
for ticket in nearby_tickets:
    for value in ticket:
        if value not in aggregate_rules:
            ans += value
print(ans)

# P2
def valid_ticket(ticket):
    for value in ticket:
        if value not in aggregate_rules:
            return 0
    return 1
nearby_valid_tickets = [ticket for ticket in nearby_tickets if valid_ticket(ticket)]

possible_rules = {}
for field in range(0, len(nearby_valid_tickets[0])):
    rules_that_apply = list(rules.keys())
    for ticket in nearby_valid_tickets:
        for rule in rules_that_apply:
            if ticket[field] not in rules[rule]:
                rules_that_apply.remove(rule)
    possible_rules[field] =  set(rules_that_apply)
    #print(field,rules_that_apply)

actual_rules = {}
taken_rules = set()
for t in range(0, len(possible_rules.keys())): # for each field
    for field, rules_that_apply in possible_rules.items():
        if len(rules_that_apply-taken_rules) == 1:
            rule = list(rules_that_apply-taken_rules)[0]
            actual_rules[rule] = field
            taken_rules.add(rule)
            break

ans = 1
for rule, field in actual_rules.items():
    if rule.startswith('departure'):
        ans*=your_ticket[field]
print(ans)