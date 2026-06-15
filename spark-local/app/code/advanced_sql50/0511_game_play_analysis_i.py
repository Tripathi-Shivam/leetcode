from datetime import date

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DateType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

activity_schema = StructType([
    StructField("player_id", IntegerType(), False),
    StructField("device_id", IntegerType(), False),
    StructField("event_date", DateType(), False),
    StructField("games_played", IntegerType(), False)
])

activity_data = [
    (1, 2, date(2016, 3, 1), 5),
    (1, 2, date(2016, 5, 2), 6),
    (2, 3, date(2017, 6, 25), 1),
    (3, 1, date(2016, 3, 2), 0),
    (3, 4, date(2018, 7, 3), 5)
]

activity_df = spark.createDataFrame(activity_data, activity_schema)
activity_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, min

result_df = (
    activity_df
        .groupBy("player_id")
        .agg(min(col("event_date")).alias("first_login"))
)
result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, first_value
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("player_id")).orderBy(col("event_date"))

result_df = (
    activity_df
        .withColumn("first_login", first_value(col("event_date")).over(window_spec))
        .select("player_id", "first_login")
        .distinct()
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice

# endregion