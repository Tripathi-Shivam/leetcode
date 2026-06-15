from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("player_id",   IntegerType(), False),
    StructField("device_id",   IntegerType(), False),
    StructField("event_date",  DateType(),    False),
    StructField("games_played",IntegerType(), False),
])

data = [
    (1, 2, date(2016, 3, 1),  5),
    (1, 2, date(2016, 3, 2),  6),
    (2, 3, date(2017, 6, 25), 1),
    (3, 1, date(2016, 3, 2),  0),
    (3, 4, date(2018, 7, 3),  5),
]

activity = spark.createDataFrame(data, schema)
activity.show()

# region: solution
print("--- Solution #1 ---")
from pyspark.sql.functions import col, lit, count, countDistinct, lead, row_number, datediff, round
from pyspark.sql.window import Window

# returns a DataFrame
# all_players = (
#     activity.agg(countDistinct(col("player_id")).alias("total_players"))
# )

# this will give a literal value instead of a dataframe
# avoids cross join
all_players = activity.select("player_id").distinct().count()

window_spec = Window.partitionBy(col("player_id")).orderBy(col("event_date").asc())

result = (
    activity
        .withColumn("next_login_date", lead(col("event_date"), 1).over(window_spec))
        .withColumn("next_login_row", row_number().over(window_spec))
        .filter(
            (col("next_login_row") == 1)
            & (datediff(col("next_login_date"), col("event_date")) == 1)
        )
        .agg(
            round(
                count(col("player_id")) / lit(all_players),
            2).alias("fraction")
        )
)
result.show()
# endregion

# region: optimized
print("--- Optimized ---")
from pyspark.sql.functions import col, lit, round, count, date_sub, min
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("player_id"))

total_players = activity.select("player_id").distinct().count()

result = (
    activity
        .withColumn("first_login", min(col("event_date")).over(window_spec))
        .filter(col("first_login") == date_sub(col("event_date"), 1))
        .select(
            round(count("player_id") / lit(total_players), 2).alias("fraction")
        )
)
result.show()
# endregion

# region: practice #1
print("--- Practice #1 ---")
from pyspark.sql.functions import col, min, lead, date_sub, round, count, lit
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("player_id")).orderBy(col("event_date").asc())

total_players = activity.select("player_id").distinct().count()

result_df = (
    activity
        .withColumn("first_login_date", min(col("event_date")).over(window_spec))
        .withColumn("next_login_date", lead(col("event_date"), 1).over(window_spec))
        .filter(
            (col("event_date") == col("first_login_date"))
            & (col("first_login_date") == date_sub(col("next_login_date"), 1))
        )
        .select(
            round(
                count(col("player_id")) / lit(total_players),
            2).alias("fraction")
        )
)
result_df.show()
# endregion

# region: practice #2
print("--- Practice #2 ---")

# endregion