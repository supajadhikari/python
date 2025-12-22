# Initial list
lst = [9, 8, 7, 6, 5, 4]
print(lst)        # [9, 8, 7, 6, 5, 4]

# Access element at index 2
print(lst[2])     # 7

# Update element at index 2
lst[2] = 10
print(lst)        # [9, 8, 10, 6, 5, 4]

# Convert list to tuple
tup = tuple(lst)
print(tup)        # (9, 8, 10, 6, 5, 4)

# Convert tuple back to list
list2 = list(tup)
print(list2)      # [9, 8, 10, 6, 5, 4]

# Extend list with new elements
list2.extend([3, 2, 1])
print(list2)      # [9, 8, 10, 6, 5, 4, 3, 2, 1]

# Convert back to tuple
tup = tuple(list2)
print(tup)        # (9, 8, 10, 6, 5, 4, 3, 2, 1)
