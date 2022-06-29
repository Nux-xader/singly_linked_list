import customertype, linklist, dvdtype, bstcust


def get_menu_choice1():
    print()
    print('menu for customer')
    print('------------------------------')
    print('1. check dvd availability in store.')
    print('2. rent dvd.')
    print('3. return dvd.')
    print('4. check the particular dvd is available for borrowing.')
    print('5. list all the dvd titles.')
    print('6. list all details the dvds.')
    print('7. exit.')
    print('-------------------------------')
    print()

       
def run_menu_choice1():
    option1 = 0
    while option1 !=7:
        option1 = int(input('enter 1-7 to choose : '))
        if option1 == 1:
            title = str(input("input title : "))
            check_dvd_exists(title)
        elif option1 ==2:
            title = str(input("input title : "))
            checkout_dvd(title)
        elif option1 == 3:
            title = str(input("input title : "))
            checkin_dvd(title)
        elif option1 == 4:
            title = str(input("input title : "))
            checkforborrow_dvd(title)
        elif option1== 5:
            list_all_titles()
        elif option1 == 6:
            list_all_dvd_details()


def get_menu_choice2():
    print()
    print('menu for admin')
    print('-------------------------------')
    print('1. add the customer.')
    print('2. search the customer.')
    print('3. check customer details.')
    print('4. update customer details.')
    print('5. add dvd.')
    print('6. search dvd.')
    print('7. view all the dvds')
    print('8. updates dvd details')
    print('9. exit')
    print('-------------------------------')
    print()


def run_menu_option2():
    option2 = 0
    while option2 !=9:
        option2 = int(input('enter 1-9 to choose : '))
        if option2 == 1:
            add_customer()
        elif option2 ==2:
            search_customer()
        elif option2 == 3:
            check_customer_deatils()
        elif option2 == 4:
            update_customer_deatils()
        elif option2 == 5:
            add_dvd()
        elif option2 == 6:
            search_dvd()
        elif option2 ==7:
            list_all_dvd_details()
        elif option2 == 8:
            update_dvd()


def update_dvd():
    global DVDstock
    title = str(input("Input title : "))
    found = False
    for std in DVDstock.get_list():
        if std.get_title() == title:
            found = True
            std.set_title(str(input("New title : ")))
            std.set_star1(str(input("New Star 1 : ")))
            std.set_star2(str(input("New star 2 : ")))
            std.set_producer(str(input("New Producer : ")))
            std.set_director(str(input("New Director : ")))
            std.set_prodCo(str(input("New production by : ")))
            std.set_noofDVDs(str(input("New DVD amount : ")))
            break

    if not found: print('this dvd doesnot exist')


def search_dvd():
    global DVDstock
    title = str(input("Input title : "))
    found = False
    for std in DVDstock.get_list():
        if std.get_title() == title:
            print('-------------------------------')
            print(std)
            print('-------------------------------')
            found = True
            break
    if not found: print('this dvd doesnot exist')


def add_dvd():
    global DVDstock
    titlenew = str(input("Title : "))
    star1new = str(input("Star 1 : "))
    star2new = str(input("Star 2 : "))
    producernew = str(input("Producer : "))
    directornew = str(input("Director : "))
    prodcomnew = str(input("Production by : "))
    nonew = int(input("DVD Amount : "))
    DVDstock.insert(dvdtype.dvdType(titlenew, star1new, star2new, producernew, directornew, prodcomnew, nonew))


def update_customer_deatils():
    global DVDstock, CustomerList
    firstname = str(input("First name : "))
    lastname = str(input("Last name : "))
    found = False
    for customer in CustomerList.get_list():
        if (customer.get_firstname() == firstname) and (customer.get_lastname() == lastname):
            found = True
            print("Customer found")
            customer.set_firstname(str(input("New first name : ")))
            customer.set_lastname(str(input("New last name : ")))
            customer.set_accNo(str(input("New account number : ")))
            dvd_customer = []
            if str(input("Add dvd? (y): ")).lower() == "y":
                dvd_found = False
                while True:
                    title = str(input("input dvd title : "))
                    for dvd in DVDstock.get_list():
                        if dvd.get_title() == title:
                            dvd_found = True
                            dvd_customer.insert(dvd)
                            break
                    if dvd_found: break
                    else: print("Dvd not found!")
                customer.set_lisdvdrent(dvd_customer)
            break

    if not found: print("Customer not found!")


def check_customer_deatils():
    global CustomerList
    firstname = str(input("First name : "))
    lastname = str(input("Last name : "))
    found = False
    for customer in CustomerList.get_list():
        if (customer.get_firstname() == firstname) and (customer.get_lastname() == lastname):
            found = True
            print('-------------------------------')
            print(customer)
            print("DVD Rent : ")
            [print(f"  - {dvd.get_title()}") for dvd in customer.get_listdvdrent()]
            print('-------------------------------')
            break

    if not found: print("Customer not found!")



def search_customer():
    global CustomerList
    firstname = str(input("First name : "))
    lastname = str(input("Last name : "))
    found = False
    for customer in CustomerList.get_list():
        if (customer.get_firstname() == firstname) and (customer.get_lastname() == lastname):
            found = True
            print("Customer Found")

    if not found: print("Customer not found!")


def add_customer():
    global CustomerList
    firstname = str(input("First name : "))
    lastname = str(input("Last name : "))
    accNo = str(input("Account number : "))
    CustomerList.insert(customertype.customerType(firstname, lastname, accNo, []))


def list_all_dvd_details():
    global DVDstock
    [print(f'-------------------------------\n{std}') for std in DVDstock.get_list()]
    print('-------------------------------')


def check_dvd_exists(title):
    global DVDstock
    found = False
    for item in DVDstock.get_list():
        if item.get_title() == title:
            found = True
            print("DVD Exist")
            break
    if not found: print("DVD not Exist")


           
def checkout_dvd(title):
    global DVDstock
    found = False
    for val in DVDstock.get_list():
        if val.get_title() == title:
            found = True
            print('Item is found')
            n = val.get_noofDVDs()
            print('dvd available for rent', n)
            if n > 0:
                val.checkout()
                print('updates of numbers dvd available:', val.get_noofDVDs())
            else:
                print('This DVD not available at the moment, please come back again next time')
            break
    if not found: print(f"DVD with title : {title} not found")



#return dvd/checkin dvd
def checkin_dvd(title):
    global DVDstock
    found = False
    for val in DVDstock.get_list():
        if val.get_title() == title:
            print('item is avalaible in the library')
            found = True
            n = val.get_noofDVDs()
            print('current of dvd in stock:', n)
            val.checkin()
            x = val.get_noofDVDs()
            print('updates no of dvds after check-in:',x)
            break

    if not found: print('this dvd doesnot exist')

    
#check dvd availability to borrow
def checkforborrow_dvd(title):
    global DVDstock
    found = False
    for item in DVDstock.get_list():
        if item.get_title() == title:
            print('Item found')
            found = True
            n = item.get_noofDVDs()
            if n > 0: print('No copies is available:', n)
            else: print('Sorry, but no copies available')
            break
    
    if not found: print('This copies does not available')


# get list dvd title           
def list_all_titles():
    global DVDstock
    print('-------------------------------')
    [print(f'Title : {std.get_title()}') for std in DVDstock.get_list()]
    print('-------------------------------')



def main():
    global DVDstock, CustomerList

    DVDstock, CustomerList = linklist.LinkedList(), linklist.LinkedList()
    for line in [i for i in str(open('dvd_list.txt', 'r').read()).split("\n") if len(i) > 6]:
        columns = line.split(',')
        titlenew = columns[0]
        star1new = columns[1]
        star2new = columns[2]
        producernew = columns[3]
        directornew = columns[4]
        prodcomnew = columns[5]
        nonew = int(columns[6])
        DVDstock.insert(dvdtype.dvdType(titlenew, star1new, star2new, producernew, directornew, prodcomnew, nonew))

    for line in [i for i in str(open('list_customer.txt', 'r').read()).split("\n") if len(i) > 5]:
        columns = line.split(', ')
        firstname = columns[0]
        lastname = columns[1]
        accNo = columns[2]
        CustomerList.insert(customertype.customerType(firstname, lastname, accNo, []))

    choice = int(input('Enter 1 to choose customer menu and 2 for Admin menu: '))
    if choice == 1:
        get_menu_choice1()
        run_menu_choice1()
    elif choice == 2:
        get_menu_choice2()
        run_menu_option2()
    else:
        print("Pilihan salah")


#call the main function
if __name__=='__main__':
    main()
