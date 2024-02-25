#WAP to find nth largest and nth smallest elemenrt from list.
def nth_largest(numbers, n):
    numbers.sort(reverse=True)
    return numbers[n-1]

def nth_smallest(numbers, n):
    numbers.sort()
    return numbers[n-1]

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
n = 3
print("Nth largest element:", nth_largest(numbers, n))  
print("Nth smallest element:", nth_smallest(numbers, n))  
