import os.path as p
print("Contents of file1")

file1=open("file1.txt","r")
print(file1.read())

print()
print("Contents of file2")

file2=open("file2.txt","r")
print(file2.read())

count =0
val = "Java"
arr = ["file1.txt","file2.txt"]
n = len(arr)
print(n)

with open("file1.txt","r") as input:
    with open("file3.txt","w") as output:
        for line in input:
            words = line.split(" ")
            if val in words:
                words.remove(val)
            
            for w in words:
                count+=1
                output.write(w)
                output.write(" ")


with open("file2.txt","r") as input:
    with open("file3.txt","a") as output:
        for line in input:
            words = line.split(" ")
            if val in words:
                words.remove(val)
            for w in words:
                count+=1
                output.write(w)
                output.write(" ")
print()
file3=open("file3.txt","r")
print(file3.read())
print("Total words written",count)
file3.close()







