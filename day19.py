import re
input_data = open("input_data/day19.txt").read().splitlines()

rules = {}
msgs = []
flag = 0
rule_extraction = re.compile("(\d+):(.*)")
for line in input_data:
    if line == '':
        flag = 1
        continue
    if flag:
        msgs.append(line)
    else:
       res = rule_extraction.search(line)
       rules[res.group(1)] = res.group(2).strip()

rule = rules['0']
regex = ''

