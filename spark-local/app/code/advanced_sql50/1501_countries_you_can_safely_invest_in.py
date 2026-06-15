from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

person_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("phone_number", StringType(), False)
])

country_schema = StructType([
    StructField("name", StringType(), False),
    StructField("country_code", StringType(), False)
])

calls_schema = StructType([
    StructField("caller_id", IntegerType(), False),
    StructField("callee_id", IntegerType(), False),
    StructField("duration", IntegerType(), False)
])

person_data = [
    (3, "Jonathan", "051-1234567"),
    (12, "Elvis", "051-7654321"),
    (1, "Moncef", "212-1234567"),
    (2, "Maroua", "212-6523651"),
    (7, "Meir", "972-1234567"),
    (9, "Rachel", "972-0011100")
]

country_data = [
    ("Peru", "051"),
    ("Israel", "972"),
    ("Morocco", "212"),
    ("Germany", "049"),
    ("Ethiopia", "251")
]

calls_data = [
    (1, 9, 33),
    (2, 9, 4),
    (1, 2, 59),
    (3, 12, 102),
    (3, 12, 330),
    (12, 3, 5),
    (7, 9, 13),
    (7, 1, 3),
    (9, 7, 1),
    (1, 7, 7)
]

country_df = spark.createDataFrame(country_data, country_schema)
person_df = spark.createDataFrame(person_data, person_schema)
calls_df = spark.createDataFrame(calls_data, calls_schema)

country_df.show()
person_df.show()
calls_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, avg, substr, lit

global_avg = calls_df.agg(avg("duration")).collect()[0][0]

result_df = (
    calls_df.alias("cl")
        .join(
            person_df.alias("p"),
            on = (col("cl.caller_id") == col("p.id")) | (col("cl.callee_id") == col("p.id")),
            how = "inner"
        )
        .join(
            country_df.alias("cntry"),
            on = substr(col("p.phone_number"), lit(1), lit(3)) == col("cntry.country_code"),
            how = "inner"
        )
        .groupBy(col("cntry.name").alias("country"))
        .agg(avg(col("cl.duration")).alias("country_avg"))
        .filter(col("country_avg") > lit(global_avg))
        .drop("country_avg")
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion