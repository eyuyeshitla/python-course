student = {'name':"eyu", "age":21, "department": "cs"}

student["year"] = 2
print(student)


#accsess
print(student['name'])
print(student.get("age"))
print(student.get("grade", "Not available"))

# update
student["age"] =23
student.update({'name':'eyukaye', "department":"chemical enginering"})
print(student)


