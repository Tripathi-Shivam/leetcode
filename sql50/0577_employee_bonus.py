from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

employee_schema = StructType([
    StructField("empId", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("supervisor", IntegerType(), True),
    StructField("salary", IntegerType(), False)
])

employee_data = [
    (3, "Brad",   None, 4000),
    (1, "John",   3,    1000),
    (2, "Dan",    3,    2000),
    (4, "Thomas", 3,    4000),
]

employee = spark.createDataFrame(employee_data, employee_schema)

bonus_schema = StructType([
    StructField("empId", IntegerType(), False),
    StructField("bonus", IntegerType(), False)
])

bonus_data = [
    (2, 500),
    (4, 2000)
]

bonus = spark.createDataFrame(bonus_data, bonus_schema)

employee.show()
bonus.show()

# solution
from pyspark.sql.functions import col

result = (
    employee
        .alias("e")
        .join(bonus.alias("b"), on = "empID", how = "left")
        .filter(
            (col("b.bonus")< 1000)
            | (col("b.bonus").isNull())
        )
        .select(col("e.name"), col("b.bonus"))
)

result.show()