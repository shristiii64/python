x=int(input("enter your name"))
n=x
y=str(x)
s=0
while x>0:
    rem=x%10
    x=x//10
    s+=rem**len(y)
if n==s:
    print(s)


