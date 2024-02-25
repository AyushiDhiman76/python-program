#WAP to display only digits from tuple.
def display_digits(tup):
    digits = ()
    for item in tup:
        if isinstance(item, int) or isinstance(item, float):
            digits += (item,)
    return digits

tup = (1, 2.5, "hello", (3, 4), 5)
print(display_digits(tup))  
