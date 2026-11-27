from oprations import add, multiply, divide, subtract


def calculate():
     
    try:
        
        c =menu()
        
        number1 = int(input("Enter the number1:"))
        number2 = int(input("Enter the number2:"))
        
        if c == 1:
            
             result =add(number1,number2)
             print("Result:",result)
             
        elif c == 2:
              result =multiply(number1,number2)
              print("Result:",result)
        elif c ==3:
              result =divide(number1,number2)
              print("Result:",result)
        elif c ==4:
                result =subtract(number1,number2)
                print("Result:",result)
              
        else:
            print("Invalid choice.")
            
        
    except ValueError:
        print("value Error.")
    except ZeroDivisionError:
        print("Can not divided by zero.")
    finally:
        print("Completed.")
        

def menu():
    print("1. add number")
    print("2. multiply number")
    print("3. divide number")  
    print("4. substract number") 
    
    choice = int(input("Enter your choice:"))
    return choice
    
      
calculate()
        