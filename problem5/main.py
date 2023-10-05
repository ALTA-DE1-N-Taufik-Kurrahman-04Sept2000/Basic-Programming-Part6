def remove_duplicates(array):
    if not array:
        return 0

    unique_ptr = 0

    for current_ptr in range(1, len(array)):
        if array[current_ptr] != array[unique_ptr]:
            unique_ptr += 1
            array[unique_ptr] = array[current_ptr]

    return unique_ptr + 1

if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9])) # 6
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([1, 2, 3, 11, 11])) # 4