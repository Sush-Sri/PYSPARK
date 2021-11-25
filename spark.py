from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('First_task').getOrCreate()
conn_url="jdbc:oracle:thin:@10.188.193.183:1521/INFADB"
df=spark.read.format('jdbc').option('url',conn_url).option('driver','oracle.jdbc.driver.OracleDriver').option('dbtable','TEST_EMP1').option('user','dw_user').option('password','Welcome1!').load()
print(df.printSchema())