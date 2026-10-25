#Write file
f=open("demo.txt","w")
data=f.write("Hello World !")
print(data)
f.close()

#read file
f=open("demo.txt","r")
data=f.read()
print(data)
f.close()



f=open("demo.txt","r")
print("Filename:",f.name)
print("Mode:",f.mode)
print("Is Closed ?",f.closed)
f.close()
print("Is Closed?",f.closed)


#with statement

with open("demo.txt","w")as file:
    data=file.write("Hello , Python!\n")
    print(data)


with open("demo.txt","a")as file:
    data=file.write("Hello , Python!\n")
    print(data)
    

with open("demo.txt","r")as file:
    data=file.read()
    print(data)


try:
    file = open("demo.txt","r")
    data= file.read()
    print(data)
finally:
    file.close()



with open("demo.txt","a+") as file:
    file.write("Appended text\n")
    file.seek(0) 
    data = file.read()
    print(data)



with open("demo.txt","w+") as file:
    file.write("This will overwrite existing content")
    file.seek(0)
    data = file.read()
    print(data)



with open("demo.txt","r") as file_r:
    data= file_r.read()
    print("data in r:",data)


with open("demo.txt","r+") as file:
    data = file.read()
    print(data)

      




