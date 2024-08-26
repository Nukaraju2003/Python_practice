# # program to find second largest element 

# def lar(arr):
#     arr.sort()
#     lar = arr[-1]
#     i = len(arr) -1
#     while(i >= 0):
#         if(arr[i] == lar ):
#             i -= 1 
#         else:
#             return arr[i]
        
#     return -1 

# arr = list(map(int, input().split()))
# print(lar(arr))
# 1, 2, 3, 4, 4, 4


def largestsmallsum(arr):
    e = []
    o = []
    for i in range(0,len(arr)):
        if(i%2 == 0):
            e.append(arr[i])
        else:
            o.append(arr[i])
    e.sort()
    o.sort()
    return e[-2] + o[1]


arr = list(map(int, input().split()))
print(largestsmallsum(arr))  
    
    
    
         
    
    
arr = list(map(int, input().split()))
print(largestsmallsum(arr))