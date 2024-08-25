words = ["bella", "label", "roller"]

l = []
for k in words[0]:
    if k not in l:
        l.append(k)
print(l)  

for i in l:  
    for j in range(0, len(words)):
        if i not in words[j]:
            l.remove(i)                    
print(l)  

d = dict()

for m in l:
    d[m] = words[0].count(m)
    
for j in d.keys():
    for i in range(0, len(words)):
        d[j] = min(d[j], words[i].count(j))
            
print(d) 

w = []
for i in d.keys():
    for j in range(d[i]):
        w.append(i)   
        
print(w)        
    




# for i in words:
#     d = dict()
#     for j in i:
#         if j not in d.keys():
#             d[j] = 1
#         else:
#             d[j] +=1
#     print(d)        

# l = []
        
           
    
    








# for i in words[0]:
#     if i not in l:
#         l.append(i)     
# # print(l)

# for j in range(0, len(l)):
    # print(l[j])

     
