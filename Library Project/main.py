class Library:
    bookdict=dict()
    numdict=dict()
    def __init__(self,name,li):
        self.booklist=li
        self.name=name
        for item in self.booklist:
            self.bookdict[item]=[]
            if self.numdict.get(item)==None:
                self.numdict[item]=0
            self.numdict[item]+=1
    def display(self):
        for key,value in self.numdict.items():
            print(f"{key}  :  {value}")
    def lend(self,lendername,bookname):
        if bookname not in self.booklist:
            print("No such book is there in our library to lend \n")
        elif self.numdict.get(bookname)==0:
            print("This book is not available , it is lended to ",self.bookdict.get(bookname))
        else:
            self.bookdict[bookname]+=[lendername]
            self.numdict[bookname]-=1
    def add(self,bookname):
        self.bookdict[bookname]=[]
        if self.numdict.get(bookname)==None:
            self.numdict[bookname]=0
        self.numdict[bookname]+=1
    def retbook(self,bookname,lendername):
        try:
            self.bookdict.get(bookname).remove(lendername)
            self.numdict[bookname]+=1
        except:
            print("Please check again lender name or bookname something is going wrong.")

if __name__ == "__main__":
    l=["A","B","C","D","E","F","G","A","B","C","A"]
    # we can alse use xlsx file format for entering books in library and use pandas to read via it .
    lib=Library("Nitish",l)
    while True:
        print()
        print(f"Enter query you want to do in Nitish Library :\nadd : to add new book to library \ndisplay : to display list of all books \nlend : to issue a book \nreturn : to return a issued book \nquit to quit this process")
        print()
        q=input()
        if q=="add":
            print("Enter name of new book")
            nb=input()
            lib.add(nb)
        elif q=="display":
            print("List of name and number of books available in library are :")
            lib.display()
        elif q=="lend":
            print("Enter your name :")
            name=input()
            print("Enter name of book you want to issue :")
            bookname=input()
            lib.lend(name,bookname)
        elif q=="return":
            print("Enter your name :")
            lendername=input()
            print("Enter name of book you want to return :")
            name=input()
            lib.retbook(name,lendername)
        elif q=="quit":
            break
