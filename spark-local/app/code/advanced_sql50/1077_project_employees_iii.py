from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

project_schema = StructType([
    StructField("project_id", IntegerType(), False),
    StructField("employee_id", IntegerType(), False)
])

employee_schema = StructType([
    StructField("employee_id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("experience_years", IntegerType(), False)
])

project_data = [
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 4)
]

employee_data = [
    (1, "Khaled", 3),
    (2, "Ali", 2),
    (3, "John", 3),
    (4, "Doe", 2)
]

project_df = spark.createDataFrame(
    project_data,
    project_schema
)

employee_df = spark.createDataFrame(
    employee_data,
    employee_schema
)

project_df.show()
employee_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, max as spark_max

pro_emp_df = (
    project_df.alias("p")
        .join(employee_df.alias("e"), on = "employee_id", how = "inner")
        .select("p.project_id", "p.employee_id", "e.experience_years")
)

result_df = (
    pro_emp_df
        .groupBy(col("project_id"))
        .agg(spark_max(col("experience_years")).alias("max_exp"))
        .alias("p1")
        .join(
            pro_emp_df.alias("p2"), 
            on = (col("p1.project_id") == col("p2.project_id")) & (col("p1.max_exp") == col("p2.experience_years")), 
            how = "inner"
        )
        .select("p2.project_id", "p2.employee_id")
)

result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, rank
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("project_id")).orderBy(col("experience_years").desc())

result_df = (
    project_df.alias("p")
        .join(employee_df.alias("e"), on = "employee_id", how = "inner")
        .select("p.project_id", "p.employee_id", "e.experience_years")
        .withColumn("rnk", rank().over(window_spec))
        .filter(col("rnk") == 1)
        .select("project_id", "employee_id")
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion