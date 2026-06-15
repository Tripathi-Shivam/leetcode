from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

logs_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("num", IntegerType(), False)
])

logs_data = [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 1),
    (6, 2),
    (7, 2)
]

logs_df = spark.createDataFrame(logs_data, logs_schema)
logs_df.show()

print("--- Solution #1 ---")
# region: solution
from pyspark.sql.functions import col, lag, lead
from pyspark.sql.window import Window

window_spec = Window.orderBy(col("id").asc())

result = (
    logs_df
        .withColumn("prev_row", lag(col("num"), 1).over(window_spec))
        .withColumn("next_row", lead(col("num"), 1).over(window_spec))
        .filter(
            (col("num") == col("prev_row"))
            & (col("num") == col("next_row"))
        )
        .select(col("num").alias("ConsecutiveNums"))
        .distinct()
)
result.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion