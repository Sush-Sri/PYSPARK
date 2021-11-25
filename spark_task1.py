#DATAFRAME AND CONNECTING USING SPARK
import os
import sys

from pyspark import SparkContext, SparkConf
'''from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('First_task').getOrCreate()
conn_url="jdbc:oracle:thin:@10.188.193.183:1521/INFADB"
df=spark.read.format('jdbc').option('url',conn_url).option('driver','oracle.jdbc.driver.OracleDriver').option('dbtable','TEST_EMP1').option('user','dw_user').option('password','Welcome1!').load()
print(df.printSchema())'''



#USING RDD

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
os.environ['PYSPARK_PYTHON']=sys.executable
os.environ['PYSPARK_DRIVER_PYTHON']=sys.executable


conf = SparkConf().setAppName("task")
sc = SparkContext(conf=conf)
spark=SparkSession.builder.getOrCreate()
config={}

config["user"] = "dw_user"
config["password"] = "Welcome1!"
config["driver"] = "oracle.jdbc.OracleDriver"
config["url"] = "jdbc:oracle:thin:@10.188.193.183:1521:INFADB"
#prop=list(config.items())

query='(SELECT EMPID,PRENAME,FNAME,MIDINITIAL,LNAME,GENDER,EMAIL FROM TEST_EMP1 FETCH FIRST 10 ROWS ONLY)TEST_EMP1'

res=spark.sparkContext.parallelize(spark.read.jdbc("jdbc:oracle:thin:@10.188.193.183:1521:INFADB",query,properties=config).collect())
#print(res)


##using toDf for converting into df
df2=res.toDF()
#print(df2.show())


#Second table tables
query2='(SELECT EMPID_BKP,PRENAME_BKP,FNAME_BKP,LNAME_BKP,GENDER_BKP,EMAIL_BKP FROM TEST_EMP1_BKP FETCH FIRST 10 ROWS ONLY)TEST_EMP1_BKP'

res1=spark.sparkContext.parallelize(spark.read.jdbc("jdbc:oracle:thin:@10.188.193.183:1521:INFADB",query2,properties=config).collect())
df3=res1.toDF()
#print(df3.show())

#COMPARING TWO RDD

df4=df2.join(df3,[df2.PRENAME ==df3.PRENAME_BKP], how='outer')
print(df4.show())






