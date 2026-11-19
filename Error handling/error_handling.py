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

def deposit(amount):
    if amount < 0:
        raise ValueError("Amount can not be lessthan zero")
    else:
        print("deposit success")

# deposit(-6)
deposit(50)


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive.")

    if amount > balance:
        raise ValueError("Insufficient balance.")

    return balance - amount


print(withdraw(1000, 3000))