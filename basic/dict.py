# from collections import Iterable

# dict
d = {
    'name': 'kerwin',
    'age': 23,
    'sex': 'man'
}

d1 = {'name': 'kerwin'}

# if name is not the attribute of d, error...
d['name'] = 'bob'

# loop key
for key in d.keys():
    print(key)

# loop value
for value in d.values():
    print(value)

# loop object
for k, v in d.items():
    print(k, v)

# copy
d2 = d1.copy()

# clear
d1.clear()
print(d1)

# to check if it iterable
# isinstance([1, 2], Iterable) # True

# generate a dict which key is 1, 2, 3 and value is 'kerwin'
print(d1.fromkeys((1, 2, 3), 'kerwin'))

# to check the property
'weight' in d # return a bool
d.get('weight') # return None
d.get('weight', -1) # if not exist, return -1

print(d)

