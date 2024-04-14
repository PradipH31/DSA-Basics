def binarySearch(array, key):
	r = len(array) - 1
	l = 0
	while l <= r:
		m = (l + r) // 2
		if array[m] == key:
			return m
		elif key < array[m]:
			r = m - 1
		else:
			l = m + 1
	return -1

print(binarySearch([2,4,5,67,80],80) == 4)
print(binarySearch([2,4,5,67,80],-1) == -1)
print(binarySearch([2,4,5,67,80],67) == 3)
print(binarySearch([2,4,5,67,80],2) == 0)
print(binarySearch([2,4,5,67,80],100) == -1)