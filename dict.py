student = {'name':"eyu", "age":21, "department": "cs"}

student["year"] = 2
student['hobby']= "coding"
print(student)


#accsess
print(student['name'])
print(student.get("age"))
print(student.get("grade", "Not available"))

# update
student["age"] =23
student.update({'name':'eyukaye', "department":"chemical enginering"})
print(student)

#removing item
print(student.pop('age'))
print(student)

print(student.popitem())
print(student)

del student["department"]
print(student)

# keys and values
print(student.keys())
print(student.values())


# nested dictionary
students = { "student1": {'name':"eyu", "age":21, "department": "cs"}, 
             "student2": {'name':"haile", "age":25, "department": "SE"} ,
             "student3": {'name':"marta", "age":56, "department": "IS"}

             }

print(len(students))
print(students["student1"])
print(students["student1"]['name'])


