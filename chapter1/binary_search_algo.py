def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        middle = int((low + high) / 2)
        value = list[middle]

        if value == item:
            return middle
        elif value > item:
            high = middle - 1
        else:
            low = middle + 1

    return None

test_list = [1, 3, 5, 7, 9]

print(binary_search(test_list, 3))
print(binary_search(test_list, -1))