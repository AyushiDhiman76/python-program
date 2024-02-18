#WAP TO FIND MAXIMUM AND MINIMUM OF NUMBERS.
L=[2,45,78,38,98]

mn=L[0]
mx=L[0]

for i in L:
    if mx<1:
        mx=i
    if mn>1:
        mn=i
print("max :",mx)
print("min :",mn)
        
