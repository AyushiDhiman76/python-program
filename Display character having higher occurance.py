#WAP to display a character having higher occurance.
def highest_occurance(string):
    char_count = {}
    max_count = 0
    max_char = None

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

        if char_count[char] > max_count:
            max_count = char_count[char]
            max_char = char
    return max_char

string = "hello world, welcome to the world of python programming!"
print(highest_occurance(string))  
