from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

players_schema = StructType([
    StructField("player_id", IntegerType(), False),
    StructField("player_name", StringType(), False)
])

championships_schema = StructType([
    StructField("year", IntegerType(), False),
    StructField("Wimbledon", IntegerType(), False),
    StructField("Fr_open", IntegerType(), False),
    StructField("US_open", IntegerType(), False),
    StructField("Au_open", IntegerType(), False)
])

players_data = [
    (1, "Nadal"),
    (2, "Federer"),
    (3, "Novak")
]

championships_data = [
    (2018, 1, 1, 1, 1),
    (2019, 1, 1, 2, 2),
    (2020, 2, 1, 2, 2)
]

players_df = spark.createDataFrame(players_data, players_schema)
championships_df = spark.createDataFrame(
    championships_data,
    championships_schema
)

players_df.show()
championships_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, lit, count

result_df = (
    championships_df
        .select(col("year"), lit("Wimbledon").alias("tournment"), col("Wimbledon").alias("player_id"))
        .unionAll(
            championships_df
                .select(col("year"), lit("Fr_open"), col("Fr_open"))
        )
        .unionAll(
            championships_df
                .select(col("year"), lit("US_open"), col("US_open"))
        )
        .unionAll(
            championships_df
                .select(col("year"), lit("Au_open"), col("Au_open"))
        )
        .alias("c")
        .join(players_df.alias("p"), on = "player_id", how = "inner")
        .groupBy("p.player_id", "p.player_name")
        .agg(count(col("c.player_id")).alias("grand_slams_count"))
)

result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, lit, sum as spark_sum, when

result_df = (
    championships_df.alias("c")
        .join(
            players_df.alias("p"), 
            on = 
                (col("p.player_id") == col("c.Wimbledon"))
                | (col("p.player_id") == col("c.Fr_open"))
                | (col("p.player_id") == col("c.Us_open"))
                | (col("p.player_id") == col("c.Au_open")), 
            how = "inner"
        )
        .groupBy("p.player_id", "p.player_name")
        .agg(
            (
                spark_sum(when(col("p.player_id") == col("c.Wimbledon"), lit(1)).otherwise(lit(0)))
                + spark_sum(when(col("p.player_id") == col("c.Fr_open"), lit(1)).otherwise(lit(0)))
                + spark_sum(when(col("p.player_id") == col("c.Us_open"), lit(1)).otherwise(lit(0)))
                + spark_sum(when(col("p.player_id") == col("c.Au_open"), lit(1)).otherwise(lit(0)))
            ).alias("grand_slams_count")
        )
)

result_df.show()
# endregion

print("--- Solution #3 ---")
# region: solution #3

result_df = (
    championships_df
        .selectExpr(
            "year",
            """
                stack(
                    4,
                    'Wimbledon', Wimbledon,
                    'Fr_open', Fr_open,
                    'Us_open', Us_open,
                    'Au_open', Au_open
                ) AS (tournament, player_id)
            """
        )
        .alias("c")
        .join(players_df.alias("p"), on = "player_id", how = "inner")
        .groupBy("p.player_id", "p.player_name")
        .agg(count(col("c.player_id")).alias("grand_slams_count"))
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion