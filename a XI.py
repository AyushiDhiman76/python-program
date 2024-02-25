# WAP to find all prime numbers from 1 to n numbers.
def find_primes(n):
    primes = []

    for possiblePrime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)

    return primes

# Replace 'n' with the upper limit of the range you want to search for prime numbers
n = 50
primes = find_primes(n)
print("Prime numbers from 1 to", n, "are:", primes)
