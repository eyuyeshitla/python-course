class DigitalWallet:
    
    def __init__(self,owner,balance):
        self.name = owner
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
        
    def add_money(self ,amount):
        if amount < 0:
            print("Can not deposit")
        else:
            self.__balance +=amount
            print("Deposit successfully.")
            
    def spend_money(self,amount):
        if amount < 0:
            print("You can not withdraw")
        elif amount > self.__balance:
            print("Insufffiecent balance.")
        else:
            self.__balance -=amount
            print("withdraw successfully.")
            
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"balance: {self.__balance}")
        
        
user2 =DigitalWallet("Alemu",3000)
user2.display_info()    
user2.add_money(800)    
user2.spend_money(-800)
user2.display_info()
print(user2.get_balance())    

        
        
        