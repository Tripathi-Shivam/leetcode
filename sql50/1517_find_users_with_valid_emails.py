from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("user_id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("mail", StringType(), False)
])

data = [
    (1, "Winston", "winston@leetcode.com"),
    (2, "Jonathan", "jonathanisgreat"),
    (3, "Annabelle", "bella-@leetcode.com"),
    (4, "Sally", "sally.come@leetcode.com"),
    (5, "Marwan", "quarz2020@leetcode.COM"),
]

users_df = spark.createDataFrame(data, schema)
users_df.show(truncate=False)

# solution
from pyspark.sql.functions import col

result_df = (
    users_df
        .filter(col("mail").rlike(r"(^[a-zA-Z])([a-zA-Z0-9_.-]*)(\@leetcode\.com$)"))
)
result_df.show(truncate=False)