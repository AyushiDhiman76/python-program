# WAP to check anumber is binary.
def is_binary(n):
    if n < 0:
        return False
    if n > 0:
        if n % 10 > 1:
            return False
        n //= 10
    return True

# Replace 'n' with the number you want to check
n = 1010
if is_binary(n):
    print(n, "is binary.")
else:
    print(n, "is not binary.")
