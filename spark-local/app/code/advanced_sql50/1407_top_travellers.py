from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

users_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False)
])

rides_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("user_id", IntegerType(), False),
    StructField("distance", IntegerType(), False)
])

users_data = [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Alex"),
    (4, "Donald"),
    (7, "Lee"),
    (13, "Jonathan"),
    (19, "Elvis")
]

rides_data = [
    (1, 1, 120),
    (2, 2, 317),
    (3, 3, 222),
    (4, 7, 100),
    (5, 13, 312),
    (6, 19, 50),
    (7, 7, 120),
    (8, 19, 400),
    (9, 7, 230)
]

users_df = spark.createDataFrame(users_data, users_schema)
rides_df = spark.createDataFrame(rides_data, rides_schema)

users_df.show()
rides_df.show()

print("--- Solution #1 ---")
# region: solution
from pyspark.sql.functions import col, sum, coalesce, lit

result_df = (
    users_df.alias("u")
        .join(
            rides_df.alias("r"),
            on = col("u.id") == col("r.user_id"),
            how = "left"
        )
        .groupBy(col("u.id"), col("u.name"))
        .agg(coalesce(sum(col("r.distance")), lit(0)).alias("travelled_distance"))
        .select(col("u.name"), col("travelled_distance"))
        .orderBy(col("travelled_distance").desc(), col("u.name").asc())
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice

# endregion