import cx_Oracle
import pandas as pd
connection=cx_Oracle.connect('dw_user/Welcome1!@//10.188.193.183/INFADB')


c = connection.cursor()

def read_query(connection,query):

    result=None

    try:
        c.execute(query)
        result=c.fetchall()
        print(result)
    except TypeError:
        print("Typeeeror")
    finally:
        print("Done")
#GET INFO ABOUT STUDENTS
print("GET INFO ABOUT STUDENTS")
q1="""SELECT * FROM STUDENTS
"""
results=read_query(connection,q1)



#UPDATE STUDENT NAME
print("UPDATE STUDENT NAME")
c.execute("UPDATE STUDENTS SET NAME='SUSHMITA' WHERE MARKS=20 ")
update_data=c.execute("SELECT * FROM STUDENTS")
row=c.fetchall()
print(row)




#ADD NEW DATA
print("ADD NEW DATA")
c.execute("INSERT INTO STUDENTS VALUES(5,'RAM','930 VIP COLONY     ', 100)")
c.execute("SELECT * FROM STUDENTS")
row2=c.fetchall()
print(row2)

c.close()