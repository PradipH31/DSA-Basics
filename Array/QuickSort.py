def quickSort(array, l, r):
    if l < r:
        pivot = part(array, l , r)
        quickSort(array, l, pivot -1)
        quickSort(array, pivot + 1, r)

def part(array, l, r):
    pivot = array[r]
    i = l -1
    for j in range(l, r):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i + 1

arr = [1, 5, 9, 19, 22, 32, 43, 45, 55, 66, 88, 90]
quickSort(arr, 0, len(arr)-1)
print(arr)