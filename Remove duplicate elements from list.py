#WAP to remove duplicate element from list.
def remove_duplicates(input_list):
    output_list = []
    for element in input_list:
        if element not in output_list:
            output_list.append(element)
    return output_list

input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
print(remove_duplicates(input_list)) 
