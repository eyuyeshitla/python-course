class Student:
    
    def __init__(self, name,grade):
        self.name =name
        self.__grade = grade
        
    def get_grade(self):
        return self.__grade
    
    def set_grade(self,new_grade):
        if new_grade < 0 or new_grade > 100:
           print("Invalid")
        else:
            self.__grade = new_grade
            
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.__grade}") 
        
        
student1 = Student("Aster",95)
student1.display_info()
print(student1.get_grade())
student1.set_grade(10)
print(student1.get_grade())

         
             
        