from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

calls_schema = StructType([
    StructField("from_id", IntegerType(), False),
    StructField("to_id", IntegerType(), False),
    StructField("duration", IntegerType(), False)
])

calls_data = [
    (1, 2, 59),
    (2, 1, 11),
    (1, 3, 20),
    (3, 4, 100),
    (3, 4, 200),
    (3, 4, 200),
    (4, 3, 499)
]

calls_df = spark.createDataFrame(calls_data, calls_schema)
calls_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, count, sum as spark_sum
result_df = (
    calls_df.alias("c1")
        .select(col("from_id").alias("person1"), col("to_id").alias("person2"), col("duration"))
        .filter(col("person1") < col("person2"))
        .unionAll(
            calls_df.alias("c2")
                .select(col("to_id").alias("person1"), col("from_id").alias("person2"), col("duration"))
                .filter(col("person1") < col("person2"))
        )
        .groupBy("person1", "person2")
        .agg(
            count("*").alias("call_count"),
            spark_sum(col("duration")).alias("total_duration")
        )
)
result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, least, greatest, count, sum as spark_sum

result_df = (
    calls_df
        .groupBy(
            least(col("from_id"), col("to_id")).alias("person1"),
            greatest(col("from_id"), col("to_id")).alias("person2"),
        )
        .agg(
            count("*").alias("call_count"),
            spark_sum(col("duration")).alias("total_duration")
        )
)
result_df.show()
# endregion

print("--- Solution #3 ---")
# region: solution #3
from pyspark.sql.functions import col, count, sum as spark_sum, when

result_df = (
    calls_df
        .groupBy(
            when(col("from_id") < col("to_id"), col("from_id")).otherwise(col("to_id")).alias("person1"),
            when(col("from_id") > col("to_id"), col("from_id")).otherwise(col("to_id")).alias("person2"),
        )
        .agg(
            count("*").alias("call_count"),
            spark_sum(col("duration")).alias("total_duration")
        )
)
result_df.show()

# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion