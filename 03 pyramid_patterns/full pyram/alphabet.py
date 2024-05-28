n = int(input("enter n :"))
alpha = 65 # here 65 is an ascii value of a 

for i in range(0,n):
    print(" "*(n-1), end="")
    for j in range(0, n+1):
     print(chr(alpha),end="") 
     alpha +=1
    alpha = 65
    print()
