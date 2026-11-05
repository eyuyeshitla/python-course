# creat tuple
data= ('eyu',23,21.12 , False )
print(data)

student= ('haile',23,'software enginering',12.16)
print(student)

number= (10)
print(number)
print(type(number))

number= (10,)
print(number)
print(type(number))


#empty tuple
empty_tuple= ()
print(empty_tuple)
print(type(empty_tuple))

firuts= 'mango','banana', 'orange'
print(firuts)
print(type(firuts))
languages=('Amharic',"English",'spanish')
print(languages[1])
print(languages[2])
print(languages[-1])
print(languages[-2])
print(languages[::-1])

# unpacking
language1, language2, language3 = languages
print(language2)

# casting tuple to list
languages_list= list(languages)
print(languages_list)



students= 'yene','eyu','yared','netsi'
print(len(students))
students= students + ("my father",)
print(students)

# other oprations
numbers= (1,2,3,40,3)
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(numbers *2)
print(20 in numbers)
print(numbers.count(3))

students= (('haile',23,'software enginering',12.16  ) ,('eyu',23,21.12 , False ))
print(students[1])
print(students[1][0])

 # add item in directly
x = ('banana','orange', 'apple')
y= list(x)
y.append('mango')
x= tuple(y)
print(x)




