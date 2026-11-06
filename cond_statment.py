score = 78

# if... else
if score >= 50:
    print("very good")
else:
    print("bad result")


# if..elif..else
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 50:
    print("D")
else:
    print("F")


# and
attendance = 90
if score > 50 and attendance > 80:
    print('Accepted for final exam')
else:
    print(' Not Accepted for final exam')


 # or
if score > 80 or attendance > 50:
    print('Accepted for final exam')
else:
    print(' Not Accepted for final exam') 


    # not
is_student= False
if not is_student:
    print("Can not enter the campas")

    # nested if
if score > 60:
    if attendance > 80:
        print('Accepted for final exam')
else:
    print(' Not Accepted for final exam')


    # compaire
language = "PythoN"
if language.lower() == "python":
    print("matched")
else:
    print("not matched")

     

   
