import random


array_1 = [1, 2, 4, 6, 8, 10]
array_2 = [2, 4, 6, 7, 9]


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low + high // 2
        guess = list[mid]
        if guess == item:
            print(mid)
            print(item)
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return print("not in collection", item)


binary_search(array_2, random.randint(1, 9))
binary_search(array_1, random.randint(1, 9))
