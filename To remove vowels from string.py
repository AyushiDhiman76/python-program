# WAP to remove vowels from string.
def remove_vowels(s):
    vowels = 'aeiou'
    result = ''
    for char in s:
        if char.lower() not in vowels:
            result += char
    return result

# Replace 's' with the string you want to remove vowels from
s = 'Hello, how are you today?'
result = remove_vowels(s)
print(result)
