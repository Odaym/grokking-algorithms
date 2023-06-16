from random import Random


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        index = Random().randint(0, len(array))
        pivot = array[index]
        leftSub = [i for i in array[:index] if i <= pivot]
        rightSub = [i for i in array[index+ 1:] if i > pivot]

        print(f'Left subarray is {leftSub}')
        print(f'Right subarray is {rightSub}')

        return quicksort(leftSub) + [pivot] + quicksort(rightSub)


array = [10, 2, 200, 8, 17, 567, 11, 26, 3]

print(quicksort(array))
