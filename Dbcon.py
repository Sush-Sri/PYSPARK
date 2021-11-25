import cx_Oracle


#connection= cx_Oracle.connect('system/sush123@//localhost:1521/xe')
                              #username/pass@/lh/sid no


connection=cx_Oracle.connect('dw_user/Welcome1!@//10.188.193.183/INFADB')
print(connection.version)

cursor=connection.cursor()

#execute query

'''query= """
CREATE TABLE empsss(NAME VARCHAR(50),CITY VARCHAR(50), AGE NUMBER)   

"""

cursor.execute(query)'''
fquery="""
select * from PRODUCT_OLD


"""
cursor.execute(fquery)
data=cursor.fetchall()
for i in enumerate(data):
    print(i)
print("next table output")

fqueryb="""
select * from  PRODUCT_OLD_TEST
"""
cursor.execute(fqueryb)
datab=cursor.fetchall()
for c in enumerate(datab):
    print(c)
print("ok done")













'''df['product_price_match']=np.where(df['PRODUCT_PRICE'] == df1['PRODUCT_PRICE'],'True','False')
print(df)'''
'''df['priceDiff?'] = np.where(df1['PRODUCT_PRICE'] == df1['PRODUCT_PRICE'], 0, df1['PRODUCT_PRICE'] - df1['PRODUCT_PRICE']) #create new column in df1 for price diff
print(df)'''







