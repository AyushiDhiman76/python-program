# WAP to display nth Fibonacci number.
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b

# Replace 'n' with the desired Fibonacci number
n = 10
fib = fibonacci(n)
print("The", n, "th Fibonacci number is:", fib)
