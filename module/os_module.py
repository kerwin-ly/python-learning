
import os
# path
print(os.getcwd())

# create a new directory
os.mkdir('/Users/liyi/Desktop/demo')

# create nested directorys
os.makedirs('/Users/liyi/Desktop/aa/bb/cc')

# remove a directory
os.rmdir('Users/liyi/Desktop/demo')

# remove nested directorys
os.removedirs('/Users/liyi/Desktop/aa/bb/cc')

# run shell in os
os.system('cmd')

# get separator (windows => \\) (mac => /)
os.sep()

# get only filename
os.path.basename('/Users/liyi/Desktop/demo') # demo

# get directory
os.path.dirname('/Users/liyi/Desktop/demo') # /Users/liyi

# get file extension
os.path.splitext('/Users/liyi/Desktop/demo.json') # ['/Users/liyi/Desktop/demo', '.json']

# get size
os.path.getsize('/Users/liyi/Desktop/demo.json') # xxx byte

# check if file exist
os.path.exists('/Users/liyi/Desktop/demo.json') # True or False

# check if it's a file / directory
os.path.isfile('/xx')
os.path.isdir('/xx')

