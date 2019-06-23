# dict

d = {
    'name': 'kerwin',
    'age': 23,
    'sex': 'man'
}

# if name is not the attribute of d, error...
d['name'] = 'bob'

# to check the attribute
'weight' in d # return a bool
d.get('weight') # return None
d.get('weight', -1) # if not exist, return -1

print(d)

# set
init_set = set([1, 2, 3, 2, 2]) # return {1, 2, 3}