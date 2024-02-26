#WAP to remove kth character from string.
def remove_kth_char(string, k):
    if k < 1 or k > len(string):
        raise ValueError("k must be between 1 and the length of the string")

    start = 0
    if k > 1:
        start = k - 1
    end = len(string) - 1
    return string[:start] +string[start+1:]
string = "Hello, World!"
k = 6
print(remove_kth_char(string, k))  
