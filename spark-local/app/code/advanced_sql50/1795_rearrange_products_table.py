from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

products_schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("store1", IntegerType(), True),
    StructField("store2", IntegerType(), True),
    StructField("store3", IntegerType(), True)
])

products_data = [
    (0, 95, 100, 105),
    (1, 70, None, 80)
]

products_df = spark.createDataFrame(
    products_data,
    products_schema
)

products_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, lit

result_df = (
    products_df
        .filter(col("store1").isNotNull())
        .select(
            col("product_id"), 
            lit("store1").alias("store"),
            col("store1").alias("price")
        )
        .unionAll(
            products_df
                .filter(col("store2").isNotNull())
                .select(
                    col("product_id"), 
                    lit("store2").alias("store"),
                    col("store2").alias("price")
                )
        )
        .unionAll(
            products_df
                .filter(col("store3").isNotNull())
                .select(
                    col("product_id"), 
                    lit("store3").alias("store"),
                    col("store3").alias("price")
                )
        )
)

result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col

result_df = (
    products_df
        .selectExpr(
            "product_id",
            """
            stack(
                3,
                'store1', store1,
                'store2', store2,
                'store3', store3
            ) as (store, price)
            """ 
        )
        .filter(col("price").isNotNull())
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion