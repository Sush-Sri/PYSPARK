import pandas as pd
from sqlalchemy import create_engine
import numpy as np

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

engine = create_engine(
    oracle_connection_string.format(
        username='dw_user',
        password='Welcome1!',
        hostname='10.188.193.183',
        port='1521',
        database='INFADB',
    )
)
df=pd.read_sql("select PRODUCT_ID,PRODUCT_PRICE from PRODUCT_OLD WHERE ROWNUM<=10",engine)
#print(df)

df1=pd.read_sql("select PRODUCT_ID,PRODUCT_PRICE from PRODUCT_OLD_TEST WHERE ROWNUM<=10",engine)
#print(df1)
tot_null=df.isnull().sum()
print("Total null in PRODUCT_OLD",tot_null)
tot_null_TEST=df.isnull().sum()
print("Total null in PRODUCT_OLD_TEST",tot_null_TEST)

cmp=df.compare(df1,align_axis=0)
print(cmp)

cmp2=df.compare(df1,keep_equal=True)    # keep_equal is true, the result also keeps values that are equal. Otherwise, equal values are shown as NaNs. By default it is set to False.
print(cmp2)
print("f true, all rows and columns are kept. Otherwise, only the ones with different values are kept.")
print(df.compare(df1,keep_shape=True))
print("diference between two df:")

print(df.eq(df1).all(axis=1)) # .all returns True for a row if all values are True
print(".any returns true for row if any of the row's values are True")

print(df[df.ne(df1).any(axis=1)])


