#WAP TO COUNT THE NO. OF VOWELS IN A STRING.
S=(input ("enter statement"))
c=0
vowels= set("aeiou")
for letters in S:
    if letters in vowels:
        c=c+1
print("count of the vowels is:")
print(c)
