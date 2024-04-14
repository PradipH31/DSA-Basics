def bubbleSort(array):
    n = len(array)
    swapped = False
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped == False:
            break

arr = [9, 1, 5, 43, 32, 22, 19, 90, 55, 66, 45, 88]
bubbleSort(arr)
print(arr)