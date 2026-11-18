f = open("students.txt",'a')

f.write("Student list\n")

f.write("number \t\t name\t\t mark\n")
count =1
number =3
for i in range(number):

    name = input("Enter your name:")
    mark = int(input("Enter your mark:"))



    f.write(f"{count}  \t\t {name}  \t\t {mark}")
    count+=1
    f.write("\n")

f.close()