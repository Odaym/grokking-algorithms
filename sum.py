def sum(array):
    # instead of len(array) == 0
    if array == []:
        return 0
    if len(array) == 1:
        return array[0]
    else:
        # array[1:] sublist from 1 to len(array) - 1
        return array[0] + sum(array[1:])


print(sum([1, 2, 3, 4, 5]))
print(sum([1]))
print(sum([]))
