class Book:
    def __init__(self, isbn_No, title, format, subject, rental, copies):
        self.isbn_No = isbn_No
        self.title = title
        self.format = format
        self.subject = subject
        self.rental = rental
        self.copies = copies


class Magazine:
    def __init__(self, magazine_No, title, feature, subject, rental, copies):
        self.magazine_No = magazine_No
        self.title = title
        self.feature = feature
        self.subject = subject
        self.rental = rental
        self.copies = copies
    
class Educational_DVD:
    def __init__(self, DVD_Number, title, subject, rental, copies):
        self.DVD_Number = DVD_Number
        self.title = title
        self.subject = subject
        self.rental = rental
        self.copies = copies


class Lecture_CD:
    def __init__(self, CD_Number, title, subject, rental, copies):
        self.CD_Number = CD_Number
        self.title = title
        self.subject = subject
        self.rental = rental
        self.copies = copies

def printInfoB(book):
    print(f"ISBN NO: {book.isbn_No}, Title: {book.title}, Format: {book.format}, Subject: {book.subject}, Rental Price: {book.rental}, Available Copies: {book.copies}")

def printInfoM(magazine):
    print(f"Magazine NO: {magazine.magazine_No}, Title: {magazine.title}, Format: {magazine.feature}, Subject: {magazine.subject}, Rental Price: {magazine.rental}, Available Copies: {magazine.copies}")

def printInfoE(Dvd):
    print(f"Educational DVD NO: {Dvd.DVD_Number}, Title: {Dvd.title}, Subject: {Dvd.subject}, Rental Price: {Dvd.rental}, Available Copies: {Dvd.copies}")

def printInfoL(Cd):
    print(f"Lecture CD NO: {Cd.CD_Number}, Title: {Cd.title}, Subject: {Cd.subject}, Rental Price: {Cd.rental}, Available Copies: {Cd.copies}")

#bookfunction
class BookFunction:
    def __init__(self):
        self.BookList=[]
        self.data()

    def data(self):
        book01=Book(isbn_No="ISBN1234",title="The Solar System", format="Harcover", subject="Science", rental=15.00, copies=5)
        book02=Book(isbn_No="ISBN9876",title="Type of Animal Species", format="Paperback", subject="Science", rental=10.00, copies=8)
        book03=Book(isbn_No="ISBN1290",title="Second World War", format="Hardcover", subject="History", rental=12.50, copies=1)
        self.BookList.append(book01)
        self.BookList.append(book02)
        self.BookList.append(book03)

    def add(self):
        isbn=input("Enter ISBN Number : ").strip().upper()
        title1=input("Title of book : ")
        format1=input("Book Format (Harcover/Paperback) : ")
        subject1=input("Subject of the Book : ")
        rental1=float(input("Rental per day : "))
        copies1=int(input("How many copies available : "))
        book0= Book(isbn_No=isbn, title=title1, format=format1, subject=subject1,rental=rental1,copies=copies1)
        self.BookList.append(book0)
        print("Book added Succesfully")

    def remove(self):
        isbn=input("Enter a valid ISBN Number : ").strip().upper()
        matching=list(x for x in self.BookList if x.isbn_No==isbn)
        for x in matching:
            self.BookList.remove(x)
            print("Book Removed Succesfully")

    def all(self):
        for x in self.BookList:
            printInfoB(book=x)

    def available(self):
        matching=list(x for x in self.BookList if x.copies>0)
        for x in matching:
            printInfoB(book=x)

    def unavailable(self):
        matching=list(x for x in self.BookList if x.copies==0)
        for x in matching:
            printInfoB(book=x)

    def lend(self):
        isbn=input("Enter ISBN Number: ")
        copies1=int(input("How many copies yo want to lend: "))
        matching=list(x for x in self.BookList if x.isbn_No ==isbn)
        for x in matching:
            x.copies-=copies1
            print("You have lend book(s) succesfully")

    def receive(self):
        isbn=input("Enter ISBN Number: ")
        copies=int(input("How many copies you want to receive: "))
        matching=list(x for x in self.BookList if x.isbn_No == isbn)
        for x in matching:
            x.copies+=copies
            print("You have received book(s) succesfully")

    def search(self):
        subject1=input("Enter the subject (Science / History / Literature): ")
        matching=list(x for x in self.BookList if x.subject==subject1)
        for x in matching:
            printInfoB(book=x)


#Magazine function
class MagazineFunction:
    def __init__(self):
        self.MagazineList=[]
        self.data()

    def data(self):
        mag01=Magazine(magazine_No="01",title="History of Cricket", feature="color print", subject="Sports", rental=5.00, copies=7)
        mag02=Magazine(magazine_No="02",title="Evolution of the Computer", feature="black&white print", subject="Technology", rental=3.00, copies=21)
        self.MagazineList.append(mag01)
        self.MagazineList.append(mag02)

    def add(self):
        mag=input("Enter Magazine Number : ").strip().upper()
        title1=input("Title of Magazine : ")
        feature1=input("Magazine feature (color print/black&white print) : ")
        subject1=input("Subject of the Magazine : ")
        rental1=float(input("Rental per day : "))
        copies1=int(input("How many copies available : "))
        mag0= Magazine(magazine_No=mag, title=title1, feature=feature1, subject=subject1,rental=rental1,copies=copies1)
        self.MagazineList.append(mag0)
        print("Magazine added Succesfully")

    def remove(self):
        mag=input("Enter a valid Magazine Number : ")
        matching=list(x for x in self.MagazineList if x.magazine_No==mag)
        for x in matching:
            self.MagazineList.remove(x)
            print("Magazine Removed Succesfully")

    def all(self):
        for x in self.MagazineList:
            printInfoM(magazine=x)

    def available(self):
        matching=list(x for x in self.MagazineList if x.copies>0)
        for x in matching:
            printInfoM(magazine=x)

    def unavailable(self):
        matching=list(x for x in self.MagazineList if x.copies==0)
        for x in matching:
            printInfoM(magazine=x)

    def lend(self):
        mag=input("Enter Magazine Number: ")
        copies1=int(input("How many copies yo want to lend: "))
        matching=list(x for x in self.MagazineList if x.magazine_No ==mag)
        for x in matching:
            x.copies-=copies1
            print("You have lent magazine(s) succesfully")

    def receive(self):
        mag=input("Enter Magazine Number: ")
        copies=int(input("How many copies you want to receive: "))
        matching=list(x for x in self.MagazineList if x.magazine_No == mag)
        for x in matching:
            x.copies+=copies
            print("You have received magazine(s) succesfully")
 
    def search(self):
        subject1=input("Enter the subject )(Science / Technology / Sports): ")
        matching=list(x for x in self.MagazineList if x.subject==subject1)
        for x in matching:
            printInfoM(magazine=x)

#Educational DVD Function
class DVDFunction:
    def __init__(self):
        self.DVDList=[]
        self.data()

    def data(self):
        dvd01=Educational_DVD(DVD_Number="10",title="Birth of the Solar System", subject="Astronomy", rental=2.50, copies=10)
        dvd02=Educational_DVD(DVD_Number="11",title="Pythagoras Theorem", subject="Math", rental=1.00, copies=50)
        self.DVDList.append(dvd01)
        self.DVDList.append(dvd02)

    def add(self):
        dvd=input("Enter the DVD Number : ").strip().upper()
        title1=input("Title of DVD : ")
        subject1=input("Subject of the DVD : ")
        rental1=float(input("Rental per day : "))
        copies1=int(input("How many copies available : "))
        dvd= Educational_DVD(DVD_Number=dvd, title=title1, subject=subject1,rental=rental1,copies=copies1)
        self.DVDList.append(dvd)
        print("DVD added Succesfully")

    def remove(self):
        dvd=input("Enter a valid DVD Number : ")
        matching=list(x for x in self.DVDList if x.DVD_Number==dvd)
        for x in matching:
            self.DVDList.remove(x)
            print("DVD Removed Succesfully")

    def all(self):
        for x in self.DVDList:
            printInfoE(Dvd=x)

    def available(self):
        matching=list(x for x in self.DVDList if x.copies>0)
        for x in matching:
            printInfoE(Dvd=x)

    def unavailable(self):
        matching=list(x for x in self.DVDList if x.copies==0)
        for x in matching:
            printInfoE(Dvd=x)

    def lend(self):
        dvd=input("Enter DVD Number: ")
        copies1=int(input("How many copies yo want to lend: "))
        matching=list(x for x in self.DVDList if x.DVD_Number ==dvd)
        for x in matching:
            x.copies-=copies1
            print("You have lend DVD(s) succesfully")

    def receive(self):
        dvd=input("Enter DVD Number: ")
        copies=int(input("How many copies you want to receive: "))
        matching=list(x for x in self.DVDList if x.DVD_Number == dvd)
        for x in matching:
            x.copies+=copies
            print("You have received DVD(s) succesfully")

    def search(self):
        subject1=input("Enter the subject (Astronomy / Math / Technology): ")
        matching=list(x for x in self.DVDList if x.subject==subject1)
        for x in matching:
            printInfoE(Dvd=x)



#Lecture CD Function
class CDFunction:
    def __init__(self):
        self.CDList=[]
        self.data()

    def data(self):
        cd01=Lecture_CD(CD_Number="21",title="Basics of Western Music", subject="Music", rental=1.50, copies=11)
        cd02=Lecture_CD(CD_Number="22",title="Japanese Language", subject="Foreign Languages", rental=2.00, copies=3)
        self.CDList.append(cd01)
        self.CDList.append(cd02)

    def add(self):
        cd=input("Enter the CD Number : ")
        title1=input("Title of CD : ")
        subject1=input("Subject of the CD : ")
        rental1=float(input("Rental per day : "))
        copies1=int(input("How many copies available : "))
        cd= Lecture_CD(CD_Number=cd, title=title1, subject=subject1,rental=rental1,copies=copies1)
        self.CDList.append(cd)
        print("CD added Succesfully")

    def remove(self):
        cd=input("Enter a valid CD Number : ")
        matching=list(x for x in self.CDList if x.CD_Number==cd)
        for x in matching:
            self.CDList.remove(x)
            print("CD Removed Succesfully")

    def all(self):
        for x in self.CDList:
            printInfoL(Cd=x)

    def available(self):
        matching=list(x for x in self.CDList if x.copies>0)
        for x in matching:
            printInfoL(Cd=x)

    def unavailable(self):
        matching=list(x for x in self.CDList if x.copies==0)
        for x in matching:
            printInfoL(Cd=x)

    def lend(self):
        cd=input("Enter CD Number: ")
        copies1=int(input("How many copies yo want to lend: "))
        matching=list(x for x in self.CDList if x.CD_Number ==cd)
        for x in matching:
            x.copies-=copies1
            print("You have lend CD(s) succesfully")

    def receive(self):
        cd=input("Enter CD Number: ")
        copies=int(input("How many copies you want to receive: "))
        matching=list(x for x in self.CDList if x.CD_Number == cd)
        for x in matching:
            x.copies+=copies
            print("You have received CD(s) succesfully")

    def search(self):
        subject1=input("Enter the subject (Music / Math/ Foreign Languages): ")
        matching=list(x for x in self.CDList if x.subject==subject1)
        for x in matching:
            printInfoL(Cd=x)


