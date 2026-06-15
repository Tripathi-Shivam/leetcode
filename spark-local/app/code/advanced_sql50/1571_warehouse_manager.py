from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

warehouse_schema = StructType([
    StructField("name", StringType(), False),
    StructField("product_id", IntegerType(), False),
    StructField("units", IntegerType(), False)
])

products_schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("product_name", StringType(), False),
    StructField("width", IntegerType(), False),
    StructField("length", IntegerType(), False),
    StructField("Height", IntegerType(), False)
])

warehouse_data = [
    ("LCHouse1", 1, 1),
    ("LCHouse1", 2, 10),
    ("LCHouse1", 3, 5),
    ("LCHouse2", 1, 2),
    ("LCHouse2", 2, 2),
    ("LCHouse3", 4, 1)
]

products_data = [
    (1, "LC-TV", 5, 50, 40),
    (2, "LC-KeyChain", 5, 5, 5),
    (3, "LC-Phone", 2, 10, 10),
    (4, "LC-T-Shirt", 4, 10, 20)
]

warehouse_df = spark.createDataFrame(warehouse_data, warehouse_schema)
products_df = spark.createDataFrame(products_data, products_schema)

warehouse_df.show()
products_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, sum

result_df = (
    warehouse_df.alias("w")
        .join(
            products_df.alias("p"),
            on = "product_id",
            how = "left"
        )
        .groupBy(col("w.name").alias("warehouse_name"))
        .agg(
            sum(
                col("p.length") * col("p.width") * col("p.height") * col("w.units")
            ).alias("volume")
        )
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice

# endregion