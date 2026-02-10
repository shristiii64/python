for i in range (6,0,-1):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()
for i in range (1,5):
    for j in range(1,i+1):
        print(i,end="  ")
    print() 
for i in range (1,6):
    for j in range (1,3):
        print("*",end=" ")
    print()   
for i in range(1,6):
    for j in range(1,6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  