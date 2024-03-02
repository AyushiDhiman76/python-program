#WAP to check whether a list is monotonic
l=[4,3,2,0]

a1=sorted(l)
dl=a1[::-1]

if (l==a1) or (l==dl):
    print("monotonic")

else:
    print("not monotonic")
