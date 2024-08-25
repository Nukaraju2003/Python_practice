l = [1, 2, 3,4, 4, 5, 6,5,6]
d = dict()
m = []
for i in l:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] +=1
print(d)
for i in d.keys():
    if d[i] == 1:
        m.append(i)
        
print(m)        