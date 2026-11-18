f = open("notes.txt",'w')

f.write("Student list\n")
name = input("Enter your name:")
mark = int(input("Enter your mark:"))


student ={
"name":name,
"mark":mark
}

f.write(str(student))

f.close()