from datetime import date

from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    DateType
)

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
    (1, 3, date(2017, 6, 25), 1),
    (3, 1, date(2016, 3, 2), 0),
    (3, 4, date(2018, 7, 3), 5)
]

activity_df = spark.createDataFrame(
    activity_data,
    activity_schema
)

activity_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, sum as spark_sum
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("player_id")).orderBy(col("event_date"))

result_df = (
    activity_df
        .withColumn("games_played_so_far", spark_sum(col("games_played")).over(window_spec))
        .select("player_id", "event_date", "games_played_so_far")
)

result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, sum as spark_sum

result_df = (
    activity_df.alias("a1")
        .join(
            activity_df.alias("a2"),
            on = (col("a1.player_id") == col("a2.player_id")) & (col("a1.event_date") <= col("a2.event_date")),
            how = "inner"
        )
        .groupBy(col("a2.player_id"), col("a2.event_date"))
        .agg(
            spark_sum(col("a1.games_played")).alias("games_played_so_far")
        )
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion