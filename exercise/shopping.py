products = []

def addproduct():
    n = int(input("How many products do you want:"))
    
    for i in range(n):
    
        name =input(f"Enter name for product {i +1}:")
        price =int(input("Enter price:"))
        quantity =int(input("Enter quantity:"))

        product ={
            "name":name,
            "price":price,
            "quantity":quantity
        }

        products.append(product)
      
      
def calculate_total():
    total_price =0
    for product in products:
        total =product["price"] *product["quantity"]  
        total_price = total_price + total
       
    return total_price

def display_cart():
    print("\n====== Product list =========")
    
    print("Name  \t   Quantity  \t     Price")
    for product in products:
        print(f" {product["name"]} \t \t {product["quantity"]} \t \t {product["price"]}")  
        
addproduct()
print(calculate_total())
display_cart()
