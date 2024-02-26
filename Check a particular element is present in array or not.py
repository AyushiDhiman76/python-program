#WAP to check a particular element is present in the array or not.
def is_element_present(arr, target):
    for element in arr:
        if element == target:
            True
    return

arr = [1, 2, 3, 4, 5]
target = 1
print(is_element_present(arr, target))  # Returns True

target = 1
print(is_element_present(arr, target))  # Returns False
