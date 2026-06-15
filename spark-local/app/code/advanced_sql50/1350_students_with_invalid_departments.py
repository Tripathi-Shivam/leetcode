from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

students_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("department_id", IntegerType(), False)
])

departments_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False)
])

students_data = [
    (23, "Alice", 1),
    (1, "Bob", 7),
    (5, "Jennifer", 13),
    (2, "John", 14),
    (4, "Jasmine", 77),
    (3, "Steve", 74),
    (6, "Luis", 1),
    (8, "Jonathan", 7),
    (7, "Daiana", 33),
    (11, "Madelynn", 1)
]

departments_data = [
    (1, "Electrical Engineering"),
    (7, "Computer Engineering"),
    (13, "Business Administration")
]

students_df = spark.createDataFrame(
    students_data,
    students_schema
)

departments_df = spark.createDataFrame(
    departments_data,
    departments_schema
)

students_df.show()
departments_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col

result_df = (
    students_df.alias("s")
        .join(
            departments_df.alias("d"),
            on = col("s.department_id") == col("d.id"),
            how = "left_anti"
        )
        .select(col("s.id"), col("s.name"))
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion