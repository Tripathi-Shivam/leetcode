from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, TimestampType
from datetime import datetime

spark = SparkSession.builder.getOrCreate()

signups_schema = StructType([
    StructField("user_id",    IntegerType(),   False),
    StructField("time_stamp", TimestampType(), False),
])

signups_data = [
    (3,  datetime(2020, 3,  21, 10, 16, 13)),
    (7,  datetime(2020, 1,  4,  13, 57, 59)),
    (2,  datetime(2020, 7,  29, 23, 9,  44)),
    (6,  datetime(2020, 12, 9,  10, 39, 37)),
]

signups = spark.createDataFrame(signups_data, signups_schema)

confirmations_schema = StructType([
    StructField("user_id",    IntegerType(),   False),
    StructField("time_stamp", TimestampType(), False),
    StructField("action",     StringType(),    False),  # 'confirmed' or 'timeout'
])

confirmations_data = [
    (3,  datetime(2021, 1,  6,  3,  16, 5),  "timeout"),
    (3,  datetime(2021, 7,  14, 14, 0,  52), "timeout"),
    (7,  datetime(2021, 6,  12, 11, 57, 29), "confirmed"),
    (7,  datetime(2021, 6,  13, 12, 58, 28), "confirmed"),
    (7,  datetime(2021, 6,  14, 13, 59, 27), "confirmed"),
    (2,  datetime(2021, 1,  22, 00, 0,  0),  "confirmed"),
    (2,  datetime(2021, 2,  28, 23, 59, 59), "timeout"),
]

confirmations = spark.createDataFrame(confirmations_data, confirmations_schema)

signups.show()
confirmations.show()

# solution
from pyspark.sql.functions import col, lit, avg, when, round

result = (
    signups.alias("sgnu")
        .join(confirmations.alias("cnfm"), on = col("sgnu.user_id") == col("cnfm.user_id"), how = "left")
        .groupBy(col("sgnu.user_id"))
        .agg(
            round(
                avg(when(col("cnfm.action") == "confirmed", lit(1)).otherwise(lit(0))),
                2
            ).alias("confirmation_rate")
        )
)
result.show()