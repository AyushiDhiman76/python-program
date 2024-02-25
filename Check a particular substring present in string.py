#WAP to check a particular substring present in the string.
def is_substring_present(string, substring):
    if substring in string:
        return True
    else:
        return False

string = "Hello, welcome to Python programming!"
substring = "Python"
print(is_substring_present(string, substring))
substring = "Java"
print(is_substring_present(string, substring))  
