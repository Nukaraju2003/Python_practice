# print("Hello world")
nums  = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# n = []
# for i in range(len(nums)):
#     if i not in n:
#         n.append(i)
# print(n)


# for num in nums:
#     if num not in n:
#         print(num)
#         n.append(num)
# if(len(n) < len(nums) ):
#     dots = len(nums)- len(n)
#     for i in range(dots):
#         n.append(" - ")
# print(n)                        
# print(len(n))     


k = 3
k = k % 7
print(k)  
nums  = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(nums[:-k])
print(nums[-k:])
nums[:] = nums[-k:]+nums[:-k]
print(nums) 