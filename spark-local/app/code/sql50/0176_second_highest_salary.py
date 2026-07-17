from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

from pyspark.sql.functions import col, dense_rank
from pyspark.sql.window import Window

spark = (
    SparkSession.builder
        # .master("spark://spark-master:8080")
        .appName("Leetcode-SecondHighestSalary")
        .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("salary", IntegerType(), False)
])

data = [
    (1, 100),
    (2, 100),
    (3, 300)
]

employee_df = spark.createDataFrame(data, schema)
employee_df.show()

# region: solution #1
window_spec = Window.orderBy(col("salary").desc())

result_df = (
    employee_df
        .withColumn("rnk", dense_rank().over(window_spec))
        .filter(col("rnk") == 2)
        .select(col("salary").alias("SecondHighestSalary"))
        .distinct()
)

if result_df.count() == 0:
    schema = StructType([StructField("SecondHighestSalary", IntegerType(), True)])
    result_df = spark.createDataFrame([(None,)], schema)

result_df.show()
# endregion

# region: solution #2
from pyspark.sql.functions import col

result_df = (
    employee_df
        .select(col("salary").alias("SecondHighestSalary"))
        .distinct()
        .orderBy(col("salary").desc())
        .offset(1)
        .limit(1)
)

if result_df.count() == 0:
    schema = StructType([StructField("SecondHighestSalary", IntegerType(), True)])
    result_df = spark.createDataFrame([(None,)], schema)
result_df.show()
# endregion