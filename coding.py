f=open("sample.txt","r")
lines=f.readlines()
print("content of sample.txt files")
print(lines)
print("lines seperated by #:-")
for line in lines:
    words=line.split()
    for word in words:
      print(word+'#')
print() 
f.close()

