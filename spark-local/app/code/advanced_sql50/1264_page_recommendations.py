from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

friendship_schema = StructType([
    StructField("user1_id", IntegerType(), False),
    StructField("user2_id", IntegerType(), False)
])

likes_schema = StructType([
    StructField("user_id", IntegerType(), False),
    StructField("page_id", IntegerType(), False)
])

friendship_data = [
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 3),
    (2, 4),
    (2, 5),
    (6, 1)
]

likes_data = [
    (1, 88),
    (2, 23),
    (3, 24),
    (4, 56),
    (5, 11),
    (6, 33),
    (2, 77),
    (3, 77),
    (6, 88)
]

friendship_df = spark.createDataFrame(
    friendship_data,
    friendship_schema
)

likes_df = spark.createDataFrame(
    likes_data,
    likes_schema
)

friendship_df.show()
likes_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, when

user_1_friends = (
    friendship_df
        .filter((col("user1_id") == 1) | (col("user2_id") == 1))
        .select(when(col("user1_id") == 1, col("user2_id")).otherwise(col("user1_id")).alias("user_id"))
)

result_df = (
    likes_df.alias("l1")
        .join(
            user_1_friends.alias("u1"),
            on = "user_id",
            how = "left_semi"
        )
        .join(
            likes_df.alias("l2").filter(col("user_id") == 1),
            on = "page_id",
            how = "left_anti"
        )
        .select(col("l1.page_id").alias("recommended_page"))
        .distinct()
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion