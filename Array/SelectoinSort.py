def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index],arr[i] = arr[i], arr[min_index]

arr = [9, 1, 5, 43, 32, 22, 19, 90, 55, 66, 45, 88]
selection_sort(arr)
print(arr)