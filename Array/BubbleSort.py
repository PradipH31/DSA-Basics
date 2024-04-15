def bubbleSort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped == False:
            break

arr = [9, 1, 5, 43, 32, 22, 19, 90, 55, 66, 45, 88]
bubbleSort(arr)
print(arr)