from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

student_schema = StructType([
    StructField("student_id", IntegerType(), False),
    StructField("student_name", StringType(), False)
])

exam_schema = StructType([
    StructField("exam_id", IntegerType(), False),
    StructField("student_id", IntegerType(), False),
    StructField("score", IntegerType(), False)
])

student_data = [
    (1, "Daniel"),
    (2, "Jade"),
    (3, "Stella"),
    (4, "Jonathan"),
    (5, "Will")
]

exam_data = [
    (10, 1, 70),
    (10, 2, 80),
    (10, 3, 90),
    (20, 1, 80),
    (30, 1, 70),
    (30, 3, 80),
    (30, 4, 90),
    (40, 1, 60),
    (40, 2, 70),
    (40, 4, 80)
]

student_df = spark.createDataFrame(
    student_data,
    student_schema
)

exam_df = spark.createDataFrame(
    exam_data,
    exam_schema
)

student_df.show()
exam_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, rank, min as spark_min
from pyspark.sql.window import Window

window_spec_1 = Window.partitionBy(col("exam_id")).orderBy(col("score").desc())
window_spec_2 = Window.partitionBy(col("exam_id")).orderBy(col("score").asc())

result_df = (
    exam_df
        .withColumn("first_rnk", rank().over(window_spec_1))
        .withColumn("last_rnk", rank().over(window_spec_2))
        .groupBy("student_id")
        .agg(
            spark_min(col("first_rnk")).alias("min_first_rnk"),
            spark_min(col("last_rnk")).alias("min_last_rnk")
        )
        .filter((col("min_first_rnk") != 1) & (col("min_last_rnk") != 1))
        .alias("e")
        .join(student_df.alias("s"), on = "student_id", how = "inner")
        .select(col("e.student_id"), col("s.student_name"))
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion