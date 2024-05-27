

# xonditiobal mapping : square element if it is odd

my_list = {1,2,3,4,5,6,7,8,8,9,11,14,15,17}

mpdifies_list =  (list(map(lambda x : x**3 if x %2 !=0 else x, my_list) ))

print(mpdifies_list)