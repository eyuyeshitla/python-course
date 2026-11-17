students = ["Abel","Eyu","Aster","Nolawi"]
numbers =[10,30,40,56,67]


for s in students:
    print(s)

total = 0
for num in numbers:
    total +=num

print(f"total:{total}")
print(f"Avarage:{total/len(numbers)}")   

for i in range(4):
    if i==2:
        break
    print(i)

for i in range(1,16):
    if i % 2 ==0:
        print(f"{i} is even ")
    else:
        print(f"{i} is odd ")

for s in students:
    if s == "Aster":
        continue
    print(s)

for n in numbers:
     pass

string = "python program"
i = 0
while i <= len(string):
    print(i)
    i=i+1

for i in range(4,0,-1):
    print(i)

for i in range(5):
    for j in range(2):
        print(f"{i},{j}")




