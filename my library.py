class Library:
    def __init__(self,list,name):
        self.booklists = list
        self.name = name
        self.Bookdict = {}
    def displayBook(self):
        print(f"We have following book in our library -- {self.name}")
        for book in self.booklists:
            print(book)
    def addBook(self,book):
        self.booklists.append(book)
    def returnBook(self,book):
        self.booklists.remove(book)
        
if __name__ == '__main__':
    suraj = Library(["Python","R","C++"],"indian_lab")
    while True:
        print(f"Wellcome to {suraj.name} ,The best labrary in india.")
        print("1. Display the book.")
        print("2. Add the book.")
        print("3. Return the book.")
        print("4. Exit")
        user_choise = input("Enter your choise : ")
        if user_choise == "1":
            suraj.displayBook()
        elif user_choise == "2":
            book = input("Enter the book name :")
            suraj.addBook(book)
            print("Book has been added.")
        elif user_choise == "3":
            book = input("Enter the book name :")
            suraj.returnBook(book)
            print("Book has been returned.")
        elif user_choise == "4":
            exit()
        else:
            print("Wrong entry. Try again...")
            continue
        while True:
            user_choise2 = input("Enter 'c' to countinue and 'q' to quit.")
            if user_choise2 == "c":
                break
            elif user_choise2 == "q":
                exit()
            