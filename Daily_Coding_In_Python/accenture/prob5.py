def differenceofSum(n, m):
    a = 0
    b = 0
    i = 0
    while(i <= m):
        if(i%n == 0):
            a += i
        else: 
            b += i
        i += 1 
    return abs(a-b) 

n = int(input())
m = int(input())
print(differenceofSum(n,m))