# a string demo

import random

times = 3
target = random.randint(1, 10) # generate random number 1-10
num = int

while num != target and times > 0:
    num = int(input('please input your number'))
    times -= 1
    if num < target:
        print('too small')
    elif num < target:
        print('too large')

if times > 0:
    print('you make it')
else:
    print('times out')



