#WAP to display the first occurance of number divisible by k in the list
def first_divisible_by_k(numbers, k):
    for num in numbers:
        if num % k == 0:
            return num
numbers= [4, 7, 2, 9, 6, 1, 3, 8]
k=3

result = first_divisible_by_k(numbers, k)
print(result)     
    
