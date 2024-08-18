list1 = list(map(int, input().split()))
cnt = 0
for i in range(1, len(list1)-1):
    if(list1[i]>list1[i-1] and list1[i] > list1[i+1]):
        cnt +=1
print(cnt)