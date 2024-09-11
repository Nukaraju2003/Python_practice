list1 = []
def DectoNBase(n,num):
    if(num>n):
        if(num%n <= 9):
            list1.append(num%n)
        else:
            list1.append(chr((num%n)+55))
        num = num // n
        DectoNBase(n, num) 
    else:
        if(num%n <= 9):
            list1.append(num%n)
        else:
            list1.append(chr((num%n)+55))  
    return " ".join(map(str, list1[::-1]))
                     


# n = int(input())
# num = int(input())
print(DectoNBase(12,718)) 
# print()
