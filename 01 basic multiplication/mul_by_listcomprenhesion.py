

# multiplication using list comprehension

# taking input from user

num = int(input("enter num : "))

# using list comprehension to print multiplication table

_= [print(num,"x",i, "=",num*i) for i in range(1,11)]

#output
# enter num : 11
# 11 x 1 = 11
# 11 x 2 = 22
# 11 x 3 = 33
# 11 x 4 = 44
# 11 x 5 = 55
# 11 x 6 = 66
# 11 x 7 = 77
# 11 x 8 = 88
# 11 x 9 = 99
# 11 x 10 = 110