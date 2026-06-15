from datetime import date

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DateType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

employees_schema = StructType([
    StructField("emp_id", IntegerType(), False),
    StructField("event_day", DateType(), False),
    StructField("in_time", IntegerType(), False),
    StructField("out_time", IntegerType(), False)
])

employees_data = [
    (1, date(2020, 11, 28), 4, 32),
    (1, date(2020, 11, 28), 55, 200),
    (1, date(2020, 12, 3), 1, 42),
    (2, date(2020, 11, 28), 3, 33),
    (2, date(2020, 12, 9), 47, 74)
]

employees_df = spark.createDataFrame(employees_data, employees_schema)
employees_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, sum

result_df = (
    employees_df
        .groupBy(col("event_day").alias("day"), col("emp_id"))
        .agg(sum(col("out_time") - col("in_time")).alias("total_time"))
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion