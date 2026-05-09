from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("salary", IntegerType(), False)
])

data = [
    (1, 100),
    (2, 200),
    (3, 300)
]

employee_df = spark.createDataFrame(data, schema)
employee_df.show()

# solution
from pyspark.sql.functions import col, dense_rank
from pyspark.sql.window import Window

window_spec = Window.orderBy(col("salary").desc())

result_df = (
    employee_df
        .withColumn("rnk", dense_rank().over(window_spec))
        .filter(col("rnk") == 2)
        .distinct()
        .select(col("salary").alias("SecondHighestSalary"))
)

if result_df.count() == 0:
    schema = StructType([StructField("SecondHighestSalary", IntegerType(), True)])
    result_df = spark.createDataFrame([(None,)], schema)

result_df.show()