# s = input("Enter your string:")
s = [1,3,4,1,1,2,0,2,0,1]
freq = {}
for c in s:
    if c ==",":
        continue
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
print(freq)
