nums = [64, 34, 25, 5, 22, 11, 90, 12]
print("Unsorted array: ",nums)
n = len(nums)
for i in range(n-1):
    minidx = i
    for j in range(i+1, n):
        if nums[j] < nums[minidx]:
            minidx = j
    nums[i], nums[minidx] = nums[minidx], nums[i]
print("Sorted array: ", nums)

#Now this is classic swapping tehnique which give the algo O(n^2)