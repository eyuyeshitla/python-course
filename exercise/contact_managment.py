n = int(input("How many contacts do you want:"))
contacts = {}
 
for contact in range(n):
    name =input("Enter your name:")
    phone =input("Enter your phone:")
    
    if phone in contacts.values():
        print("contacts already exist.")
    else:
        
      contacts[name] =phone

print("\n")

for name,phone in contacts.items():
    print(f"Name: {name}, Phone {phone}")
 


    