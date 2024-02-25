# Generate fibonacci series upto n terms using while loop.
def generate_fibonacci(n):
    a, b = 0, 1
    count = 0

    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci series upto", n, "terms:")
        print(a)
    else:
        print("Fibonacci series upto", n, "terms:")
        while count < n:
            print(a, end=" ")
            a, b = b, a + b
            count += 1

# Replace 'n' with the number of terms you want to generate
n = 10
generate_fibonacci(n)
