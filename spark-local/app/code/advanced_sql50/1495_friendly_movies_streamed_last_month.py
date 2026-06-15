from datetime import datetime

from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    TimestampType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

tv_program_schema = StructType([
    StructField("program_date", TimestampType(), False),
    StructField("content_id", IntegerType(), False),
    StructField("channel", StringType(), False)
])

content_schema = StructType([
    StructField("content_id", IntegerType(), False),
    StructField("title", StringType(), False),
    StructField("kids_content", StringType(), False),
    StructField("content_type", StringType(), False)
])

tv_program_data = [
    (datetime(2020, 6, 10, 8, 0), 1, "LC-Channel"),
    (datetime(2020, 5, 11, 12, 0), 2, "LC-Channel"),
    (datetime(2020, 5, 12, 12, 0), 3, "LC-Channel"),
    (datetime(2020, 5, 13, 14, 0), 4, "Disney Ch"),
    (datetime(2020, 6, 18, 14, 0), 4, "Disney Ch"),
    (datetime(2020, 7, 15, 16, 0), 5, "Disney Ch")
]

content_data = [
    (1, "Leetcode Movie", "N", "Movies"),
    (2, "Alg. for Kids", "Y", "Series"),
    (3, "Database Sols", "N", "Series"),
    (4, "Aladdin", "Y", "Movies"),
    (5, "Cinderella", "Y", "Movies")
]

tv_program_df = spark.createDataFrame(
    tv_program_data,
    tv_program_schema
)

content_df = spark.createDataFrame(
    content_data,
    content_schema
)

tv_program_df.show()
content_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, lit, date_format
result_df = (
    tv_program_df.alias("t")
        .join(
            content_df.alias("c"),
            on = "content_id",
            how = "inner"
        )
        .filter(
            (date_format(col("t.program_date"), "yyyy-MM") == lit("2020-06"))
            & (col("c.content_type") == "Movies")
            & (col("c.kids_content") == "Y")
        )
        .select("c.title")
        .distinct()
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion