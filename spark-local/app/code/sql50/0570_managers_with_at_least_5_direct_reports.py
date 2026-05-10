from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

employee_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("department", StringType(), False),
    StructField("managerId", IntegerType(), True)
])

employee_data = [
    (101, "John",  "A", None),
    (102, "Dan",   "A", 101),
    (103, "James", "A", 101),
    (104, "Amy",   "A", 101),
    (105, "Anne",  "A", 101),
    (106, "Ron",   "B", 101),
]

employee = spark.createDataFrame(employee_data, employee_schema)
employee.show()

# solution
from pyspark.sql.functions import col, count

e1 = employee.alias("e1")
e2 = employee.alias("e2")

result = (
    e1
        .join(e2, on = col("e1.managerId") == col("e2.id"), how = "inner")
        .groupBy(col("e2.id"), col("e2.name"))
        .agg(count(col("e1.id")).alias("direct_reports"))
        .filter(col("direct_reports") >= 5)
        .select(col("e2.name"))
)
result.show()