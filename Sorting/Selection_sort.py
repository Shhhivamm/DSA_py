nums = [64, 34, 25, 5, 22, 11, 90, 12]
print("Unsorted array: ",nums)
n = len(nums)
for i in range(n-1):
    minidx = i
    for j in range(i+1, n):
        if nums[j] < nums[minidx]:
            minidx = j
    min_value = nums.pop(minidx)
    nums.insert(i , min_value)
print("Sorted array: ", nums)