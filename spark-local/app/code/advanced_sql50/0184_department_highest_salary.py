from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

employee_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("salary", IntegerType(), False),
    StructField("departmentId", IntegerType(), False)
])

department_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False)
])

employee_data = [
    (1, "Joe", 70000, 1),
    (2, "Jim", 90000, 1),
    (3, "Henry", 80000, 2),
    (4, "Sam", 60000, 2),
    (5, "Max", 90000, 1)
]

department_data = [
    (1, "IT"),
    (2, "Sales")
]

employee_df = spark.createDataFrame(
    employee_data,
    employee_schema
)

department_df = spark.createDataFrame(
    department_data,
    department_schema
)

employee_df.show()
department_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, max as spark_max

result_df = (
    employee_df.alias("e1")
        .join(
            employee_df.groupBy("departmentId").agg(spark_max("salary").alias("max_salary")).alias("e2"),
            on = (col("e1.departmentId") == col("e2.departmentId")) & (col("e1.salary") == col("e2.max_salary")),
            how = "inner"
        )
        .join(department_df.alias("d"), on = col("e1.departmentId") == col("d.id"), how = "inner")
        .select(col("d.name").alias("department"), col("e1.name").alias("employee"), col("e2.max_salary").alias("salary"))
)

result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, max as spark_max
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("e.departmentId")).orderBy(col("e.salary").desc())

result_df = (
    employee_df.alias("e")
        .join(department_df.alias("d"), on = col("e.departmentId") == col("d.id"), how = "inner")
        .withColumn("max_salary", spark_max(col("e.salary")).over(window_spec))
        .filter(col("e.salary") == col("max_salary"))
        .select(col("d.name").alias("department"), col("e.name").alias("employee"), col("max_salary").alias("salary"))
)

result_df.show()
# endregion

print("--- Solution #3 ---")
# region: solution #3
from pyspark.sql.functions import col, first_value
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("e.departmentId")).orderBy(col("e.salary").desc())

result_df = (
    employee_df.alias("e")
        .join(department_df.alias("d"), on = col("e.departmentId") == col("d.id"), how = "inner")
        .withColumn("max_salary", first_value(col("e.salary")).over(window_spec))
        .filter(col("e.salary") == col("max_salary"))
        .select(col("d.name").alias("department"), col("e.name").alias("employee"), col("max_salary").alias("salary"))
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion