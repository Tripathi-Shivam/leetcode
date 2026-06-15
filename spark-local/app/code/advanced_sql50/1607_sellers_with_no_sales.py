from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

customer_schema = StructType([
    StructField("customer_id", IntegerType(), False),
    StructField("customer_name", StringType(), False)
])

orders_schema = StructType([
    StructField("order_id", IntegerType(), False),
    StructField("sale_date", DateType(), False),
    StructField("order_cost", IntegerType(), False),
    StructField("customer_id", IntegerType(), False),
    StructField("seller_id", IntegerType(), False)
])

seller_schema = StructType([
    StructField("seller_id", IntegerType(), False),
    StructField("seller_name", StringType(), False)
])

customer_data = [
    (101, "Alice"),
    (102, "Bob"),
    (103, "Charlie")
]

orders_data = [
    (1, date(2020, 3, 1), 1500, 101, 1),
    (2, date(2020, 5, 25), 2400, 102, 2),
    (3, date(2019, 5, 25), 800, 101, 3),
    (4, date(2020, 9, 13), 1000, 103, 2),
    (5, date(2019, 2, 11), 700, 101, 2)
]

seller_data = [
    (1, "Daniel"),
    (2, "Elizabeth"),
    (3, "Frank")
]

customer_df = spark.createDataFrame(customer_data, customer_schema)
orders_df = spark.createDataFrame(orders_data, orders_schema)
seller_df = spark.createDataFrame(seller_data, seller_schema)

customer_df.show()
orders_df.show()
seller_df.show()

print("--- Solution #1 ---")
# region: solution
from pyspark.sql.functions import col, lit, date_format

result_df = (
    seller_df.alias("s")
        .join(
            orders_df.alias("o").filter(date_format(col("o.sale_date"), 'yyyy') == lit(2020)),
            on = "seller_id",
            how = "left_anti"
        )
        .select("s.seller_name")
        .orderBy("s.seller_name")
)
result_df.show()

# endregion

print("--- Practice #1 ---")
# region: practice

# endregion