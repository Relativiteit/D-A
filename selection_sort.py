array_1 = [1, 2, 4, 5, 6, 10]
array_2 = [2, 1, 6, 0, 12, 14]


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort(array_1))
print(selectionSort(array_2))
