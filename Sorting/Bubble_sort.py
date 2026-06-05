arr = [1,0,4,2,1,3,1,0,3,7,6,0]
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

freq ={}

for num in arr:
    if num == ",":
        continue
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1 
print("Frequency of each number:",freq)