from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

employee_schema = StructType([
    StructField("employee_id", IntegerType(), False),
    StructField("team_id", IntegerType(), False)
])

employee_data = [
    (1, 8),
    (2, 8),
    (3, 8),
    (4, 7),
    (5, 9),
    (6, 9)
]

employee_df = spark.createDataFrame(employee_data, employee_schema)
employee_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, count
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("team_id"))

result_df = (
    employee_df
        .withColumn("team_size", count(col("employee_id")).over(window_spec))
        .select("employee_id", "team_size")
)

result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
result_df = (
    employee_df.alias("e")
        .join(
            employee_df.groupBy(col("team_id")).agg(count(col("employee_id")).alias("team_size")).alias("t"),
            on = "team_id",
            how = "inner"
        )
        .select(col("e.employee_id"), col("t.team_size"))
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion