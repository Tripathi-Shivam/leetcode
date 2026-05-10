from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()

products_schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("product_name", StringType(), False)
])

orders_schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("order_date", DateType(), False),
    StructField("unit", IntegerType(), False)
])

products_data = [
    (1, "Leetcode Solutions"),
    (2, "Jewels of Stringology")
]

orders_data = [
    (1, date(2020, 2, 5), 60),
    (1, date(2020, 2, 10), 70),
    (2, date(2020, 2, 20), 30)
]

products_df = spark.createDataFrame(products_data, products_schema)
orders_df = spark.createDataFrame(orders_data, orders_schema)

# solution
from pyspark.sql.functions import col, date_format, sum

result_df = (
    products_df.alias("p")
        .join(
            orders_df.alias("o"),
            on = "product_id",
            how = "left"
        )
        .filter(date_format(col("o.order_date"), "yyyy-MM") == "2020-02")
        .groupBy(col("p.product_name"))
        .agg(sum(col("o.unit")).alias("unit"))
        .filter(col("unit") >= 100)
)
result_df.show()