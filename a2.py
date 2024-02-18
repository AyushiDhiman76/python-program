#WAP TO FIND FACTORIAL OF A NO. USING FUNCTION
def factorial(n):
    var=1
    for i in range(2,n+1):
        var*=i
    return var
num=5
print("factorial of",num,"is",factorial(num))
