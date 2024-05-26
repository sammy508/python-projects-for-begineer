k=int(input('value of a: '))
for a in range(1,k):
    for b in range(1,k):
        if a==b:
            print('A',end=" ")
        else:
            print('B',end=" ")
        
    print()