def count(array):
    if array == []:
        return 0
    if len(array) == 1:
        return 1
    else:
        return 1 + count(array[1:])


print(count([1, 2, 3, 4, 5, 98]))
print(count([1]))
print(count([]))
