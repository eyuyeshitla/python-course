class Employee:

    company ="Balina"

    def __init__( self,name, department,salary):
        self.name = name
        self.department = department
        self.salary = salary
    def display_info(self):
        print(f"name: {self.name}")
        print(f"department: {self.department}")
        print(f"salary: {self.salary}")
        print("Company:",self.company) 


employee1 =Employee("Eyerusalem","Computer scince",20000)
employee2 =Employee("Haile","Software",50000)
employee1.display_info()

employee2.display_info()   




        


