dict1 = {
    "name" : "alice",
    "age" : 30,
    "city" : "kathmandu"
}

#list 
print(dict1.values())
print(dict1.keys())
print(dict1.items())

#keys 
for i in dict1.keys():
    print(i)
    
for i in dict1.values():
    print(i)

for keys, values in dict1.items():
    print(f"(keys) : (value)")
    
    
