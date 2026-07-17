from datetime import date

from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    DateType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

failed_schema = StructType([
    StructField("fail_date", DateType(), False)
])

succeeded_schema = StructType([
    StructField("success_date", DateType(), False)
])

failed_data = [
    (date(2018, 12, 28),),
    (date(2018, 12, 29),),
    (date(2019, 1, 4),),
    (date(2019, 1, 5),)
]

succeeded_data = [
    (date(2018, 12, 30),),
    (date(2018, 12, 31),),
    (date(2019, 1, 1),),
    (date(2019, 1, 2),),
    (date(2019, 1, 3),),
    (date(2019, 1, 6),)
]

failed_df = spark.createDataFrame(
    failed_data,
    failed_schema
)

succeeded_df = spark.createDataFrame(
    succeeded_data,
    succeeded_schema
)

failed_df.show()
succeeded_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, lit, row_number, min as spark_min, max as spark_max, date_sub, year
from pyspark.sql.window import Window

all_dates_df = (
    failed_df.select(lit("failed").alias("period_state"), col("fail_date").alias("run_date"))
        .unionByName(
            succeeded_df.select(lit("succeeded").alias("period_state"), col("success_date").alias("run_date"))
        )
        .filter(year(col("run_date")) == 2019)
)

window_spec = Window.partitionBy("period_state").orderBy("run_date")

result_df = (
    all_dates_df
        .withColumn("row_no", row_number().over(window_spec))
        .groupBy(col("period_state"), date_sub(col("run_date"), col("row_no")))
        .agg(
            spark_min(col("run_date")).alias("start_date"),
            spark_max(col("run_date")).alias("end_date")
        )
        .select("period_state", "start_date", "end_date")
        .orderBy("start_date")
)

result_df.show(truncate=False)
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, lit, year, row_number, date_sub, min as spark_min, max as spark_max
from pyspark.sql.window import Window

window_spec = Window.partitionBy("period_state").orderBy("date")

result_df = (
    failed_df
        .select(lit("failed").alias("period_state"), col("fail_date").alias("date"))
        .unionAll(
            succeeded_df
                .select(lit("succeeded").alias("period_state"), col("success_date").alias("date"))
        )
        .filter(year(col("date")) == 2019)
        .withColumn("rnk", row_number().over(window_spec))
        .groupBy("period_state", date_sub(col("date"), col("rnk")))
        .agg(
            spark_min("date").alias("start_date"),
            spark_max("date").alias("end_date"),
        )
        .select("period_state", "start_date", "end_date")
        .orderBy("start_date")
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1


# endregion