

# Full pyramid in python using loop

# def full_pyramid (n):

n = int(input("input number :"))

for i in range (n):
    for j in range (n-i-1):
        print(" ", end="")

    for j in range (2*i+1):
        print("*", end="")
       
       
    print()    
      