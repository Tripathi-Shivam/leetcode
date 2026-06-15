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
    (2, 3, date(2017, 6, 25), 1),
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
from pyspark.sql.functions import col, min as spark_min

result_df = (
    activity_df.alias("a1")
        .join(
            activity_df.alias("a2").groupBy("player_id").agg(spark_min("event_date").alias("min_date")).alias("a2"),
            on = (col("a1.player_id") == col("a2.player_id")) & (col("a1.event_date") == col("a2.min_date")),
            how = "inner"
        )
        .select(col("a1.player_id"), col("a1.device_id"))
)

result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("player_id")).orderBy(col("event_date"))

result_df = (
    activity_df
        .withColumn("rnk", row_number().over(window_spec))
        .filter(col("rnk") == 1)
        .select("player_id", "device_id")
)

result_df.show()
# endregion

print("--- Solution #3 ---")
# region: solution #3
from pyspark.sql.functions import col, first_value
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("player_id")).orderBy(col("event_date"))

result_df = (
    activity_df
        .withColumn("device_id", first_value(col("device_id")).over(window_spec))
        .select("player_id", "device_id")
        .distinct()
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion