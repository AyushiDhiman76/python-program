#WAP to print all the characters whose length is even.
def print_even_length_chars(string):
    for i in range(len(string)):
        if len(string[i]) % 2 == 0:
            print(string[i])

string = "Hello, World! This is a test string."
print_even_length_chars(string)
