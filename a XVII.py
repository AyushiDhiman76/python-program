#WAP to check whether a number is armstrong or not
n=int(input("enter any numbers:"))
sum=0

temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

if n==sum:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")
