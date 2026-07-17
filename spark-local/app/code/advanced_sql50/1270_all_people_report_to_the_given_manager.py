from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

employees_schema = StructType([
    StructField("employee_id", IntegerType(), False),
    StructField("employee_name", StringType(), False),
    StructField("manager_id", IntegerType(), True)
])

employees_data = [
    (1, "Boss", 1),
    (3, "Alice", 3),
    (2, "Bob", 1),
    (4, "Daniel", 2),
    (7, "Luis", 4),
    (8, "Jhon", 3),
    (9, "Angela", 8),
    (77, "Robert", 1)
]

employees_df = spark.createDataFrame(
    employees_data,
    employees_schema
)
employees_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col

result_df = (
    employees_df.alias("e")
        .join(employees_df.alias("m2"), on = col("e.manager_id") == col("m2.employee_id"), how = "left")
        .join(employees_df.alias("m3"), on = col("m2.manager_id") == col("m3.employee_id"), how = "left")
        .filter(
            (col("e.employee_id") != 1)
            & (
                (col("e.manager_id") == 1)
                | (col("m2.manager_id") == 1)
                | (col("m3.manager_id") == 1)
            )
        )
        .select(col("e.employee_id"))
        .distinct()
)

result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col

result_df = (
    # anchor
    employees_df
        .filter((col("employee_id") != 1) & (col("manager_id") == 1))
        .select("employee_id")
)

current_df = result_df
# recursive loop
while True:
    # print("Current DF:")
    # current_df.show()
    next_level_df = (
        employees_df.alias("e")
            .join(current_df.alias("c"), on = col("e.manager_id") == col("c.employee_id"), how = "inner")
            .select(col("e.employee_id"))
    )
    # print("Next Level DF:")
    # next_level_df.show()

    if next_level_df.count() == 0:
        break

    result_df = (
        result_df
            .union(next_level_df)
    )
    current_df = next_level_df

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

current_df = (
    employees_df
        .filter((col("employee_id") != 1) & (col("manager_id") == 1))
        .select("employee_id")
)

result_df = current_df

while True:
    next_df = (
        employees_df.alias("e")
            .join(current_df.alias("m"), on = col("e.manager_id") == col("m.employee_id"), how = "inner")
            .select("e.employee_id")
    )

    if next_df.count() == 0:
        break

    result_df = (
        result_df.union(next_df)
    )
    current_df = next_df

result_df.show()
# endregion