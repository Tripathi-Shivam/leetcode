from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, TimestampType
from datetime import datetime

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

loginfo_schema = StructType([
    StructField("account_id", IntegerType(), False),
    StructField("ip_address", IntegerType(), False),
    StructField("login", TimestampType(), False),
    StructField("logout", TimestampType(), False),
])

from datetime import datetime

loginfo_data = [
    (
        1,
        1,
        datetime(2021, 2, 1, 9, 0, 0),
        datetime(2021, 2, 1, 9, 30, 0)
    ),
    (
        1,
        2,
        datetime(2021, 2, 1, 8, 0, 0),
        datetime(2021, 2, 1, 11, 30, 0)
    ),
    (
        2,
        6,
        datetime(2021, 2, 1, 20, 30, 0),
        datetime(2021, 2, 1, 22, 0, 0)
    ),
    (
        2,
        7,
        datetime(2021, 2, 2, 20, 30, 0),
        datetime(2021, 2, 2, 22, 0, 0)
    ),
    (
        3,
        9,
        datetime(2021, 2, 1, 16, 0, 0),
        datetime(2021, 2, 1, 16, 59, 59)
    ),
    (
        3,
        13,
        datetime(2021, 2, 1, 17, 0, 0),
        datetime(2021, 2, 1, 17, 59, 59)
    ),
    (
        4,
        10,
        datetime(2021, 2, 1, 16, 0, 0),
        datetime(2021, 2, 1, 17, 0, 0)
    ),
    (
        4,
        11,
        datetime(2021, 2, 1, 17, 0, 0),
        datetime(2021, 2, 1, 17, 59, 59)
    )
]

loginfo_df = spark.createDataFrame(loginfo_data, loginfo_schema)
loginfo_df.show(truncate=False)

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col

result_df = (
    loginfo_df.alias("l1")
        .join(
            loginfo_df.alias("l2"),
            on = 
                (col("l1.account_id") == col("l2.account_id"))
                & (col("l1.ip_address") != col("l2.ip_address"))
                & (col("l1.login") <= col("l2.logout"))
                & (col("l2.login") <= col("l1.logout")),
            how = "inner"
        )
        .select("l1.account_id")
        .distinct()
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion