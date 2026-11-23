class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def get_employee(self):
        return self.__salary
    
    def set_employee(self, new_salary):
        if new_salary < 0:
            print("Reject salary")
        else:
            self.__salary = new_salary
            print("correct")
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"salary: {self.__salary}")
        
        
Employee1 =Employee("Yene",50000)
Employee1.display_info()
print(Employee1.get_employee())
Employee1.set_employee(-500)
Employee1.set_employee(333)
        
            