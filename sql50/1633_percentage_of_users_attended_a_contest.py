from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

users_schema = StructType([
    StructField("user_id", IntegerType(), False),
    StructField("user_name", StringType(), False)
])

users_data = [
    (6,  "Alice"),
    (2,  "Bob"),
    (7,  "Alex")
]

users = spark.createDataFrame(users_data, users_schema)

register_schema = StructType([
    StructField("contest_id", IntegerType(), False),
    StructField("user_id", IntegerType(), False)
])

register_data = [
    (215, 6),
    (209, 2),
    (208, 2),
    (210, 6),
    (208, 6),
    (209, 7),
    (209, 6),
    (215, 7),
    (208, 7),
    (210, 2),
    (207, 2),
    (210, 7),
]

register = spark.createDataFrame(register_data, register_schema)

users.show()
register.show()

# solution
from pyspark.sql.functions import count, round, lit, col

total_users = users.count()

result = (
    register
        .groupBy("contest_id")
        .agg(
            round(
                (count("user_id") / lit(total_users))
                * 100,
            2).alias("percentage")
        )
        .orderBy(col("percentage").desc(), col("contest_id").asc())
)
result.show()