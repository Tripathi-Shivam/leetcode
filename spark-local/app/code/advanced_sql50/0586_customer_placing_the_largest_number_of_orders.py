from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("order_number", IntegerType(), False),
    StructField("customer_number", IntegerType(), False)
])

data = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 3)
]

orders_df = spark.createDataFrame(data, schema)
orders_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, count

result_df = (
    orders_df
        .groupBy("customer_number")
        .agg(count(col("order_number")).alias("orders_cnt"))
        .orderBy(col("orders_cnt").desc())
        .limit(1)
        .select("customer_number")
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1


# endregion