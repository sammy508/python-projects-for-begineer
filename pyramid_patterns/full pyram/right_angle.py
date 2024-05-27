# n = int(input("enter num of rows"))
# for i in range (0, n+1):
    
#     for j in range(0, i+1):
#         print("*", end="")
#     print()

#     # output
# #     enter num of rows5
# # *
# **
# ***
# ****
# *****
# ******


# m = int(input("enter m :"))
# for i in range(1,m+1):
#     print(" ")

#     for j in range(1, i+1):
#         print("*", end=" ")

#     print()    

n = int(input("Enter rows: "))
for i in range(1, n + 1):  # Loop through rows
    for j in range(i):  # Loop through columns
        print("*", end=" ")  # Print asterisk without newline
    print()  # Print newline at the end of each row
