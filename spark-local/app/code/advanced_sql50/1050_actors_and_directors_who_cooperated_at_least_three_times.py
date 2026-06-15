from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("actor_id", IntegerType(), False),
    StructField("director_id", IntegerType(), False),
    StructField("timestamp", IntegerType(), False),
])

data = [
    (1, 1, 0),
    (1, 1, 1),
    (1, 1, 2),
    (1, 2, 3),
    (1, 2, 4),
    (2, 1, 5),
    (2, 1, 6)
]

actor_director_df = spark.createDataFrame(data, schema)
actor_director_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, count

result_df = (
    actor_director_df
        .groupBy("actor_id", "director_id")
        .agg(count(col("timestamp")).alias("cnt"))
        .filter(col("cnt") >= 3)
        .drop("cnt")
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion