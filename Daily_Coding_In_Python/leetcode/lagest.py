# print("Hello world")

# A = {1,8,7,56,90}
# for i in A:
#     print(i)
# A.add(100)
# A.remove(7)

# B = list(A)

# n = len(B)
# for i in range(n):
#     if(B[i]>B[i+1]):
#         print(B[i])
#         break
#     else:
#         print(B[i+1]) 
#         break    
        
    

# print(B[0])





# one approach
# A = [1,4, 3, 7,5]
# A.sort()
# print(A[-1])

# second approach

# A = [1,4,3,7,5]

# B = A[0]
# for i in A:
#     if (B>A[i+1]):
#         print(B)
#     else:
#         B = A[i+1]

#third approach

A = [3,2,6,1,8]
C = len(A)

def largest(A):
    B=A[0]
    for i in range(0, C):
        if(B<A[i]):
            B=A[i]
    print(B)
     

largest(A)     
        
    
    
    
    
# for i in range(0, len(A)):
#     if(B<A[i]):
#         B=A[i]
# print(B)        
            

