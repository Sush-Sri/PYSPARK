
import pandas as pd

'''import cx_Oracle
connection=cx_Oracle.connect('dw_user/Welcome1!@//10.188.193.183/INFADB')
print(connection.version)

cursor=connection.cursor()'''
table_data=pd.read_csv("abc.csv",delimiter=' ',skipinitialspace=True)


#df = pd.DataFrame(data, columns= [ 'STDNAME' ,'STDDEG','STDGRP' , 'Address', 'Year_of_Passed_Out','PinCode','PHNO','GENDER'])
#https://www.codegrepper.com/code-examples/python/python+script+to+read+csv+file+and+insert+into+database+using+pandas