n = int(input("Enter a number:"))
count = bin(n).count('1')
print("No. of set bits:",count)