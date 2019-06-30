
# if you open a file, you have to close it in hook 'finally'
try:
    f = open('./demo.txt', 'w')
    for each_line in f:
        print(each_line)
except OSError as reason:
    print('error occured' + str(reason))
finally:
    f.close()
    print('still implement')

# with: close automatically, don't need to close by yourself
try:
    with open('./demo.txt', 'w') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('error occured' + str(reason))
finally:
    print('still implement')
