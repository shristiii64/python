# s = "dev"
# for i in range (len(s)):
#    if i%2==0:
#     print(s[i],end=" ")
# s="sheera"
# for i in s:
#   if i%2==0:
#     print(s[i])
# string=input("enter your string")
# count=0
# for ch in string:
#     if ch.isupper():
#         break
#     if ch .islower():
#         count+=1
#         print(count)
# s = input("enter your word")
# for ch in s:
#     if ch.isalpha():
#         print(ch.upper())
# s='HelloWorld'
# print(s.isalpha())
# name=input("enter your name")
# word=input("enter your word")
# count=0
# for ch in name:
#     if(ch==word):
#         count+=1   
# print (count)
# # s=input("enter a string")
# # for i in s:
# #     if (i.islower()):
# #         i=i.upper()
# #         print(i, end="")
# #     elif(i.isupper()):
# #         i=i.lower()
# #         print(i,end="")
# #     else:
# #         print(i,end="")
# s="abcdefg"
# r=""
# for i in range(len(s)-1,-1,-1):
#     if i%2==0:
#         r += s[i]
# print(r)

# n = int(input("Enter a positive integer: "))
# while n >= 10:     
#     temp = 0      
#     while n > 0:       
#         digit = n % 10   
#         temp += digit   
#         n = n // 10     
#     n = temp            
# print("Digital root:", n) 
# arr = [1,2,3,5,6,8]
# unique = []
# for i in arr:
#     flag = 0
#     for j in unique:
#         if i == j:
#             flag = 1
#     if flag == 0:
#         unique += [i]
# print(unique) 
arr=[2,4,6,10,18]
result=10
for i in range (0,len(arr)):
    for j in range (0,len(arr)):
        if arr[i]+arr[j]==result:
            print("the sum of the",i,"and",j,"=", result) 
# nums = [3, 2, 4]
# result = 6
# seen = {}
# for i in range(len(nums)):
#     need = target - nums[i]
#     if need in seen:
#         print(seen[need], i)
#         break
#     seen[nums[i]] = i

