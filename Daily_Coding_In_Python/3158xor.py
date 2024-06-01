nums = [1,2,1,3, 2]
d = dict()
l = []
for i in nums:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
xor = 0        
for i in d.keys():
    if(d[i] > 1):
        xor ^= i  
print(xor)                
        
    