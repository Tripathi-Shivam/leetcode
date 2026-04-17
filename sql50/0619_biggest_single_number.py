from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("num", IntegerType(), True)
])

data = [
    (8),
    (8),
    (3),
    (3),
    (1),
    (4),
    (5),
    (6)
]

numbers_df = spark.createDataFrame(data, schema)
numbers_df.show()

# solution
from pyspark.sql.functions import col, count, max

result = (
    numbers_df
        .groupBy(col("num"))
        .agg(count(col("num")).alias("num_count"))
        .filter(col("num_count") == 1)
        .select(max("num").alias("num"))
)
result.show()