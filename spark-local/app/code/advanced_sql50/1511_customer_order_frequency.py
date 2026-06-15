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
    StructField("name", StringType(), False),
    StructField("country", StringType(), False),
])

orders_schema = StructType([
    StructField("order_id", IntegerType(), False),
    StructField("customer_id", IntegerType(), False),
    StructField("product_id", IntegerType(), False),
    StructField("order_date", DateType(), False),
    StructField("quantity", IntegerType(), False)
])

product_schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("description", StringType(), False),
    StructField("price", IntegerType(), False)
])

customers_data = [
    (1, "Winston", "USA"),
    (2, "Jonathan", "Peru"),
    (3, "Moustafa", "Egypt")
]

orders_data = [
    (1, 1, 10, date(2020, 6, 10), 1),
    (2, 1, 20, date(2020, 7, 1), 1),
    (3, 1, 30, date(2020, 7, 8), 2),
    (4, 2, 10, date(2020, 6, 15), 2),
    (5, 2, 40, date(2020, 7, 1), 10),
    (6, 3, 20, date(2020, 6, 24), 2),
    (7, 3, 30, date(2020, 6, 25), 2),
    (9, 3, 30, date(2020, 5, 8), 3),
]

product_data = [
    (10, "LC Phone", 300),
    (20, "LC T-Shirt", 10),
    (30, "LC Book", 45),
    (40, "LC Keychain", 2)
]

customers_df = spark.createDataFrame(customers_data, customers_schema)
customers_df.show()

orders_df = spark.createDataFrame(orders_data, orders_schema)
orders_df.show()

product_df = spark.createDataFrame(product_data, product_schema)
product_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, sum, when, year, month, lit
result_df = (
    orders_df.alias("o")
        .join(
            customers_df.alias("c"),
            on = "customer_id",
            how = "inner"
        )
        .join(
            product_df.alias("p"),
            on = "product_id",
            how = "inner"
        )
        .filter(year(col("o.order_date")) == 2020)
        .groupBy(col("c.customer_id"), col("c.name"))
        .agg(
            sum(when(month("o.order_date") == 6, col("o.quantity")).otherwise(lit(0)) * col("p.price")).alias("june_amt"),
            sum(when(month("o.order_date") == 7, col("o.quantity")).otherwise(lit(0)) * col("p.price")).alias("july_amt")
        )
        .filter(
            (col("june_amt") >= 100)
            & (col("july_amt") >= 100)
        )
        .drop("june_amt", "july_amt")
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion