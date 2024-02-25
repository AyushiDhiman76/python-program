#WAP to find uncommon words from 2 string.
def uncommon_words(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())
    uncommon = words1 ^ words2
    return uncommon

str1 = "This is a test string"
str2 = "This is a test string to find uncommon words"
print(uncommon_words(str1, str2))  
