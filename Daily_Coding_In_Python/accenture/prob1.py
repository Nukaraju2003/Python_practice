def ratFood(r, unit, n, arr):
    if n == 0:
        return -1 
    if sum(arr) < r*unit:
        return 0
    i = 0
    s = 0
    while(i < n and s<r*unit):
        s += arr[i]   
        i+= 1         
    return i

r = int(input())
unit = int(input())
n= int(input())
arr = list(map(int, input().split()))
print(ratFood(r, unit, n, arr))