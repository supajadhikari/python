#Data Strucures in python
"""1. List -> collection of mutable items
2. Tuple -> collection of immutable items 
3. set -> collection of unique items 
4. Dictionary -> collection of key value pairs"""

#1. List -> collection of mutable items
list1 = [1,2,3,4,5,6,7]
print(list1)
print(list1[4])
list1[4] =10
print(list1)
#list methods - append,insert
# remove, pop , sort, reverse
#count ,extend 

#append - add items at the end of the list 
list1.append(5)
print(list1)

#insert - add items at specific index
list1.insert(2,20)
print(list1)

# remove specific items 
list1.remove(20)
print(list1)

#remove -> remove specific items 
list1.remove(5)
print(list1)
 
#pop-> remove item at specific index
list1.pop(4)
print(list1)

#reverse -> reverse the list
list1.reverse()
print(list1)
list1.append(5)

#count - count occurence of an item 
print(list1.count(5))

#sort - sort the list
list2 = [5,4,3,2,1]
list2.sort()
print(list2)

#extend - extend use of the list by adding items form another 
list2.extend([6,7,8])
print(list2)

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

#3. set - collection of unqiue items 
set1={1,2,3,4,5,6,4,3,2,1}
print(set1)

#remove - remove specific items 
set1.remove(3)
print(set1)

#discard - remove specific item if present 
set1.discard(20) #no eroor if item not present 
print(set1)

#pop - remove arbitrary items
set1.pop()
print(set1)

#clear - remove all items 
set1.clear()
print(set1)

#4.Dictiinary - collection of key value pairs 

dict1 = {
    "name": "spj"
    "age": 20,
    "city": "ktm"
}
dict1["age"] = 27
print(dict1)
print(dict1["name"])

#methods in dictionary -> keys , values ,items , get ,update 
#keys -> returm all keys 
print(dict1.keys())

#values -> return all valuess
print(dict1.values())

#intems -> return all key value pairs 
print(dict1.values())

#items -> get value for specific key 
print(dict1.get("city"))

#get -> get value for specific key 
dict1.update({"age"}:20)
print(dict1["age"])

#update -> update value for the specifi key 
dict1.update({"age":28}) 
print(dict1.["age"])

#pop -> remove specific keyt value pair 