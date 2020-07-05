class Library():
    def __init__(self,booklist,name):
        self.booklist = booklist
        self.bookdata = {}
        self.name = name
    
    def addbook(self,name):
        self.booklist.append(name)
        print(f'{name} successfully added')
    
    def displaybook(self):
        print("Books in Library are")
        for index, item in enumerate(self.booklist):
            print(f'{index + 1} -------> {item}')
        print()
    
    def displaylendedbook(self):
        print("Lended Books are")
        for names, lists in self.bookdata.items():
            print(names, '-------> ',lists)
        print()
    
    def lendbook(self,bkname,lendername):
        if bkname in self.booklist:
            self.booklist.remove(bkname)
            if lendername not in self.bookdata:
                self.bookdata[lendername] = []
            self.bookdata[lendername].append(bkname)
            print(f"'{bkname}' successfully lended to {lendername}")
        else:
            print('No such book found')
    
    def returnbook(self,bkname,lendername):
        if lendername in self.bookdata:
            for values in self.bookdata.values():
                if bkname in values:
                    values.remove(bkname)
                    self.booklist.append(bkname)
            print(f"'{bkname}' successfully returned by {lendername}")
        else:
            print('No such Lender exists')

if __name__ == "__main__":
    shaibazlib = Library(['errorless', 'HC verma', 'python' , 'webdev'],'shaibazlibrary')

    while True:
        print(f"Welcome to the {shaibazlib.name} library. Enter your choice to continue")
        print("1. Display All Available Books")
        print("2. Lend a Book")
        print("3. Display Lended Books")
        print("4. Add a Book")
        print("5. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4','5']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)
        
        if user_choice == 1:
            shaibazlib.displaybook()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: \t")
            user = input("Enter name of Lender: \t")
            shaibazlib.lendbook(book,user)
        
        elif user_choice == 3:
            shaibazlib.displaylendedbook()

        elif user_choice == 4:
            book = input("Enter the name of the book you want to add: \t")
            shaibazlib.addbook(book)

        elif user_choice == 5:
            book = input("Enter the name of the book you want to return: \t")
            user = input("Enter name of lender: \t")
            shaibazlib.returnbook(book,user)

        else:
            print("Not a valid option")
        
        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue
            else:
                print("Not a valid option")
    