#WAP to find words whose length is greater than j and less than k
def find_words_length(string, j, k):
    words = string.split()
    output_list = []

    for word in words:
        if len(word) > j and len(word) < k:
            output_list.append(word)

    return output_list

string = "This is a test string to find words whose length is greater than two and less than six"
j = 2
k = 6
print(find_words_length(string, j, k))  
