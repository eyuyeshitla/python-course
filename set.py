students = {'Abebe', 'Kebede', "Abebe", "Aster" ,"Chalitu"}
numbers = {12,23,34,56,78,90,23}
numbers2 = {12,23,35,56,79,90,23}

print(students)
print(len(students))
# ADD
numbers.add(57)
print(numbers)

# update
numbers.update({1,2,3,4})
print(numbers)
# menbership
print(80 in numbers)
# remove
numbers.remove(90)
print(numbers)

# pop
numbers.pop()
print(numbers)
# discard
numbers.discard(78)
print(numbers)

# casting
print(set([9,8,7,6,5]))

# others
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

# union
print(numbers | numbers2)
# intersection

print(numbers & numbers2)
# symetric diffrence
print(numbers ^ numbers2)

# clear
numbers.clear()
print(numbers)