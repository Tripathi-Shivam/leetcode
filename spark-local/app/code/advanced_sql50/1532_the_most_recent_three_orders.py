from datetime import date

from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DateType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

customers_schema = StructType([
    StructField("customer_id", IntegerType(), False),
    StructField("name", StringType(), False)
])

orders_schema = StructType([
    StructField("order_id", IntegerType(), False),
    StructField("order_date", DateType(), False),
    StructField("customer_id", IntegerType(), False),
    StructField("cost", IntegerType(), False)
])

customers_data = [
    (1, "Winston"),
    (2, "Jonathan"),
    (3, "Annabelle"),
    (4, "Marwan"),
    (5, "Khaled")
]

orders_data = [
    (1, date(2020, 7, 31), 1, 30),
    (2, date(2020, 7, 30), 2, 40),
    (3, date(2020, 7, 31), 3, 70),
    (4, date(2020, 7, 29), 4, 100),
    (5, date(2020, 6, 10), 1, 1010),
    (6, date(2020, 8, 1), 2, 102),
    (7, date(2020, 8, 1), 3, 111),
    (8, date(2020, 8, 3), 1, 99),
    (9, date(2020, 8, 7), 2, 32),
    (10, date(2020, 7, 15), 1, 2)
]

customers_df = spark.createDataFrame(customers_data, customers_schema)
orders_df = spark.createDataFrame(orders_data, orders_schema)

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("customer_id")).orderBy(col("order_date").desc())

result_df = (
    orders_df
        .withColumn("rnk", row_number().over(window_spec))
        .alias("o")
        .join(customers_df.alias("c"), on = "customer_id", how = "inner")
        .filter(col("o.rnk") <= 3)
        .select(col("c.name").alias("customer_name"), col("c.customer_id"), col("o.order_id"), col("o.order_date"))
        .orderBy("customer_name", "customer_id", col("order_date").desc())
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion