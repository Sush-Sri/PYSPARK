def fetchdetails(func):
    def inner():
        print("DETAILS OF EMPLOYEE:")
        func()
    return inner


@fetchdetails
def info():
    print("NAME:SUSHMITA SRIVASTAVA")
    print("PLACE:FATEHPUR")

info()
class Dob:
     def __init__(self,date):
         self.date=date

     def getdate(self):
         return self.date
     @staticmethod
     def datechange(date):
        return date.replace("/","-")

date=Dob("07-10-2000")
datefromdb="07/10/2000"
datewithdash=Dob.datechange(datefromdb)

if(date.getdate() == datewithdash):
    print("Equal")
else:
    print("Unequal")
class Person:
    age = 21
    @classmethod

    def printAge(cls):
        print('The age is:', cls.age)


#Person.printAge = classmethod(Person.printAge)


Person.printAge()


class Lemon:
    def __init__(self):
        print("I LIKE LEMON")
    def __call__(self, a, b):
        print("LEMON IS",a,b)
e=Lemon()
e("YELLOW IN COLOR","AND SOUR TOO")


def comp(func1):
    def inner():
        print("COMPANY IS CLOSED FOR TODAY")
        func1()
        print("EMPLOYEES WILL GET THEIR PAY FOR TODAY")
    return inner
@comp
def holiday():
    print("TH ABOVE INFORMATON IS ALREADY MENTIONED IN CALENDER")
holiday()

class Birthday:
    def __init__(self,age):
        self.age=age
    @staticmethod
    def isage(age):
        return age>18
res=Birthday.isage(22)
print(res)
res=Birthday.isage(12)
print(res)


class Month:
    mon="october"


    @classmethod
    def pt(cls):
        print("MONTH IS ",cls.mon)
Month.pt()
