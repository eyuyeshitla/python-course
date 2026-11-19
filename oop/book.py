class Book:


    def __init__ (self, t, a, y):
        self.title = t
        self.author = a
        self.year = y


    def displayInfo(self):
        print(f"title: {self.title} ")
        print(f"author: {self.author} ")
        print(f"year: {self.year} ")


    def check_year(self):
        if self.year < 2000:
            print("old")
        else:
            print("new")

        

book1 = Book("chemistry","Eyuka",1994)
book1.displayInfo()

print(book1.author)
book1.check_year()

book2 = Book("sememen","Sisay Ngusu",1977)
book2.displayInfo()
print(book2.title)
book2.check_year()

book3= Book("Fkr eske mekabr","Hadisalemayehu",1958)
book3.displayInfo()
book3.check_year()



        
        