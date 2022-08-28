tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])

listed_tel=list(tel)
print(listed_tel)

# del tel['sape']
# print(tel)

sorted(tel)
print(tel)

# dict constructor
new_dict=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(new_dict)