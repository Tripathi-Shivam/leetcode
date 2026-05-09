from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("employee_id", IntegerType(), False),
    StructField("department_id", IntegerType(), False),
    StructField("primary_flag", StringType(), False)
])

data = [
    (1, 1, "N"),
    (2, 1, "Y"),
    (2, 2, "N"),
    (3, 3, "N"),
    (4, 2, "N"),
    (4, 3, "Y"),
    (4, 4, "N")
]

employee_df = spark.createDataFrame(data, schema)
employee_df.show()

# solution - using union
from pyspark.sql.functions import col, count

primary_set_1_df = (
    employee_df
        .filter(col("primary_flag") == "Y")
        .select("employee_id", "department_id")
)

primary_set_2_df = (
    employee_df
        .groupBy("employee_id")
        .agg(count(col("department_id")).alias("department_count"))
        .filter(col("department_count") == 1)
        .join(employee_df, on = "employee_id", how = "inner")
        .select("employee_id", "department_id")
)

result_df = primary_set_1_df \
                .union(primary_set_2_df)

result_df.show()

# solution - using window
from pyspark.sql.functions import col, count
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("employee_id"))

result = (
    employee_df
        .withColumn("department_count", count(col("department_id")).over(window_spec))
        .filter(
            (col("primary_flag") == 'Y')
            | (col("department_count") == 1)
        )
        .select("employee_id", "department_id")
)
result.show()