def binaryRecursive(array, low, high, item):
    if array == []:
        return None
    if len(array) == 1:
        return array[0]

    mid = (high + low) // 2
    guess = array[mid]

    if guess == item:
        return mid
    if guess > item:
        return binaryRecursive(array, low, mid - 1, item)
    else:
        return binaryRecursive(array, mid + 1, high, item)


array = [1, 3, 8, 9, 100, 200]
print(f'First array: 100 is at index: {binaryRecursive(array, 0, len(array) - 1, 100)}')

array2 = [1, 2]
print(f'Second array: 1 is at index: {binaryRecursive(array2, 0, len(array2) - 1, 2)}')
