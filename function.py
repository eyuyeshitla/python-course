def grtat():
    print("this is grtat")

grtat()

def greet(name):
    print(f"hello {name}")


n = input("Enter your name:")
greet(n)    


def add(a,b):
    return a + b

result =add(5,8)
print("sum:",result)


def students(*args):
    print(args)

students("Ayele","Abel","Eyuti","Haile")




def study(name, department):
    print(f"{name} studies {department}")

study(department= "CS", name = "Eyu")

def greeting(name ="Abebe"):
    print(f"hello {name}")
greeting() 
greeting("Yene")   