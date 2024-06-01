s = "hello"
sum = 0
for i in range(0,len(s)-1):
    dif = abs(ord(s[i]) - ord(s[i+1]))
    sum += dif
print(sum)