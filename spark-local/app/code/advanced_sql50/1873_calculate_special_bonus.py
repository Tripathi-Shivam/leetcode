from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

employees_schema = StructType([
    StructField("employee_id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("salary", IntegerType(), False)
])

employees_data = [
    (2, "Meir", 3000),
    (3, "Michael", 3800),
    (7, "Addilyn", 7400),
    (8, "Juan", 6100),
    (9, "Kannon", 7700)
]

employees_df = spark.createDataFrame(employees_data, employees_schema)
employees_df.show()

# region: solution
from pyspark.sql.functions import col, when, rlike, lit

result_df = (
    employees_df
        .select(
            col("employee_id"),
            when(
                (col("employee_id") % 2 == 1)
                & ~(col("name").rlike("^M")), # (~col("name").startswith("M")),
                col("salary")
            ).otherwise(lit(0))
            .alias("bonus")
        )
        .orderBy("employee_id")
)
result_df.show()
# endregion

# region: practice
print("--- Practice ---")

# endregion 