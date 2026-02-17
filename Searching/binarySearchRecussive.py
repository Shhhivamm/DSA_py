nums= [3,5,8,10,15,19,21,27,35,37,39,65,69,73,82,99]
target = 21

def bs(nums, low, high, target):
    if low >high:
        print("Target not found ")
    mid = (low + high) // 2
    
    if nums[mid] == target:
        print("Target found at index:",mid)
    elif nums[mid] < target:
        return bs(nums, mid +1 , high, target)
    else:
        return bs(nums, low, mid - 1, target)

bs(nums, 0, len(nums) -1, target)