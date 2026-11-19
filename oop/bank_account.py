class BankAccount:


    def __init__(self,name, number, balance):
            self.name= name
            self.number = number
            self.balance=balance

        
    def ditail_info(self):
          print(f"name: {self.name} ")
          print(f"number: {self.number} ")
          print(f"balance: {self.balance} ")


user1 = BankAccount("Haile",1000576890342,100000)
user1.ditail_info()


            