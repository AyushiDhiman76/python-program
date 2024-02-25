#WAP to check a string is binary or not.
def is_binary(string):
    for char in string:
        if char not in '01':
            return False
    return True

string = "1011010101"
print(is_binary(string))  # Returns True

string = "12345"
print(is_binary(string))  # Returns False
