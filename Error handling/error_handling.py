try:
    number =input("Enter the number:")
    print(100 / number)

except TypeError:
    print("Type error")

except ValueError:
    print("invalid input")

except ZeroDivisionError:
    print("can not divided by zero")
else:
    print("division succesfully")
finally:
    print("program finished")    