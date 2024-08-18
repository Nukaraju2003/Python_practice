list1 = list(map(int, input().split()))
a = list1.index(min(list1))
b = list1.index(max(list1))
list1[a], list1[b] = list1[b], list1[a]
print(" ".join(map(str, list1)))