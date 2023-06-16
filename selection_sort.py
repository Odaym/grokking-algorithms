def findSmallest(array):
    smallest = array[0]
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i

    return smallest_index

def selectionSort(array):
    newArray = []

    for _ in range(len(array)):
        smallest = findSmallest(array)
        newArray.append(array.pop(smallest))

    return newArray

my_array = [20, 18, 18,4 ,5 , 82 , 29]

print(selectionSort(my_array))
