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
    StructField("product_id", IntegerType(), False)
])

products_schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("product_name", StringType(), False),
    StructField("price", IntegerType(), False)
])

customers_data = [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Tom"),
    (4, "Jerry"),
    (5, "John")
]

orders_data = [
    (1, date(2020, 7, 31), 1, 1),
    (2, date(2020, 7, 30), 2, 2),
    (3, date(2020, 8, 29), 3, 3),
    (4, date(2020, 7, 29), 4, 1),
    (5, date(2020, 6, 10), 1, 2),
    (6, date(2020, 8, 1), 2, 1),
    (7, date(2020, 8, 1), 3, 3),
    (8, date(2020, 8, 3), 1, 2),
    (9, date(2020, 8, 7), 2, 3),
    (10, date(2020, 7, 15), 1, 2)
]

products_data = [
    (1, "Keyboard", 120),
    (2, "Mouse", 80),
    (3, "Screen", 600),
    (4, "Hard Disk", 450)
]

customers_df = spark.createDataFrame(customers_data, customers_schema)
orders_df = spark.createDataFrame(orders_data, orders_schema)
products_df = spark.createDataFrame(products_data, products_schema)

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, count, rank
from pyspark.sql.window import Window

window_spec = Window.partitionBy("customer_id").orderBy(col("product_cnt").desc())

result_df = (
    orders_df
        .groupBy("customer_id", "product_id")
        .agg(count(col("product_id")).alias("product_cnt"))
        .withColumn("rnk", rank().over(window_spec))
        .filter(col("rnk") == 1)
        .alias("o")
        .join(products_df.alias("p"), on = "product_id", how = "inner")
        .select("o.customer_id", "p.product_id", "p.product_name")
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion