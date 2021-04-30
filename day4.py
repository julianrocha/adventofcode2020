import re

fh = open("input_data/day4.txt", "r")

passports = []
passport = []
for line in fh.readlines():
	line = line.strip().split()
	print(line)
	if(line == []):
		passports.append(passport)
		passport = []
		continue
	passport += line
passports.append(passport)
fh.close()

necessary_fields = ['iyr', 'hgt', 'eyr', 'byr', 'pid', 'ecl', 'hcl']
optional_fields = ['cid']

valid_passports = 0
total_passports = 0
for passport in passports:
	total_passports+=1
	fields = [field[0:3] for field in passport]
	if len(set(necessary_fields)-set(fields)) == 0:
		valid_passports+=1

print(total_passports)
print(valid_passports)

# Part 2


valid_passports = 0
for passport in passports:
	pass_dict = {}
	for field in passport:
		pass_dict[field[0:3]] = field[4:]
	if(len(set(necessary_fields)-set(pass_dict.keys())) != 0):
		continue
	if int(pass_dict['byr']) < 1920 or int(pass_dict['byr']) > 2002:
		continue
	if int(pass_dict['iyr']) < 2010 or int(pass_dict['iyr']) > 2020:
		continue
	if int(pass_dict['eyr']) < 2020 or int(pass_dict['eyr']) > 2030:
		continue
	if pass_dict['hgt'][-2:] not in ['in','cm']:
		continue
	if pass_dict['hgt'][-2:] == 'cm' and (int(pass_dict['hgt'][:-2]) < 150 or int(pass_dict['hgt'][:-2]) > 193):
		continue
	if pass_dict['hgt'][-2:] == 'in' and (int(pass_dict['hgt'][:-2]) < 59 or int(pass_dict['hgt'][:-2]) > 76):
		continue
	if re.match("^#[0-9|a-f]{6}$", pass_dict['hcl']) is None:
		continue
	if pass_dict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		continue
	if re.match("^\d{9}$", pass_dict['pid']) is None:
		continue

	valid_passports+=1
print(valid_passports)



