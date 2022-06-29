#customer class to store about customer data
class customerType:
    def __init__(self, firstname, lastname, accNo, listdvdrent):
        self.__firstname=firstname
        self.__lastname=lastname
        self.__accNo=accNo
        self.__listdvdrent=listdvdrent

#set getter and setter
    def set_firstname(self, firstname):
        self.__firstname=firstname

    def get_firstname(self):
        return self.__firstname

    def set_lastname(self, lastname):
        self.__lastname=lastname

    def get_lastname(self):
        return self.__lastname

    def set_accNo(self, accNo):
        self.__accNo=accNo

    def get_accNo(self):
        return self.__accNo

    def set_lisdvdrent(self, listdvdrent):
        self.__listdvdrent=listdvdrent

    def get_listdvdrent(self):
        return self.__listdvdrent

    def __eq__(self,other):
        return self.__accNo == other.__accNo

    def __lt__(self,other):
        return self.__accNo < other.__accNo

    def __le__(self,other):
        return self.__accNo <= other.__accNo

    def __gt__(self,other):
        return self.__accNo > other.__accNo

    def __ge__(self,other):
        return self.__accNo >= other.__accNo

    def __str__(self):

        return f'First name:{self.__firstname}\n'+\
               f'Last name:{self.__lastname}\n'+\
               f'Account number:{self.__accNo}'



    def printDetails(self):
        print('Name of customer:', self.__firstname+' '+self.__lastname)
        print('Customer Account Number:',self.__accNo)
        for item in self.__listdvdrent:
            print(item.get_title())