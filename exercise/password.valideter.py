user_name ="Eyu@12"
password ="Haile123"

username=input("Enter username:")
enterd_password =input("Enter password:")

if user_name == username and password ==enterd_password:
    print("Login successfully.")
    
elif user_name == username and password != enterd_password:
    print("incorrect password.")
    
    
else:
    print("User not found.")
    

