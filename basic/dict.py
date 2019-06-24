from collections import Iterable

# dict
d = {
    'name': 'kerwin',
    'age': 23,
    'sex': 'man'
}

# if name is not the attribute of d, error...
d['name'] = 'bob'

# loop key
for key in d:
    print(key)

# loop value
for value in d.values():
    print(value)

# loop object
for k, v in d.items():
    print(k, v)

# to check if it iterable
isinstance([1, 2], Iterable) # True

# to check the attribute
'weight' in d # return a bool
d.get('weight') # return None
d.get('weight', -1) # if not exist, return -1

print(d)

# set
init_set = set([1, 2, 3, 2, 2]) # return {1, 2, 3}