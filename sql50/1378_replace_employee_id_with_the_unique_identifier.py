from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

employees_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), True)
])

employees_data = [
    (1, "Alice"),
    (7, "Bob"),
    (11, "Meir"),
    (90, "Winston"),
    (3, "Jonathan"),
]

df_employees = spark.createDataFrame(employees_data, employees_schema)

employee_uni_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("unique_id", IntegerType(), True)
])

employee_uni_data = [
    (3,  1),
    (11, 2),
    (90, 3),
]

df_employee_uni = spark.createDataFrame(employee_uni_data, employee_uni_schema)

df_employees.show(truncate = False)
df_employee_uni.show(truncate = False)

# solution
result = (
    df_employees
        .join(df_employee_uni, on = df_employees["id"] == df_employee_uni["id"], how = "left")
        .select(df_employee_uni["unique_id"], df_employees["name"])
)
result.show()