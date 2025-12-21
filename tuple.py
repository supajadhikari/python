#2. Tuple -> collection of immutable items 

lst = [9,8,7,6,5,4]
print(lst)        # [9, 8, 7, 6, 5, 4]
print(lst[2])     # 7
lst[2] = 10
print(lst)        # [9, 8, 10, 6, 5, 4]
list2 = list(tup)   
print(list2)
list2.extend([3,2,1])
print(list2)
tup = tuple(list2)
print(tup)