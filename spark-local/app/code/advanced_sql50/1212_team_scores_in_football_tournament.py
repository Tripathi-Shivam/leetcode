from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

teams_schema = StructType([
    StructField("team_id", IntegerType(), False),
    StructField("team_name", StringType(), False)
])

matches_schema = StructType([
    StructField("match_id", IntegerType(), False),
    StructField("host_team", IntegerType(), False),
    StructField("guest_team", IntegerType(), False),
    StructField("host_goals", IntegerType(), False),
    StructField("guest_goals", IntegerType(), False)
])

teams_data = [
    (10, "Leetcode FC"),
    (20, "NewYork FC"),
    (30, "Atlanta FC"),
    (40, "Chicago FC"),
    (50, "Toronto FC")
]

matches_data = [
    (1, 10, 20, 3, 0),
    (2, 30, 10, 2, 2),
    (3, 10, 50, 5, 1),
    (4, 20, 30, 1, 0),
    (5, 50, 30, 1, 0)
]

teams_df = spark.createDataFrame(teams_data, teams_schema)
matches_df = spark.createDataFrame(matches_data, matches_schema)

teams_df.show()
matches_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, sum, when, coalesce, lit

result_df = (
    teams_df.alias("t")
        .join(
            matches_df.alias("m"),
            on = 
                (col("t.team_id") == col("m.host_team"))
                | (col("t.team_id") == col("m.guest_team")),
            how = "left"
        )
        .groupBy(col("t.team_id"), col("t.team_name"))
        .agg(
            coalesce(
                sum(
                    when((col("t.team_id") == col("m.host_team")) & (col("m.host_goals") > col("m.guest_goals")), 3)
                    .when((col("t.team_id") == col("m.guest_team")) & (col("m.guest_goals") > col("m.host_goals")), 3)
                    .when((col("t.team_id") == col("m.host_team")) & (col("m.host_goals") == col("m.guest_goals")), 1)
                    .when((col("t.team_id") == col("m.guest_team")) & (col("m.host_goals") == col("m.guest_goals")), 1)
                    .otherwise(0)
                ),
            lit(0)).alias("num_points")
        )
        .orderBy(col("num_points").desc(), col("team_id"))
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice

# endregion