#dvd class stores data about the dvd
class dvdType:
    def __init__(self, title, star1, star2, producer, director, prodCo, noofDVDs):
        self.__title=title
        self.__star1=star1
        self.__star2=star2
        self.__producer=producer
        self.__director=director
        self.__prodCo=prodCo
        self.__noofDVDs=noofDVDs
#set getter and setter
    def set_title(self, title):
        self.__title=title

    def get_title(self):
        return self.__title

    def set_star1(self, star1):
        self.__star1=star1

    def get_star1(self):
        return self.__star1

    def set_star2(self, star2):
        self.__star2=star2

    def get_star2(self):
        return self.__star2

    def set_producer(self, producer):
        self.__producer=producer

    def get_producer(self):
        return self.__producer

    def set_director(self, director):
        self.__director=director

    def get_director(self):
        return self.__director

    def set_prodCo(self, prodCo):
        self.__prodCo=prodCo

    def get_prodCo(self):
        return self.__prodCo
    
    def set_noofDVDs(self, noofDVDs):
        self.__noofDVDs=noofDVDs

    def get_noofDVDs(self):
        return self.__noofDVDs

    
    def __str__(self):
#to print movie about detail
        return f'Title:{self.__title}\n'+\
               f'Starring:{self.__star1}\n'+\
               f'And:{self.__star2}\n'+\
               f'Producer:{self.__producer}\n'+\
               f'Director:{self.__director}\n'+\
               f'Production by:{self.__prodCo}\n'+\
               f'Dvd number:{self.__noofDVDs}'
               
#to check DVD availability 
    def checkout (self):
        if self.__noofDVDs > 0:
            self.__noofDVDs= self.__noofDVDs - 1
        else:
            print('Curently out of stock')

    def checkin(self):
        self.__noofDVDs = self.__noofDVDs+1

    def printDVDtitle(self):
        print('DVD Title:', self.__title)

    def checkTitle(self, title):
        return (self.__title==title)

    def upDateStock(self, num):
        self.__noofDVDs = self.__noofDVDs + num
