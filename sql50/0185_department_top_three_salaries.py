from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

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
    (1, "Joe", 85000, 1),
    (2, "Henry", 80000, 2),
    (3, "Sam", 60000, 2),
    (4, "Max", 90000, 1),
    (5, "Janet", 69000, 1),
    (6, "Randy", 85000, 1),
    (7, "Will", 70000, 1)
]

department_data = [
    (1, "IT"),
    (2, "Sales")
]

employee_df = spark.createDataFrame(employee_data, employee_schema)
department_df = spark.createDataFrame(department_data, department_schema)

employee_df.show()
department_df.show()

# solution
from pyspark.sql.functions import col, dense_rank
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("d.id")).orderBy(col("salary").desc())

result_df = (
    employee_df.alias("e")
        .join(
            department_df.alias("d"),
            on = col("e.departmentId") == col("d.id"),
            how = "inner"
        )
        .withColumn("rnk", dense_rank().over(window_spec))
        .filter(col("rnk") <= 3)
        .select(col("d.name").alias("department"), col("e.name").alias("employee"), col("e.salary"))
)
result_df.show()