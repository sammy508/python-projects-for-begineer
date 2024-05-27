

# filtering list and select even value from the list

my_list = {1,2,3,4,5,6,7,8,8,9,11,14,15,17}
filterd_list = list(filter(lambda x: x%2 ==0, my_list))

print(my_list)
print(filterd_list)