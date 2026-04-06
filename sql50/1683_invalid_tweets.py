from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("tweet_id", IntegerType(), False),
    StructField("content", StringType(), False)
])

data = [
    (1, "Vote for Biden"),
    (2, "Let us Explore the world"),
]

df_tweets = spark.createDataFrame(data, schema)
df_tweets.show()

# solution
from pyspark.sql.functions import col, length

result = (
    df_tweets
        .filter(
            (length(col("content")) > 15)
        )
        .select("tweet_id")
)
result.show()