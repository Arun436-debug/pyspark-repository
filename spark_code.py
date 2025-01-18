from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('ArunApp').getOrCreate()

output = spark.read.format('csv').option('header','true')\
    .option('path',"C:/Users/Administrator/Desktop/mycsv/employee_data_with_col_names.csv")\
    .load()

spark.sql('select * from output').show()