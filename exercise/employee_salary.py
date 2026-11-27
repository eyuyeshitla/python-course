employees = {
        "Abebe":2000,
        "Ayele":3000,
        "Aster":25000
}


for name,salary in employees.items():
    print(f"Name: {name}, Salary: {salary}")
    
name = input("Enter employee name:")
if name in employees:
    anual_salary = employees[name] * 12
    
    if employees[name] > 10000:
        bonus = employees[name] * 0.1
        employees[name] =employees[name] + bonus
    else:
        bonus = employees[name] * 0.05
        
        employees[name] =employees[name] + bonus
    
    
    print(f"Name: {name}")
    print(f"Monthly Salary: {employees[name]}") 
    print(f"Anual Salary: {anual_salary}")
    print("Bones:",bonus )    
       
        
        
        
    
    
    