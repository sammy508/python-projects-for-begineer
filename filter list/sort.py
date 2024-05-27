

# sorted list of dictionary : sort a lsit of dictionary based on soecific key

my_list = [
    {'a': 2},
    {'b': 5},
    {'c': 3},
    {'e': 8},
    {'d': 10}
]

# sorting based on the keys of dictionaries

sorted_list = sorted(my_list, key= lambda x: list(x.keys())[0])

print(sorted_list)