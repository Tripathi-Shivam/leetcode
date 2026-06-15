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

orders_schema = StructType([
    StructField("order_id", IntegerType(), False),
    StructField("order_date", DateType(), False),
    StructField("customer_id", IntegerType(), False),
    StructField("product_id", IntegerType(), False)
])

products_schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("product_name", StringType(), False)
])

orders_data = [
    (1, date(2020, 7, 31), 1, 1),
    (2, date(2020, 7, 30), 2, 2),
    (3, date(2020, 8, 29), 3, 3),
    (4, date(2020, 7, 29), 4, 1),
    (5, date(2020, 6, 10), 1, 2),
    (6, date(2020, 8, 1), 2, 1),
    (7, date(2020, 8, 1), 3, 1),
    (8, date(2020, 8, 3), 1, 2),
    (9, date(2020, 8, 7), 2, 3),
    (10, date(2020, 7, 15), 1, 2)
]

products_data = [
    (1, "Keyboard"),
    (2, "Mouse"),
    (3, "Screen"),
    (4, "Hard Disk")
]

orders_df = spark.createDataFrame(
    orders_data,
    orders_schema
)

products_df = spark.createDataFrame(
    products_data,
    products_schema
)

orders_df.show()
products_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, max as spark_max

result_df = (
    orders_df.alias("o1")
        .join(
            orders_df.groupBy("product_id").agg(spark_max("order_date").alias("max_order_date")).alias("o2"),
            on = (col("o1.product_id") == col("o2.product_id")) & (col("o1.order_date") == col("o2.max_order_date")),
            how = "inner"
        )
        .join(products_df.alias("p"), on = col("o1.product_id") == col("p.product_id"), how = "inner")
        .select(col("p.product_name"), col("o1.product_id"), col("o1.order_id"), col("o2.max_order_date").alias("order_date"))
        .orderBy("product_name", "product_id", "order_id")
)

result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, max as spark_max
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("o.product_id"))

result_df = (
    orders_df.alias("o")
        .join(products_df.alias("p"), on = col("o.product_id") == col("p.product_id"), how = "inner")
        .withColumn("max_order_date", spark_max(col("o.order_date")).over(window_spec))
        .filter(col("o.order_date") == col("max_order_date"))
        .select(col("p.product_name"), col("o.product_id"), col("o.order_id"), col("max_order_date").alias("order_date"))
        .orderBy("product_name", "product_id", "order_id")
)

result_df.show()
# endregion

print("--- Solution #3 ---")
# region: solution #3
from pyspark.sql.functions import col, first_value
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("o.product_id")).orderBy(col("o.order_date").desc())

result_df = (
    orders_df.alias("o")
        .join(products_df.alias("p"), on = col("o.product_id") == col("p.product_id"), how = "inner")
        .withColumn("max_order_date", first_value(col("o.order_date")).over(window_spec))
        .filter(col("o.order_date") == col("max_order_date"))
        .select(col("p.product_name"), col("o.product_id"), col("o.order_id"), col("max_order_date").alias("order_date"))
        .orderBy("product_name", "product_id", "order_id")
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion