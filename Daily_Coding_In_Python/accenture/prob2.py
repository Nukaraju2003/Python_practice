
# # 1C0C1C1A0B1  
# def OperationsBinaryString(str1):
#     i = 0
#     while(i < len(str1) and len(str1) >= 3):
#         if(str1[i+1] == "A"):
#             res = str(int(str1[i]) & int(str1[i+2]))
#         elif(str1[i+1] == "B"):
#             res = str(int(str1[i]) | int(str1[i+2]))
#         elif(str1[i+1] == "C"):
#             res = str(int(str1[i]) ^ int(str1[i+2])) 
#         str1 = res + str1[i+3:]
#     return int(str1)
# str1 = "1C0C1C1A0B1"    
# print(OperationsBinaryString(str1))


def OperationsBinaryString(str1):
    a = int(str1[0])
    i = 1
    while(i < len(str1) and len(str1) >= 3):
        if(str1[i] == "A"):
            a = a & int(str1[i+1])
        elif(str1[i] == "B"):
            a = a | int(str1[i+1])
        else:
            a = a ^ int(str1[i+1])
        i+=2
    return a   

str1 = "1C0C1C1A0B1"
print(OperationsBinaryString(str1))