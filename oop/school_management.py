class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def displayInfo(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        
        
class Student(Person):
   
   def __init__(self, name, age,department):
       super().__init__(name, age)
       self.department = department
    
   def study(self):
       print("I am studing.")
       
   def displayInfo(self):
       super().displayInfo()
       
       print("department:",self.department)
        
    

class Teacher(Person):
   
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject = subject
        
    def teach(self):
            print("I am teaching.")
                 
    def displayInfo(self):
        super().displayInfo()
        
        print("subject:",self.subject)     
        
student1 =Student("Abel",23,"IS")
teacher1 =Teacher("Haile",30,"biology")    
print("===========student information.============")
student1.displayInfo()
student1.study()
print("===========student information.============")

teacher1.displayInfo()           
teacher1.teach()           
        