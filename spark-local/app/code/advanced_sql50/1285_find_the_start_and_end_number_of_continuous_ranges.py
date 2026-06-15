from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

logs_schema = StructType([
    StructField("log_id", IntegerType(), False)
])

logs_data = [
    (1,),
    (2,),
    (3,),
    (7,),
    (8,),
    (10,)
]

logs_df = spark.createDataFrame(
    logs_data,
    logs_schema
)

logs_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, row_number, min as spark_min, max as spark_max
from pyspark.sql.window import Window

result_df = (
    logs_df
        .withColumn("row_no", row_number().over(Window.orderBy(col("log_id"))))
        .groupBy(col("log_id") - col("row_no"))
        .agg(spark_min(col("log_id")).alias("start_id"), spark_max(col("log_id")).alias("end_id"))
        .select("start_id", "end_id")
        .orderBy("start_id")
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion