height = [0,1,0,2,1,0,1,3,2,1,2,1]
n = len(height)
leftmax = [0] * n 
rightmax = [0] * n 

leftmax[0] = height[0]
for i in range(1,n):
    leftmax[i] = max(leftmax[i-1], height[i])
    
rightmax[n-1] = height[n-1]
for i in range(n-2,-1,-1):
    rightmax[i] = max(rightmax[i+1], height[i])

trappedWater = 0
for i in range(n):
    h = min(leftmax[i], rightmax[i]) - height[i]
    trappedWater += h
print("total trapped water is: ", trappedWater)