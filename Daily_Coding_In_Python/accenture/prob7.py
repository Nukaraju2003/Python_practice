def ProductSmallestPair(sum, arr):
    arr.sort()
    if(len(arr)<2):
        return -1
    for i in range(len(arr)-1):
        if(arr[i]+arr[i+1]<sum):
            return arr[i] *arr[i+1]
    return 0

sum = int(input())
arr = list(map(int,input().split()))
print(ProductSmallestPair(sum,arr))
