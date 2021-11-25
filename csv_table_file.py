'''import pandas as pd
import csv

import cx_Oracle
connection=cx_Oracle.connect('dw_user/Welcome1!@//10.188.193.183/INFADB')
print(connection.version)

c=connection.cursor()
data=pd.read_csv("abc.csv",delim_whitespace=True,skipinitialspace=True)
print(data)

#for printing the data from table
def read_query(connection,query):

    result=None

    try:
        c.execute(query)
        result=c.fetchall()
        print(result)
        #c.commit()
    except TypeError:
        print("Typeeeror")


q1="""SELECT * FROM APS
"""



#slicing of data starts here
total=data.shape[0]
pdet=[]
det=[]
for a in range(0,total):
        for b in data:

            if (b == "DegGrpAdd"):

                det.append((data[b][a][0:5]))

                det.append((data[b][a][5:8]))

                det.append((data[b][a][8:]))

            elif (b == "pinphnogen"):

                det.append((data[b][a][0:6]))

                det.append((data[b][a][6:16]))

                det.append((data[b][a][16:]))

            else:

                det.append(data[b][a])


        pdet.append(det)
        det = []
print(pdet)
for x in pdet:
        q2 = c.execute("INSERT INTO APS VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(*x)

#result = read_query(connection, q1)
#connection.commit()




#insertion of data in the table


print("Number of times you want to run query")
n=int(input())
#The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
for x in range(n):
    for x in pdet:
        q2 = c.execute("INSERT INTO APS VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(*x))

    result = read_query(connection, q1'''



















