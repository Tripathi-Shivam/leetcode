from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("user_id", IntegerType(), False),
    StructField("follower_id", IntegerType(), False)
])

data = [
    (0, 1),
    (1, 0),
    (2, 0),
    (2, 1)
]

followers_df = spark.createDataFrame(data, schema)
followers_df.show()

# solution
from pyspark.sql.functions import col, count

result = (
    followers_df
        .groupBy(col("user_id"))
        .agg(count(col("follower_id")).alias("followers_count"))
        .orderBy(col("user_id").asc())
)

result.show()