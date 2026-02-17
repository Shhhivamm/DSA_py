nums= [3,5,8,10,15,19,21,27,35,37,39,65,69,73,82,99]
target = 21
n = len(nums)
low, high = 0, n-1
while low <= high:
    mid = (low + high)//2

    if nums[mid] == target:
         print("Target found at index:",mid)
         break
    elif nums[mid] > target:
        high = mid -1
    else:
        low = mid + 1
else:
    print("Target not found ")