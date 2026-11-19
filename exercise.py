'''student = {}
student["name"] =input("Enter your name:")
student["age"] =int(input("Enter your age:"))

if student["age"] > 15:
    print("Adult")
else:
    print("child")




far=float(input("Enter the temprature:"))
cel=5/9 * far-32
print("temprature in celsius=", cel)

# QUESTION list TWO
list_item =[
    { "name":"laptop","price":50000,"quantity":5},
    { "name":"mouse","price":500,"quantity":3},
    { "name":"keybord","price":500,"quantity":2},
]

print("Available products.")

for item in list_item:
    print(f"{item["name"]}:{item["quantity"]} ")

product = input("Select product:")
quantity = int(input("Enter quantity:"))

for item in list_item:
    if product == item["name"]:
     print("total:",quantity * item["price"])


'''


# QUESTION NUMBER THREE

for i in range(5):
    x=int(input("Enter the number:"))
for number in (x):
    print(number,sep=" ")

sum=0
for j in i:
    sum =sum + i
average =sum / len(i)
print("total:",sum)
print("Average:",average)

word = tuple(i)
print("highest:",max(word))
print("lowest:",min(word))


if average >= 90 and average <= 100:
    print('Grade: A')
elif average >= 80 and average  <= 89:
    print('Grade: B')
elif average >=70 and average <=79:
    print('Grade: C')
elif average >=60 and average <=69:
    print('Grade: D')
else:
    print('Grade: F')
   








    


