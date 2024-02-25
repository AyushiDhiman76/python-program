#WAP to print ASCII values of all the character of string with character.
def print_ascii_values(string):
    for char in string:
        print(f"{char}: {ord(char)}")

string = input("Enter a string: ")
print_ascii_values(string)
