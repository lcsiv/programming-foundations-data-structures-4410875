def find_second_smallest(my_list) -> str: 
    sorted(my_list, reverse = True)
    return str(my_list[1])

print(find_second_smallest([5, 8, 3, 2, 6]))
