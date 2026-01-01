#file handling in python: 
#create break add or remove the text 

#create -> data add like text 
#update -> append
#remove -> indexing
#indexing -> 
# import os 
#delete

#certain keywords -> a , a+ , w+, r, r+ , 
#for deleting -> 
#import os 
#os.remove ("filename")


#open('file location'  ," mode")

#file.close()
#read
file = open("file/hello.txt", "r")
content = file.read()
print(content)
file.close()

#write
file = open("file/write.txt", mode = "w")
file.write("hi this is writing using write mode")
file.close()

#overrite the read
file = open("file/write.txt", mode = "w")
file.write("write something:")
file.close() 

#it reads from the last: 
file = open("file/write.txt", mode = "w+")
file.write("this is w+")
file.seek(0)
print(file.read())
file.close() 

#read mode
file = open("file/write.txt", mode = "r")
content = file.read()
print(content)
file.close() 

#write + 
file = open("file/write.txt", mode = "w+")
file.write("this ia a wtiter mode ")
file.seek(0)
print(file.read())

try:
    file.open("file/read.txt", mode = "r+")
    content = file.read()
    print(content)
    content2 = file.write("\n This  is added using r+ mode")
    file.close()
    
except FileNotFoundError:
    print("file not found error: ")

file3 = open ("file/read.txt", "a")
file4 = open("file/read.txt", "r")

file3.write(file4.read())
file3.close()
file4.close()

#delete 
import os
os.remove("file/hello.txt")
print(" file deleted")

#check we have that path file
ifExist = os.path.exist("file/hello.txt")
print(ifExist)

#with statement -> automatic file close
#with open("filename", mode ) as file:
#code blocks 

with open("file/read.txt", "r") as r1:
    content = r1.read()
    print(content)
    #file.close()
    
    
#wap that print table form 1 to 10 in different files 
for i in range(1,11):
    with open(f"file/{i}.txt", mode = "w") as file:
        print(f"file create of {i}.txt")
        for j in range(1,11):
            file.write(f"{i} x {j} = {i*j}\n")
            
            
#wap to print multiplication table 
#from 1 to 10 without using with statement:
