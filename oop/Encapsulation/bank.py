class BankAccount:
    
    def __init__(self,owner,balance):
        self.owner =owner
        self.__balance =balance
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self ,amount):
        if amount > 0:
            
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Amount can not be negative")
            
    def withdraw(self,amount):
        if amount < 0:
            print("Amount can not be negative")
            
        elif amount > self.__balance:
            print("Insufficent balance.")
        else:
            self.__balance -=amount
            print("Withdraw successful.")
            
    def desplayInfo(self):
        print(f"Owner: {self.owner}")
        print(f"balance: {self.__balance}")


user1 =BankAccount("Eyob",20000 )
# print(user1.get_balance())      
# print(user1.owner)               
# user1.desplayInfo()
          
user1.deposit(1000)
# user1.desplayInfo()

user1.withdraw(500)
# user1.desplayInfo() 
         
user1.deposit(-3000)
print(user1.get_balance())      

user1.withdraw(100000)
print(user1.get_balance())      
        
         
          