def get_name():
    print('kerwin')


get_name()

# default params: it should never be changed! For example:
def get_age(ages = []):
    ages.append(23)
    return ages;


print(get_age()); # [23]
print(get_age()) # [23, 23]

# if you want 'ages' will never be changed.
def get_ages(ages = None):
    if ages is None:
        ages = []
    ages.append(23)
    return ages

print(get_ages()) # 23
print(get_ages()) # 23

# changeable param: add '*' before params, type is tuple
def get_num(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(get_num())
print(get_num(1, 2, 3, 4))

# add '**' before params, type is dict
def get_obj(**kw):
    obj = {
        'name': 'kerwin',
        'other': kw
    }
    return obj

print(get_obj(age = 22, sex = 'man'))
