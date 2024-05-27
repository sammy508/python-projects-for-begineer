

# here we will code for multiplication table using recursion function
num = int(input("enter num :"))
def multiplication(num, times=1):
    if times >10:
        return
    print(num ,"x",times, "=" ,num*times)
    multiplication(num, times+1)
multiplication(num)    
