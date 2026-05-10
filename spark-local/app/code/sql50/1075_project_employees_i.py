from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

project_schema = StructType([
    StructField("project_id",  IntegerType(), False),
    StructField("employee_id", IntegerType(), False),
])

project_data = [
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 4),
]

project = spark.createDataFrame(project_data, project_schema)

employee_schema = StructType([
    StructField("employee_id",      IntegerType(), False),
    StructField("name",             StringType(),  False),
    StructField("experience_years", IntegerType(), False),
])

employee_data = [
    (1, "Khaled", 3),
    (2, "Ali",    2),
    (3, "John",   1),
    (4, "Doe",    2),
]

employee = spark.createDataFrame(employee_data, employee_schema)

project.show()
employee.show()

# solution
from pyspark.sql.functions import round, avg

result = (
    project
        .join(employee, on = project.employee_id == employee.employee_id, how = "left")
        .groupBy(project.project_id)
        .agg(
            round(
                avg(employee.experience_years),
            2).alias("average_years")
        )
)
result.show()