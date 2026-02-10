# x=0
# y=1
# z=y
# i=int(input("Enter the number of terms you want in series: "))
# if i<=2:
#     if i==1:
#         print(x,end=" ")
#     elif i==2:
#         print(x,y,end=" ")
#     else:
#         print("Greater value for number of terms")
# else: 
#     print(x,y,end=" ")
#     for j in range(i-2):
#         z=x+y  
#         print(z,end=" ")
#         x=y
#         y=z




n = int(input("Enter the range: "))
n1, n2 = 0, 1
for i in range(1, n + 1):
    if i == 1:
        print(n1, end=" ")
    elif i == 2:
        print(n2, end=" ")
    else:
        n3 = n1 + n2
        print(n3, end=" ")
        n1 = n2 
        n2 = n3

# a,b=0,1
# n=int(input("enter your number"))
# for i in range(n):
#     print(a,end= " ")
#     a,b=b,(a+b)
