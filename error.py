print("FIRST  NORMAL EXAMPLE")
def cal(a):
    if(a>4):
        b=a/(a-5)

try:
    cal(5)

except ZeroDivisionError:
    print("RESOLVED")

print("SECOND EXAMPLE USING ELSE")

def main(a,b):
    try:
        c=a/b
    except ZeroDivisionError:
        print("RESOLVED")
    else:
        print(c)
    finally:
        print("CALCULATION IS DONE")

main(2,0)
main(4,2)

# use class , class variable , static methods , decorators in your example.

class sush:
    name="SUSHMITA"
    @classmethod
    def info(cls):
        print(cls.name)
    @staticmethod
    def lastname(a):
        print(a)
def mobile(func1):
    func1()
    print(" information is correct")

@mobile
def num():
    print("1234567891")




sush.info()
a=sush.lastname("SRIVASTAVA")


'''for i in range(int(input())):
    try:
        a,b = list(map(int, input().split()))
        print(a//b)
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as e:
        print('Error Code:',e)'''
a=(1,2,3,4)
b=map(lambda x:x+x,a)
print(list(b))
def num(x):
    return x*x
d=map(num,a)
print(list(d))
e=iter(a)
print(e)

print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e,'-1'))

