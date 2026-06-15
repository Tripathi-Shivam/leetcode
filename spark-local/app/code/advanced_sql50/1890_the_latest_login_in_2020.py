from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, TimestampType
from datetime import datetime

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("user_id", IntegerType(), False),
    StructField("time_stamp", TimestampType(), False)
])

data = [
    (6, datetime(2020, 6, 30, 15, 6, 7)),
    (6, datetime(2021, 4, 21, 14, 6, 6)),
    (6, datetime(2019, 3, 7, 0, 18, 15)),
    (8, datetime(2020, 2, 1, 5, 10, 53)),
    (8, datetime(2020, 12, 30, 0, 46, 50)),
    (2, datetime(2020, 1, 16, 2, 49, 50)),
    (2, datetime(2019, 8, 25, 7, 59, 8)),
    (14, datetime(2019, 7, 14, 9, 0, 0)),
    (14, datetime(2021, 1, 6, 11, 59, 59))
]

logins_df = spark.createDataFrame(data, schema)
logins_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, date_format, max, extract, lit

result_df = (
    logins_df
        # .filter(date_format(col("time_stamp"), "yyyy") == 2020)
        .filter(extract(lit('YEAR'), col("time_stamp")) == 2020)
        .groupBy("user_id")
        .agg(max(col("time_stamp")).alias("last_stamp"))
)
result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, year, first_value
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("user_id")).orderBy(col("time_stamp").desc())

result_df = (
    logins_df
        .filter(year(col("time_stamp")) == 2020)
        .withColumn("last_stamp", first_value(col("time_stamp")).over(window_spec))
        .drop("time_stamp")
        .distinct()
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice

# endregion