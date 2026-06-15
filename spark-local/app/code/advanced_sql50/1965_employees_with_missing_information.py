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
    StructField("name", StringType(), False)
])

salaries_schema = StructType([
    StructField("employee_id", IntegerType(), False),
    StructField("salary", IntegerType(), False)
])

employees_data = [
    (2, "Crew"),
    (4, "Haven"),
    (5, "Kristian")
]

salaries_data = [
    (5, 76071),
    (1, 22517),
    (4, 63539)
]

employees_df = spark.createDataFrame(
    employees_data,
    employees_schema
)

salaries_df = spark.createDataFrame(
    salaries_data,
    salaries_schema
)

employees_df.show()
salaries_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col

missing_salaries = (
    employees_df.alias("e")
        .join(
            salaries_df.alias("s"),
            on = "employee_id",
            how = "left"
        )
        .filter((col("e.name").isNull()) | (col("s.salary").isNull()))
        .select("e.employee_id")
)

missing_names = (
    salaries_df.alias("s")
        .join(
            employees_df.alias("e"),
            on = "employee_id",
            how = "left"
        )
        .filter((col("s.salary").isNull()) | (col("e.name").isNull()))
        .select("s.employee_id")
)

result_df = (
    missing_salaries
        .union(missing_names)
        .orderBy("employee_id")
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion