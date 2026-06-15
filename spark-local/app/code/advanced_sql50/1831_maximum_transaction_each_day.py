from datetime import datetime

from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    DateType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

transactions_schema = StructType([
    StructField("transaction_id", IntegerType(), False),
    StructField("day", DateType(), False),
    StructField("amount", IntegerType(), False)
])

transactions_data = [
    (8, datetime(2021, 4, 3, 15, 57, 28), 57),
    (9, datetime(2021, 4, 28, 8, 47, 25), 21),
    (1, datetime(2021, 4, 29, 13, 28, 30), 58),
    (5, datetime(2021, 4, 28, 16, 39, 59), 40),
    (6, datetime(2021, 4, 29, 23, 39, 28), 58)
]

transactions_df = spark.createDataFrame(
    transactions_data,
    transactions_schema
)

transactions_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, rank, date_format
from pyspark.sql.window import Window

window_spec = Window.partitionBy(date_format(col("day"), 'yyyy-MM-dd')).orderBy(col("amount").desc())

result_df = (
    transactions_df
        .withColumn("rnk", rank().over(window_spec))
        .filter(col("rnk") == 1)
        .select("transaction_id")
        .orderBy("transaction_id")
)

result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, max as spark_max, date_format
from pyspark.sql.window import Window

window_spec = Window.partitionBy(date_format(col("day"), 'yyyy-MM-dd'))

result_df = (
    transactions_df
        .withColumn("max_amount", spark_max(col("amount")).over(window_spec))
        .filter(col("amount") == col("max_amount"))
        .select("transaction_id")
        .orderBy("transaction_id")
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion