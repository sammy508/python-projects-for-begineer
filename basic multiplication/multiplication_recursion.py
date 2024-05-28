

# here we will code for multiplication table using recursion function
num = int(input("enter num :"))
def multiplication(num, times=1):
    if times >10:
        return
    print(num ,"x",times, "=" ,num*times)
    multiplication(num, times+1)
multiplication(num)    



# output
# enter num :10
# 10 x 1 = 10
# 10 x 2 = 20
# 10 x 3 = 30
# 10 x 4 = 40
# 10 x 5 = 50
# 10 x 6 = 60
# 10 x 7 = 70
# 10 x 8 = 80
# 10 x 9 = 90
# 10 x 10 = 100