from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("num", IntegerType(), True)
])

# case #1
# data = [
#     (8),
#     (8),
#     (3),
#     (3),
#     (1),
#     (4),
#     (5),
#     (6)
# ]

# case #2 - no number appearing once
data = [
    (1),
    (1),
    (2),
    (2),
    (3),
    (3)
]

numbers_df = spark.createDataFrame(data, schema)
numbers_df.show()

# solution
from pyspark.sql.functions import col, count

result_df = (
    numbers_df
        .groupBy(col("num"))
        .agg(count(col("num")).alias("cnt"))
        .filter(col("cnt") == 1)
        .orderBy(col("num").desc())
        .limit(1)
        .select("num")
)

if result_df.count() == 0:
    schema = StructType([StructField("num", IntegerType(), True)])
    result_df = spark.createDataFrame([(None,)], schema)

result_df.show()