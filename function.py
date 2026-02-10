# def Greet (name):
#     print(f'HELLO to {name}')
# Greet ('Uniques 4.0')
# def add(n1,n2): 
#     print(n1+n2)
# add(6,288)
#  
# def Greet (name):
#   return(f'Hello {name}')
# c= Greet('sanskriti')
# print(c) 
# Calculators
# def greet(x,y):
#     print (x+y)
#     print (x-y)
#     print (x*y)
#     print (x/y)
# x= int(input("enter you number"))
# y= int(input("enter your number"))
# greet(x,y)
# Factorial of numbers function  
# def fact (n):
#     fact=1
#     for i in range (1,n+1):
#         fact=fact*i
#     print (fact)
# x=int(input("enter your number"))
# fact(x)
# Addition of given output
# def sum (n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     print(sum)
# x=int(input("enter your number"))
# sum(x) 
# def pallindrome (n):

# def character(ch,str):
#     if ch in str:
#         print ("true")
#     else:
#         print("false")
#         return()
# def add (x,y=5):
#     return x+y
# x= add (2,7)
# print(x)
# a=5
# b=6
# # print(a**b)
# def add(*wow) :
#     print(type(wow)) 
# add (5,6,8,7) 
# def add (*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# s=add(1,2,4,5)
# print(s)
# def join(*sc):
#     s=""
#     for i in sc:
#         s+=i+" "
#     return s
# print(join("python","class"))
# def avgerage(arg):
# def squares(*args):
#     total = 0
#     for i in args:
#         total += i ** 2
#     return total
# print(squares(1, 3, 5))
# def my_max(*args):
#     if not args:
#         return None 
#     maximum = args[0]
#     for num in args:
#         if num > maximum:
#             maximum = num
#     return maximum
# print("Maximum:", my_max(3, 7, 2, 9, 5))   
# x=5
# def greet():
#     x=10
#     print(x)
# greet()
# print(x)
# def greet():
#     global x
#     x=10
#     return(x)
# greet()
# print(x)
# import builtins
# print(dir(builtins))
# def greet ():
#     print("hello world")
# a=greet
# a()
#enclosure
# def outer():
#     message = "Hello"   # variable in enclosing scope
#     def inner():
#         print(message)  # accessing outer variable
#     return inner        # returning inner function
# my_func = outer()
# my_func()
# def fact (n):
#     if n ==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5)) 
# def grint(fact):

def fib(n):
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)

for i in range(10):
    print(fib(i),end=" ")

