#Work on field validation and row count
#Want a separate application ,
#Take the connection details from keyboard
#fetchall returns a list of tuples

import cx_Oracle
connection=cx_Oracle.connect('dw_user/Welcome1!@//10.188.193.183/INFADB')
print(connection.version)

c=connection.cursor()

#ROW VALIDATION
c.execute("SELECT COUNT(*) FROM PRODUCT_OLD ")
row1=c.fetchall()
print(list(row1))

c.execute("SELECT COUNT(*) FROM PRODUCT_OLD_TEST")
row2=c.fetchall()
print(list(row2))

if(row1==row2):
    print("ROW COUNT IS SAME")
else:
    print("ROW COUNT IS SAME")


#Datatype Validation

c.execute("Select DATA_TYPE from user_tab_columns where table_name='PRODUCT_OLD' ")
row3 = c.fetchall()
print(row3)

c.execute("Select DATA_TYPE from user_tab_columns where table_name='PRODUCT_OLD_TEST' ")
row4 = c.fetchall()
print(list(row4))

if row3 == row4:
    print("Same")
else:
    print("not Same")
# column count


c.execute("Select count(*) from user_tab_columns where table_name='PRODUCT_OLD' ")
row5 = c.fetchall()
print(list(row5))

c.execute("Select count(*) from user_tab_columns where table_name='PRODUCT_OLD_TEST' ")
row6 = c.fetchall()
print(list(row6))

if row5[0] == row6[0]:
    print("COLUMN COUNT SAME")
else:
    print("COLUMN COUNT NOT SAME")

c.execute("SELECT PRODUCT_OLD_BKP.PRODUCT_ID PRODUCT_OLD_TEST.PRODUCT_NAME FROM PRODUCT_OLD_BKP INNER JOIN PRODUCT_OLD_TEST ON PRODUCT_OLD_BKP.ID=PRODUCT_OLD_TEST.ID ")
row7 = c.fetchall()
print(row7)




