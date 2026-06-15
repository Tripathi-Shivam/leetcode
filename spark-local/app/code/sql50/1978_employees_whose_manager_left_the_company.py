from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("employee_id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("manager_id", IntegerType(), True),
    StructField("salary", IntegerType(), False)
])

data = [
    (3, "Mila", 9, 60301),
    (12, "Antonella", None, 31000),
    (13, "Emery", None, 67084),
    (1, "Kalel", 11, 21241),
    (9, "Mikaela", None, 50937),
    (11, "Jose", 6, 28485)
]

employees_df = spark.createDataFrame(data, schema)
employees_df.show()

# region: solution
from pyspark.sql.functions import col

result_df = (
    employees_df.alias("e")
        .join(employees_df.alias("m"), on = col("e.manager_id") == col("m.employee_id"), how = "left")
        .filter((col("m.employee_id").isNull()) & (col("e.salary") < 30000) & (col("e.manager_id").isNotNull()))
        .select(col("e.employee_id"))
        .orderBy(col("e.employee_id").asc())
)
result_df.show()
# endregion

# region: solution - left_anti
from pyspark.sql.functions import col

result_df = (
    employees_df.alias("e")
        .join(employees_df.alias("m"), on = col("e.manager_id") == col("m.employee_id"), how = "left_anti")
        .filter((col("e.salary") < 30000) & (col("e.manager_id").isNotNull()))
        .select(col("e.employee_id"))
        .orderBy(col("e.employee_id").asc())
)
result_df.show()
# endregion

# region: practice
print("----------- Practice Solution ----------")

# endregion