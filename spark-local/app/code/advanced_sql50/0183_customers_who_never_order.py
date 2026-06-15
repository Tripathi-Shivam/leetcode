from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

customers_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False)
])

orders_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("customerId", IntegerType(), False)
])

customers_data = [
    (1, "Joe"),
    (2, "Henry"),
    (3, "Sam"),
    (4, "Max")
]

orders_data = [
    (1, 3),
    (2, 1)
]

customers_df = spark.createDataFrame(customers_data, customers_schema)
orders_df = spark.createDataFrame(orders_data, orders_schema)

customers_df.show()
orders_df.show()

# region: solution
from pyspark.sql.functions import col
result_df = (
    customers_df.alias("c")
        .join(
            orders_df.alias("o"),
            on = col("c.id") == col("o.customerId"),
            how = "left_anti"
        )
        .select(col("c.name").alias("customers"))
)
result_df.show()
# endregion

# region: practice

# endregion