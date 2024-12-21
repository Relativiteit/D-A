array_1 = [8, 7, 4, 3, 2, 1]


def binary_search_descending(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]

        if guess == item:
            print(mid)
            return mid
        if guess < item:
            high = mid - 1
        else:
            low = mid + 1

    print('Item not in array:', item)
    return None


binary_search_descending(array_1, 1)  # Correctly prints 5 (index of 1)
