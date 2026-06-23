arr = list(map(int, input().split()))   # This is how you take input as a list of integers in python 
'''
input()           "10 20 30 40 50"
.split()          ['10', '20', '30', '40', '50']
map(int, ...)     converts each string to int
list(...)         creates a list 
'''
arr.sort()
ans = max((arr[0]* arr[1]* arr[2]), (arr[2]* arr[3]* arr[4]))
print("largest product among 5 integer is:", ans)