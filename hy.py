'''class Parrot:
    species="bird"
    def __init__(self,name,age): this is a method assigned with self
        self.name=name
        self.age=age
    def sing(self,song):
        return "{} sings {}".format(blu.name,song)
    def dance(self):
        return "{} dances crazy".format(self.name)

blu=Parrot("blu", 2)
woo=Parrot("woo",3)
print(blu.sing('happy'))
print(woo.dance())

print("blu is a {}".format(blu.__class__.species))
print("woo is a  {}".format(woo.__class__.species))
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))'''

'''INHERITENCE'''

#parent class
'''class Bird:
    def __init__(self):
        print("bird")
    def parrot(self):
        print("selfbird")
    def whoisthis(self):
        print("crow")
class Hen(Bird):
    def __init__(self):
        super().__init__()
        print("dog")


    def whoisthis(self):
        print("hen")
obj=Hen()
obj.parrot()
obj.whoisthis()'''


'''  ABSTRACTION '''


'''class Price:
    def __init__(self):
        self.__maxprice=1000
    def sell(self):
        print(self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice= price
c=Price()
c.sell()
c.__maxprice=1050
c.sell()
c.setmaxprice(1100)
c.sell()'''



'''Polymorphism'''

class Parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("par cant swim")
class Penguine:
    def fly(self):
        print("pen no fly")
    def swim(self):
        print("penguine can swim")
def flying_test(Bird):
    Bird.fly()
blu=Parrot()
woo=Penguine()
flying_test(blu)
flying_test(woo)




