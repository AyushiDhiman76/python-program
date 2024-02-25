# WAP to find sum of digits of numbers.
def sum_of_digits(n):
    if n < 0:
        return "Invalid input. Please enter a non-negative integer."
    else:
        sum = 0
        while n > 0:
            sum += n % 10
            n //= 10
        return sum

# Replace 'n' with the number you want to find the sum of digits for
n = 12345
sum = sum_of_digits(n)
print("The sum of digits of", n, "is:", sum)
