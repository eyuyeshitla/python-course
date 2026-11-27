marks =[]
for i in range(5):
    mark =int(input(f"Enter mark for subject  {i +1}:"))
    
    marks.append(mark)
print(marks)

total =sum(marks)
average = total/ len(marks)
maximum =max(marks)
minimum =min(marks)