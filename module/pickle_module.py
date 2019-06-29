
# save the data in hard drive
import pickle
data = ['kerwin', 'bob']
pickle_file = open('./pickle_file.pkl', 'wb')

# save data in pickle_file.pkl
pickle.dump(data, pickle_file)
pickle_file.close()

# get data in pickle_file.pkl
ff = open('./pickle_file.pkl', 'rb')
d = pickle.load(ff)
print(d)
ff.close()
