
from function import BookFunction
from function import MagazineFunction
from function import DVDFunction
from function import CDFunction

bookfunc=BookFunction()
magfunc=MagazineFunction()
dvdfunc=DVDFunction()
cdfunc=CDFunction()

def mainmenu():
    print("\n\nWelcome", name,
      "to our university library, where a treasure trove of knowledge awaits!")
    print("_________________________________________________________________________")
    print("_________________________________________________________________________")
    print("\nEnter the number of the option you want to select")
    print("1 - Books")
    print("2 - Magazines")
    print("3 - Educational DVDs")
    print("4 - Lecture CDs")
    print("0 - Exit")
    select_main = 1
    while select_main > 0:
        select_main = int(input("\n\nEnter your selection : "))
        if select_main == 0:
            print(
                "\n\nThank You for using our system\nYou are now succesfully exit from our library system")
            print("._____________________________________________________________.")

        elif select_main == 1:
            bookmenu()
            break
        elif select_main == 2:
            magmenu()
            break
        elif select_main == 3:
            dvdmenu()
            break
        elif select_main == 4:
            cdmenu()
            break
        else:
            print("\nInvalid input")


def bookmenu():
    select_book = 1
    while select_book > 0:
        print("\n\nYou have selected the book option\n")
        print("1 - Add Book(s)")
        print("2 - Remove Book(s)")
        print("3 - View all Books")
        print("4 - View available Books")
        print("5 - View unavailable Books")
        print("6 - Lend Book(s)")
        print("7 - Receive Book(s)")
        print("8 - Search by subject")
        print("0 - Back to Mainmenu")
        select_book = int(
            input("\nEnter the number of the option you want to select : "))
        if select_book == 1:
            bookfunc.add()
        elif select_book == 2:
            bookfunc.remove()
        elif select_book == 3:
            bookfunc.all()
        elif select_book == 4:
            bookfunc.available()
        elif select_book == 5:
            bookfunc.unavailable()
        elif select_book == 6:
            bookfunc.lend()
        elif select_book == 7:
            bookfunc.receive()
        elif select_book == 8:
            bookfunc.search()
        elif select_book == 0:
            mainmenu()
        else:
            print("Invalid input")


def magmenu():
    select_mag = 2
    while select_mag > 0:
        print("\n\nYou have selected the magazine option\n")
        print("1 - Add Magazine(s)")
        print("2 - Remove Magazine(s)")
        print("3 - View all Magazines")
        print("4 - View available Magazines")
        print("5 - View unavailable Magazines")
        print("6 - Lend Magazine(s)")
        print("7 - Receive Magazine(s)")
        print("8 - Search by subject")
        print("0 - Back to Mainmenu")
        select_mag = int(
            input("\nEnter the number of the option you want to select : "))
        if select_mag == 1:
            magfunc.add()
        elif select_mag == 2:
            magfunc.remove()
        elif select_mag == 3:
            magfunc.all()
        elif select_mag == 4:
            magfunc.available()
        elif select_mag == 5:
            magfunc.unavailable()
        elif select_mag == 6:
            magfunc.lend()
        elif select_mag == 7:
            magfunc.receive()
        elif select_mag == 8:
            magfunc.search()
        elif select_mag == 0:
            mainmenu()
        else:
            print("Invalid input")


def dvdmenu():
    select_dvd = 3
    while select_dvd > 0:
        print("\n\nYou have selected the Educational DVD option\n")
        print("1 - Add DVD(s)")
        print("2 - Remove DVD(s)")
        print("3 - View all DVDs")
        print("4 - View available DVDs")
        print("5 - View unavailable DVDs")
        print("6 - Lend DVD(s)")
        print("7 - Receive DVD(s)")
        print("8 - Search by subject")
        print("0 - Back to Mainmenu")
        select_dvd = int(
            input("\nEnter the number of the option you want to select : "))
        if select_dvd == 1:
            dvdfunc.add()
        elif select_dvd == 2:
            dvdfunc.remove()
        elif select_dvd == 3:
            dvdfunc.all()
        elif select_dvd == 4:
            dvdfunc.available()
        elif select_dvd == 5:
            dvdfunc.unavailable()
        elif select_dvd == 6:
            dvdfunc.lend()
        elif select_dvd == 7:
            dvdfunc.receive()
        elif select_dvd == 8:
            dvdfunc.search()
        elif select_dvd == 0:
            mainmenu()
        else:
            print("Invalid input")


def cdmenu():
    select_cd = 4
    while select_cd > 0:
        print("\n\nYou have selected the Lecture CD option\n")
        print("1 - Add CD(s)")
        print("2 - Remove CD(s)")
        print("3 - View all CD")
        print("4 - View available CD")
        print("5 - View unavailable CD")
        print("6 - Lend CD(s)")
        print("7 - Receive CD(s)")
        print("8 - Search by subject")
        print("0 - Back to Mainmenu")
        select_cd = int(
            input("\nEnter the number of the option you want to select : "))
        if select_cd == 1:
            cdfunc.add()
        elif select_cd == 2:
            cdfunc.remove()
        elif select_cd == 3:
            cdfunc.all()
        elif select_cd == 4:
            cdfunc.available()
        elif select_cd == 5:
            cdfunc.unavailable()
        elif select_cd == 6:
            cdfunc.lend()
        elif select_cd == 7:
            cdfunc.receive()
        elif select_cd == 8:
            cdfunc.search()
        elif select_cd == 0:
            mainmenu()
        else:
            print("Invalid input")


name = input("\n\n\nEnter your name: ")
mainmenu()


