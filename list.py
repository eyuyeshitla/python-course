print("list in python")
students = ['Abebe', 'Kebede', "Ayele", "Aster" ,"Chalitu"]
numbers = [12,23,34,56,78,90]

print(students)
print(students[3])
print(len(students))

# changing list
students[2]= 'Eyuti'
print(students)

# append
students.append('Alemitu')
print(students)

#insert
students.insert(2 , "Hailemeskel")
print(students)


# extend
numbers.extend([23,24])
print(numbers)

#REMOVE
numbers.remove(23)

#pop
numbers.pop()
print(numbers)
numbers.pop(3)

# delet
del numbers[4]
print(numbers)

# slicing
print(numbers[1:3])

# sorted
sorted_numbers= sorted(numbers)
print(sorted_numbers)
print(numbers)

# sort ascending
numbers.sort()
print(numbers)
students.sort()
print(students)

 # sort descending
numbers.sort(reverse =True)
print(numbers)

# reverse
students.reverse()
print(students)
print(students.index('Eyuti'))

# clear
numbers.clear()
print(numbers)
