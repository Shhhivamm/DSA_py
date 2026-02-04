arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array: ",arr)
n = len(arr)
for i in range(1,n):
    swapped = False
    for j in range(n-i):
        if arr[j] > arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
            swapped = True
    if not swapped:
        break
print("Sorted array: ", arr)