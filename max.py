def maxGPT(array):
    if array == []:
        return None
    if len(array) == 1:
        return array[0]
    max_rest = maxGPT(array[1:])
    return max(array[0], max_rest)


def maxBook(array):
    if array == []:
        return None
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return max(array[0], array[1])
    max_rest = maxBook(array[1:])
    return array[0] if array[0] > max_rest else max_rest


def maxNumber(array):
    if len(array) == 2:
        return max(array[0], array[1])

    return max(array[0], maxNumber(array[1:]))


print(maxGPT([1, 28, 1903, 371, 464, 164, 19]))
print(maxBook([1, 28, 1903, 371, 464, 164, 19]))

print(maxNumber([1, 28, 1903, 371, 464, 164, 19]))
