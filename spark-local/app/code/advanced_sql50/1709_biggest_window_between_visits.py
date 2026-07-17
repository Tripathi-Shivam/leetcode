from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DateType

from datetime import date

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

user_visits_schema = StructType([
    StructField("user_id", IntegerType(), False),
    StructField("visit_date", DateType(), False)
])

user_visits_data = [
    (1, date(2020, 11, 28)),
    (1, date(2020, 10, 20)),
    (1, date(2020, 12, 3)),
    (2, date(2020, 10, 5)),
    (2, date(2020, 12, 9)),
    (3, date(2020, 11, 11))
]

user_visits_df = spark.createDataFrame(user_visits_data, user_visits_schema)
user_visits_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, lead, max as spark_max, datediff
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("user_id")).orderBy(col("visit_date"))

result_df = (
    user_visits_df
        .withColumn("next_visit_date", lead(col("visit_date"), 1, date(2021, 1, 1)).over(window_spec))
        .groupBy("user_id")
        .agg(spark_max(datediff(col("next_visit_date"), col("visit_date"))).alias("biggest_window"))
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion