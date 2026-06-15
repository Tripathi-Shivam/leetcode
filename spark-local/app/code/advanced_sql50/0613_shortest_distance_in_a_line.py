from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

point_schema = StructType([
    StructField("x", IntegerType(), False)
])

point_data = [
    (-1,),
    (0,),
    (2,)
]

point_df = spark.createDataFrame(
    point_data,
    point_schema
)

point_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, lead, min, abs
from pyspark.sql.window import Window

window_spec = Window.orderBy(col("x"))

result_df = (
    point_df
        .withColumn("next_x", lead(col("x"), 1).over(window_spec))
        .agg(min(abs(col("next_x") - col("x"))).alias("shortest"))
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion