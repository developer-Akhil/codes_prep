import pickle

a = ['test value', 'test value 2', 'test value 3']

file_name = "test_file.txt"

file_obj = open(file_name, 'wb')

pickle.dump(a, file_obj)

file_obj.close()

file_obj = open(file_name, 'rb')

b = pickle.load(file_obj)

print(b)
