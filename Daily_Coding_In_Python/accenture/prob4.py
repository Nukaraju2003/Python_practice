def findCount(arr, l, num, diff):
    count = 0
    for i in range(l):
        if(abs(arr[i] - num) <= diff):
            count += 1 
    if count == 0:
        return -1         
    
    return count 


arr = list(map(int, input().split()))
num = int(input())
diff = int(input())
l = len(arr)
print(findCount(arr, l, num, diff))
